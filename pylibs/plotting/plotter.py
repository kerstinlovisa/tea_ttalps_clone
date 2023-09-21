from ROOT import TFile, TCanvas, TLegend, TObject
import ROOT
import importlib
import sys
import os
import os.path


def setupLegend(legend):
  legend.SetBorderSize(0)
  # legend.SetFillColor(0)
  # legend.SetFillStyle(0)
  legend.SetTextFont(42)
  legend.SetTextSize(0.035)


def getStackDict(config, file_type, efficiency=False):
  hists_dict = {}
  variables = config.efficiency_plots if efficiency else config.variables

  for name, params in variables.items():
    variable = params[0] if efficiency else name
    title = variable + file_type
    if efficiency:
      title += "_eff"
    hists_dict[name] = ROOT.THStack(title, title)

  return hists_dict


def getLegendDicts(config, file_type, efficiency=False):
  legends_dict = {}
  legend_position = config.legend_position[file_type]
  variables = config.efficiency_plots if efficiency else config.variables
  
  for name in variables.keys():
    legend = TLegend(legend_position[0], legend_position[1], legend_position[2], legend_position[3])
    setupLegend(legend)
    legends_dict[name] = legend

  return legends_dict


def normalizeHist(hist, normalization_type, sample_type, lumi, cross_section):
  
  if normalization_type == "norm1":
    if sample_type == "background":
      hist.Scale(lumi*cross_section/total_backgrounds_integral)
    else:
      hist.Scale(1./hist.Integral())
  elif normalization_type == "to_background":
    if sample_type == "background":
      # TODO: should do this one properly, dividing by initial number of events
      hist.Scale(lumi*cross_section/hist.Integral())
    else:
      hist.Scale(lumi*total_backgrounds_cross_section/hist.Integral())

def setupHist(hist, params, linestyles, sample_type):
  line_color, line_style = linestyles
  
  if sample_type == "signal":
    hist.SetLineStyle(line_style)
    hist.SetLineColor(line_color)
  elif sample_type == "data":
    hist.SetLineColor(ROOT.kBlack)
    hist.SetMarkerStyle(20)
    hist.SetMarkerSize(1)
    hist.SetMarkerColor(ROOT.kBlack)
  else:
    hist.SetLineColorAlpha(line_color, 0)
    hist.SetFillColorAlpha(line_color, 0.7)
    
    
  hist.Rebin(params[3])
  hist.Sumw2(False)


def setupFigure(stack, params):
  if stack is None or type(stack) is TObject:
    return

  title, _, _, _, xmin, xmax, ymin, ymax, xlabel, ylabel = params

  if (ymin > 0):
    stack.SetMinimum(ymin)
  if (ymax > 0):
    stack.SetMaximum(ymax)
    
  try:
    stack.GetXaxis().SetLimits(xmin, xmax)
    stack.GetXaxis().SetTitle(xlabel)
    stack.GetYaxis().SetTitle(ylabel)
    stack.SetTitle(title)
  except:
    print("Couldn't set axes limits")
    return


def getEfficiencyHist(input_hist):
  hist = input_hist.Clone()
  initial = hist.GetBinContent(1)
  for bin in range(1, hist.GetNbinsX()+2):
    hist.SetBinContent(bin, hist.GetBinContent(bin)/initial)
  return hist


def checkHist(hist):
  if hist is None or type(hist) is TObject:
    return False
  if hist.GetEntries() == 0:
    return False
  return True


def getTotalBackgroundsIntegral(config):
  entries = 0
  integral = 0
  cross_section = 0
  
  for sample_name, file_info in config.files.items():
    file_name, file_type = file_info
    
    if file_type != "background":
      continue
    
    input_path = config.input_paths[file_type]
    file = TFile.Open(input_path+"/"+sample_name+"/"+config.skim+"/"+file_name, "READ")

    hist_name, _ = next(iter(config.variables.items()))
    hist = file.Get(hist_name) 


    integral += hist.Integral() * config.luminosity_2018 * config.cross_sections[sample_name]
    entries += hist.Integral()
    cross_section += config.cross_sections[sample_name]
    
  return entries, integral, cross_section

def addHistsToStacks(config, input_files, file_name, hists, legends, file_type, efficiency=False):
  variables = config.efficiency_plots if efficiency else config.variables

  cross_section = config.cross_sections[file_name]
  lumi = config.luminosity_2018
  
  file_type = config.files[file_name][1]
  
  background_count = 0
  
  first = True
  for name, values in variables.items():
    params = config.variables[values[0]] if efficiency else values
    hist_name = values[0] if efficiency else name
      

    hist = input_files[file_name].Get(hist_name)
    if not checkHist(hist):
      print(f"Couldn't find hist or it is empty: {hist_name}")
      continue

    if efficiency:
      hist = getEfficiencyHist(hist)

    normalization_type = params[2]
    normalizeHist(hist, normalization_type, file_type, lumi, cross_section)
    
    setupHist(hist, params, config.lines[file_name], file_type)
    hists[file_type][name].Add(hist)
    legends[file_type][name].AddEntry(hist, config.legends[file_name], config.legend_types[file_type])
    
    if file_type == "background" and first:
      background_count += hist.Integral()
      first = False
      
  return background_count


def drawStacks(config, backgrounds_included, data_included, hists, legends, efficiency=False):

  # create output path if it doesn't exist
  if not os.path.exists(config.output_path):
    os.makedirs(config.output_path)

  variables = config.efficiency_plots if efficiency else config.variables


  for name, params in variables.items():
    
    title = "canvas_"+name
    if efficiency:
      title += "_eff"
    
    hist_params = config.variables[params[0]] if efficiency else params
      
    canvas = TCanvas(title, title, 800, 600)
    canvas.cd()
    canvas.SetLogy(hist_params[1])
    
    if backgrounds_included:
      hists["background"][name].Draw("hist")
      setupFigure(hists["background"][name], hist_params)
      hists["signal"][name].Draw("nostack same")
    else:
      hists["signal"][name].Draw("hist nostack")
      setupFigure(hists["signal"][name], hist_params)

    if data_included:
      hists["data"][name].Draw("nostack same P")

    legends["signal"][name].Draw()
    legends["background"][name].Draw()
    legends["data"][name].Draw()

    canvas.Update()
    canvas.SaveAs(config.output_path+"/"+name+".pdf")
 

def getEntries(hists):
  entries = 0
  for hist in hists.values():
    entries += hist.GetEntries()
  return entries
