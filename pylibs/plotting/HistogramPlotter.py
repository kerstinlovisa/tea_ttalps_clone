from ROOT import TFile, TCanvas, TObject
import ROOT
import os
import os.path

from Sample import SampleType


class HistogramPlotter:
  def __init__(self, config):
    self.config = config
    
    total_backgrounds_entries, total_backgrounds_integral, total_backgrounds_cross_section = self.__getTotalBackgroundsIntegral()
    self.total_backgrounds_entries = total_backgrounds_entries
    self.total_backgrounds_integral = total_backgrounds_integral
    self.total_backgrounds_cross_section = total_backgrounds_cross_section
    
    self.legends = {sample_type: self.__getLegendDicts(sample_type) for sample_type in SampleType}
    self.hists = {sample_type: self.__getStackDict(sample_type) for sample_type in SampleType}
    
    self.backgrounds_included = False
    self.data_included = False
  
  def addHistsToStacks(self, input_file, sample):
    cross_section = sample.cross_section
    lumi = self.config.luminosity_2018
    sample_type = sample.sample_type
    
    self.backgrounds_included |= sample.sample_type == SampleType.background
    self.data_included |= sample.sample_type == SampleType.data
    
    for hist_name, params in self.config.variables.items():
      hist = input_file.Get(hist_name)
      if not self.__checkHist(hist):
        print(f"Couldn't find hist or it is empty: {hist_name}")
        continue

      normalization_type = params[2]
      self.__normalizeHist(hist, normalization_type, sample_type, lumi, cross_section)
      self.__setupHist(hist, sample, params[3])
      self.hists[sample_type][hist_name].Add(hist)
      self.legends[sample_type][hist_name].AddEntry(hist, sample.legend_description, self.config.legends[sample_type].options)  
  
  def drawStacks(self):

    # create output path if it doesn't exist
    if not os.path.exists(self.config.output_path):
      os.makedirs(self.config.output_path)

    variables = self.config.variables

    for name, params in variables.items():
      title = "canvas_"+name
      hist_params = params
      
      canvas = TCanvas(title, title, 800, 600)
      canvas.cd()
      canvas.SetLogy(hist_params[1])
      
      if self.backgrounds_included:
        self.hists[SampleType.background][name].Draw("hist")
        self.__setupFigure(self.hists[SampleType.background][name], hist_params)
        self.hists[SampleType.signal][name].Draw("nostack same")
      else:
        self.hists[SampleType.signal][name].Draw("hist nostack")
        self.__setupFigure(self.hists[SampleType.signal][name], hist_params)

      if self.data_included:
        self.hists[SampleType.data][name].Draw("nostack same P")

      for sample_type in SampleType:
        self.legends[sample_type][name].Draw()
      
      canvas.Update()
      canvas.SaveAs(self.config.output_path+"/"+name+".pdf")
  
  def __getStackDict(self, sample_type):
    hists_dict = {}
    
    for name in self.config.variables.keys():
      title = name + sample_type.name
      hists_dict[name] = ROOT.THStack(title, title)

    return hists_dict

  def __getLegendDicts(self, sample_type):
    legends_dict = {}
    
    for name in self.config.variables.keys():
      legends_dict[name] = self.config.legends[sample_type].getRootLegend()

    return legends_dict

  def __normalizeHist(self, hist, normalization_type, sample_type, lumi, cross_section):
    
    if normalization_type == "norm1":
      if sample_type == SampleType.background:
        hist.Scale(lumi*cross_section/self.total_backgrounds_integral)
      else:
        hist.Scale(1./hist.Integral())
    elif normalization_type == "to_background":
      if sample_type == SampleType.background:
        # TODO: should do this one properly, dividing by initial number of events
        hist.Scale(lumi*cross_section/hist.Integral())
      else:
        hist.Scale(lumi*self.total_backgrounds_cross_section/hist.Integral())

  def __setupHist(self, hist, sample, rebin):
    hist.SetLineStyle(sample.line_style)
    hist.SetLineColor(sample.line_color)
    hist.SetMarkerStyle(sample.marker_style)
    hist.SetMarkerSize(sample.marker_size)
    hist.SetMarkerColor(sample.marker_color)
    hist.SetLineColorAlpha(sample.line_color, sample.line_alpha)
    hist.SetFillColorAlpha(sample.fill_color, sample.fill_alpha)
    hist.Rebin(rebin)
    hist.Sumw2(False)

  def __setupFigure(self, stack, params):
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

  def __checkHist(self, hist):
    if hist is None or type(hist) is TObject:
      return False
    if hist.GetEntries() == 0:
      return False
    return True

  def __getTotalBackgroundsIntegral(self):
    entries = 0
    integral = 0
    cross_section = 0
    
    for sample in self.config.samples:
      if sample.sample_type != SampleType.background:
        continue
      
      
      file = TFile.Open(sample.file_path, "READ")

      hist_name, _ = next(iter(self.config.variables.items()))
      hist = file.Get(hist_name) 


      integral += hist.Integral() * self.config.luminosity_2018 * sample.cross_section
      entries += hist.Integral()
      cross_section += sample.cross_section
      
    return entries, integral, cross_section
