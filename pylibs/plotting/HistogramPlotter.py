from ROOT import TCanvas, gStyle, THStack
import ROOT
import os
import os.path
import copy

from Sample import SampleType
from Styler import Styler
from HistogramNormalizer import HistogramNormalizer


class HistogramPlotter:
  def __init__(self, config):
    gStyle.SetOptStat(0)
    
    self.config = config
    
    self.normalizer = HistogramNormalizer(config)
    self.styler = Styler(config)
    
    self.legends = {sample_type: self.__getLegendDicts(sample_type) for sample_type in SampleType}
    self.stacks = {sample_type: self.__getStackDict(sample_type) for sample_type in SampleType}
    self.histsAndSamples = {}
    self.hists2d = {sample_type: {} for sample_type in SampleType}
    
    self.data_included = any(sample.type == SampleType.data for sample in self.config.samples)
    self.backgrounds_included = any(sample.type == SampleType.background for sample in self.config.samples)
    self.signals_included = any(sample.type == SampleType.signal for sample in self.config.samples)
    
    self.show_ratios = self.backgrounds_included and self.data_included and self.config.show_ratio_plots
    
    self.histosamples = []
    
    if not os.path.exists(self.config.output_path):
      os.makedirs(self.config.output_path)

  def addHistosample(self, hist, sample, input_file):
    hist.load(input_file)
    self.histosamples.append((copy.deepcopy(hist), sample))

  def __getDataHist(self, input_hist):
    for hist, sample in self.histosamples:
      if sample.type is not SampleType.data:
        continue
      if input_hist.getName() == hist.getName():
        return hist.hist
    return None
  
  
  def buildStacks(self):
    for hist, sample in self.histosamples:
      if not hist.isGood():
        continue
      
      self.normalizer.normalize(hist, sample, self.__getDataHist(hist))
      hist.setup(sample)
      
      self.stacks[sample.type][hist.getName()].Add(hist.hist)
      self.legends[sample.type][hist.getName()].AddEntry(hist.hist, sample.legend_description, self.config.legends[sample.type].options)  
  
  def addHists2D(self, input_file, sample):
    if not hasattr(self.config, "histograms2D"):
      return
    
    for hist in self.config.histograms2D:
      hist.load(input_file)
      
      if not hist.isGood():
        continue
      
      hist.setup()
      self.hists2d[sample.type][hist.getName()] = hist.hist
  
  def __drawLineAtOne(self, canvas, hist):
    canvas.cd(2)
    global line
    line = ROOT.TLine(hist.x_min, 1, hist.x_max, 1)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineStyle(ROOT.kDashed)
    line.Draw()
  
  def __drawRatioPlot(self, canvas, hist):
    if not self.show_ratios:
      return
    
    canvas.cd(2)
    global ratio_hist
    ratio_hist = self.__getRatioStack(hist)
    if ratio_hist:
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
    
  def __drawLegens(self, canvas, hist):
    canvas.cd(1)
    for sample_type in self.legends.keys():
      if hist.getName() not in self.legends[sample_type].keys():
        continue
      self.legends[sample_type][hist.getName()].Draw()

  def __drawHists(self, canvas, hist):
    canvas.cd(1)
    
    options = {
      SampleType.background: "hist",
      SampleType.signal: "nostack e",
      SampleType.data: "nostack pe",
    }
    
    for i, sample_type in enumerate(SampleType):
      opt = options[sample_type] if i==0 else options[sample_type]+" same"
      self.stacks[sample_type][hist.getName()].Draw(opt)
      self.styler.setupFigure(self.stacks[sample_type][hist.getName()], hist)
  
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
      self.__drawLegens(canvas, hist)
      
      canvas.Update()
      canvas.SaveAs(self.config.output_path+"/"+hist.getName()+".pdf")
  
  def drawHists2D(self):
    if not hasattr(self.config, "histograms2D"):
      return

    for hist in self.config.histograms2D:
      for sample in self.config.samples:
        title = hist.getName() + "_" + sample.name
        canvas = TCanvas(title, title, self.config.canvas_size[0], self.config.canvas_size[1])  
        canvas.cd()
      
        self.hists2d[sample.type][hist.getName()].Draw("colz")
        self.styler.setupFigure2D(self.hists2d[sample.type][hist.getName()], hist)
      
        canvas.Update()
        canvas.SaveAs(self.config.output_path+"/"+title+".pdf")
  
  def __getRatioStack(self, hist):
    try:
      data_hist = self.stacks[SampleType.data][hist.getName()].GetHists()[0]
    except:
      return None
    ratio_hist = data_hist.Clone("ratio_"+hist.getName())
    
    backgrounds_sum = ROOT.TH1D("backgrounds_sum_"+hist.getName(), "backgrounds_sum_"+hist.getName(),
                                data_hist.GetNbinsX(),
                                data_hist.GetXaxis().GetBinLowEdge(1), 
                                data_hist.GetXaxis().GetBinUpEdge(data_hist.GetNbinsX()))
    
    for background_hist in self.stacks[SampleType.background][hist.getName()].GetHists():  
      backgrounds_sum.Add(background_hist)
    
    ratio_hist.Divide(backgrounds_sum)
    
    ratio_stack = THStack("ratio_stack_"+hist.getName(), "ratio_stack_"+hist.getName())
    ratio_stack.Add(ratio_hist)
    
    return ratio_stack
  
  def __getBackgroundUncertaintyHist(self, hist):
    try:
      background_hist = self.stacks[SampleType.background][hist.getName()].GetHists()[0]
    except:
      return None
    
    uncertainty_hist = ROOT.TH1D("backgrounds_unc_"+hist.getName(), "backgrounds_unc_"+hist.getName(),
                                  background_hist.GetNbinsX(),
                                  background_hist.GetXaxis().GetBinLowEdge(1), 
                                  background_hist.GetXaxis().GetBinUpEdge(background_hist.GetNbinsX()))
    
      
    for background_hist in self.stacks[SampleType.background][hist.getName()].GetHists():  
      uncertainty_hist.Add(background_hist)
    
    return uncertainty_hist
  
  def __getStackDict(self, sample_type):
    hists_dict = {}
    
    for hist in self.config.histograms:
      title = hist.getName() + sample_type.name
      hists_dict[hist.getName()] = ROOT.THStack(title, title)

    return hists_dict

  def __getLegendDicts(self, sample_type):
    legends_dict = {}
    
    for hist in self.config.histograms:
      if sample_type in self.config.legends.keys():
        legends_dict[hist.getName()] = self.config.legends[sample_type].getRootLegend()

    return legends_dict
  