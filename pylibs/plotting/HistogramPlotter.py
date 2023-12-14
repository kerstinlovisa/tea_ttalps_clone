from ROOT import TCanvas, gStyle, THStack
import ROOT
import os
import os.path
import copy

from Sample import SampleType
from Styler import Styler
from HistogramNormalizer import HistogramNormalizer
from CmsLabelsManager import CmsLabelsManager
from Logger import *


class HistogramPlotter:
  def __init__(self, config):
    gStyle.SetOptStat(0)
    
    self.config = config
    
    self.normalizer = HistogramNormalizer(config)
    self.styler = Styler(config)
    self.cmsLabelsManager = CmsLabelsManager(config)
    
    self.legends = {}
    
    self.stacks = {sample_type: self.__getStackDict(sample_type) for sample_type in SampleType}
    self.histsAndSamples = {}
    self.hists2d = {sample_type: {} for sample_type in SampleType}
    
    self.data_included = any(sample.type == SampleType.data for sample in self.config.samples)
    self.backgrounds_included = any(sample.type == SampleType.background for sample in self.config.samples)
    
    self.show_ratios = self.backgrounds_included and self.data_included and self.config.show_ratio_plots
    
    self.histosamples = []
    self.histosamples2D = []
    self.data_integral = {}
    
    if not os.path.exists(self.config.output_path):
      os.makedirs(self.config.output_path)

  def addHistosample(self, hist, sample, input_file):
    hist.load(input_file)
    
    if not hist.isGood():
      warn(f"No good histogram {hist.getName()} for sample {sample.name}")
      return
    
    self.histosamples.append((copy.deepcopy(hist), sample))
    
    if sample.type is SampleType.data:
      self.data_integral[hist.getName()] = hist.hist.Integral()
  
  def addHistosample2D(self, hist, sample, input_file):
    hist.load(input_file)
    self.histosamples2D.append((copy.deepcopy(hist), sample))
  
  def setupLegends(self):
    already_added = []
    
    for hist, sample in self.histosamples:
      if hist.getName() not in self.legends.keys():
        self.legends[hist.getName()] = {}
      
      if sample.custom_legend is not None:
        self.legends[hist.getName()][sample.name] = sample.custom_legend.getRootLegend()
      elif (hist.getName(), sample.type) not in already_added:
        self.legends[hist.getName()][sample.type] = self.config.legends[sample.type].getRootLegend()
        already_added.append((hist.getName(), sample.type))
  
  def __getDataIntegral(self, input_hist):
    if input_hist.getName() in self.data_integral.keys():
      return self.data_integral[input_hist.getName()]
    return None
  
  def __sortHistosamples(self):
    if hasattr(self.config, "custom_stacks_order"):
      try:
        self.histosamples.sort(key=lambda x: self.config.custom_stacks_order.index(x[1].name))
      except ValueError:
        error("Couldn't sort histograms by custom order. Falling back to default order.")
        
        for _, sample in self.histosamples:
          if sample.name not in self.config.custom_stacks_order:
            error(f"Couldn't find sample {sample.name} in custom order list.")
        
        self.histosamples.sort(key=lambda x: x[1].cross_section, reverse=False)
    else:
      self.histosamples.sort(key=lambda x: x[1].cross_section, reverse=False)
    
  def buildStacks(self):
    self.__sortHistosamples()
    
    for hist, sample in self.histosamples:
      if not hist.isGood():
        warn(f"No good histogram {hist.getName()} for sample {sample.name}")
        continue
      
      self.normalizer.normalize(hist, sample, self.__getDataIntegral(hist))
      hist.setup(sample)
      
      self.stacks[sample.type][hist.getName()].Add(hist.hist)
      
      key = sample.type if sample.custom_legend is None else sample.name
      
      self.legends[hist.getName()][key].AddEntry(hist.hist, sample.legend_description, self.config.legends[sample.type].options)  
  
  def addHists2D(self, input_file, sample):
    if not hasattr(self.config, "histograms2D"):
      return
    
    for hist in self.config.histograms2D:
      hist.load(input_file)
      
      if not hist.isGood():
        warn(f"No good histogram {hist.getName()} for sample {sample.name}")
        continue
      
      hist.setup()
      self.hists2d[sample.type][hist.getName()] = hist.hist
  
  def __drawLineAtOne(self, canvas, hist):
    if not self.show_ratios:
      return
    
    global line
    line = ROOT.TLine(hist.x_min, 1, hist.x_max, 1)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineStyle(ROOT.kDashed)
    
    canvas.cd(2)
    line.Draw()
  
  def __drawRatioPlot(self, canvas, hist):
    if not self.show_ratios:
      return
    
    global ratio_hist
    ratio_hist = self.__getRatioStack(hist)
    if ratio_hist:
      
      canvas.cd(2)
      ratio_hist.Draw("p")
      self.styler.setupFigure(ratio_hist, hist, is_ratio=True)
  
  def __drawUncertainties(self, canvas, hist):
    global background_uncertainty_hist
    background_uncertainty_hist = self.__getBackgroundUncertaintyHist(hist)
    if background_uncertainty_hist is  None:
      return
    
    canvas.cd(1)
    self.styler.setupUncertaintyHistogram(background_uncertainty_hist)
    background_uncertainty_hist.Draw("same e2")
  
    if not self.show_ratios:
      return
    
    global ratio_uncertainty
    ratio_uncertainty = background_uncertainty_hist.Clone("ratio_uncertainty_"+hist.getName())
    ratio_uncertainty.Divide(ratio_uncertainty)
    
    canvas.cd(2)
    ratio_uncertainty.Draw("same e2")
    
  def __drawLegends(self, canvas, hist):
    canvas.cd(1)
    
    if hist.getName() not in self.legends:
      warn(f"Couldn't find legends for histogram: {hist.getName()}")
      return
    
    for legend in self.legends[hist.getName()].values():
      legend.Draw()
    
  def __drawHists(self, canvas, hist):
    canvas.cd(1)
    
    firstPlotted = False
    
    for sample_type in SampleType:
      options = self.config.plotting_options[sample_type]
      options = f"{options} same" if firstPlotted else options
      stack = self.stacks[sample_type][hist.getName()]
      if stack.GetNhists() > 0:
        stack.Draw(options)
        self.styler.setupFigure(stack, hist)
        firstPlotted = True
  
  def __setup_canvas(self, canvas, hist):
    if self.show_ratios:
      canvas.Divide(1, 2)
      self.styler.setup_ratio_pad(canvas.GetPad(2))
      self.styler.setup_main_pad_with_ratio(canvas.GetPad(1))
    else:
      canvas.Divide(1, 1)
      self.styler.setup_main_pad_without_ratio(canvas.GetPad(1))
    
    canvas.GetPad(1).SetLogy(hist.log_y)
  
  def drawStacks(self):
    
    for hist in self.config.histograms:
      canvas = TCanvas(hist.getName(), hist.getName(), self.config.canvas_size[0], self.config.canvas_size[1])
      self.__setup_canvas(canvas, hist)
      
      self.__drawRatioPlot(canvas, hist)
      self.__drawLineAtOne(canvas, hist)
      self.__drawHists(canvas, hist)
      self.__drawUncertainties(canvas, hist)
      self.__drawLegends(canvas, hist)
      self.cmsLabelsManager.drawLabels(canvas)
            
      canvas.Update()
      
      originalErrorLevel = ROOT.gErrorIgnoreLevel
      ROOT.gErrorIgnoreLevel = ROOT.kError
      path = self.config.output_path+"/"+hist.getName()+".pdf"
      info(f"Saving file: {path}")
      canvas.SaveAs(path)
      ROOT.gErrorIgnoreLevel = originalErrorLevel

  def drawHists2D(self):
    if not hasattr(self.config, "histograms2D"):
      return

    for hist, sample in self.histosamples2D:  
      title = hist.getName() + "_" + sample.name
      canvas = TCanvas(title, title, self.config.canvas_size[0], self.config.canvas_size[1])  
      canvas.cd()
      hist.hist.Draw("colz")
      self.styler.setupFigure2D(hist.hist, hist)
    
      canvas.Update()
      canvas.SaveAs(self.config.output_path+"/"+title+".pdf")
  
  def __get_hists_sum(self, hist, doRatio = False):
    base_sample_type = SampleType.data if doRatio else SampleType.background
    
    try:
      base_hist = self.stacks[base_sample_type][hist.getName()].GetHists()[0]
    except Exception:
      return None
    
    title = "backgrounds_" + ("sum" if doRatio else "unc" ) + "_" + hist.getName()
    backgrounds_sum = base_hist.Clone(title) 
    backgrounds_sum.Reset()
    
    for background_hist in self.stacks[SampleType.background][hist.getName()].GetHists():
      backgrounds_sum.Add(background_hist)
    
    if not doRatio:
      return backgrounds_sum

    ratio_hist = base_hist.Clone("ratio_"+hist.getName())
    ratio_hist.Divide(backgrounds_sum)
    ratio_stack = THStack("ratio_stack_"+hist.getName(), "ratio_stack_"+hist.getName())
    ratio_stack.Add(ratio_hist)
    
    return ratio_stack
  
  def __getRatioStack(self, hist):
    return self.__get_hists_sum(hist, doRatio = True)
  
  def __getBackgroundUncertaintyHist(self, hist):
    return self.__get_hists_sum(hist, doRatio = False)
  
  def __getStackDict(self, sample_type):
    hists_dict = {}
    
    for hist in self.config.histograms:
      title = hist.getName() + sample_type.name
      hists_dict[hist.getName()] = ROOT.THStack(title, title)

    return hists_dict

  