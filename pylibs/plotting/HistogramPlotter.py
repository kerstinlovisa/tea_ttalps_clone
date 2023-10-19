from ROOT import TCanvas, TObject, gPad, gStyle, THStack
import ROOT
import os
import os.path

from Sample import SampleType
from Styler import Styler
from HistogramNormalizer import HistogramNormalizer


class HistogramPlotter:
  def __init__(self, config):
    gStyle.SetOptStat(0)
    
    self.config = config
    
    self.normalizer = HistogramNormalizer(config)
    self.styler = Styler()
    
    self.hist_names = [hist.name+hist.suffix for hist in self.config.histograms]
    
    self.legends = {sample_type: self.__getLegendDicts(sample_type) for sample_type in SampleType}
    self.stacks = {sample_type: self.__getStackDict(sample_type) for sample_type in SampleType}
    self.hists2d = {sample_type: {} for sample_type in SampleType}
    
    self.data_included = any(sample.type == SampleType.data for sample in self.config.samples)
    self.backgrounds_included = any(sample.type == SampleType.background for sample in self.config.samples)
    self.signals_included = any(sample.type == SampleType.signal for sample in self.config.samples)
    
    self.initial_background_weight = None
    
    self.data_hists = {}
    
    self.show_ratios = self.backgrounds_included and self.data_included and self.config.show_ratio_plots
    
  
  def addHistsToStacks(self, input_file, sample):
    
    for hist in self.config.histograms:
      hist.load(input_file)
      
      if not hist.isGood():
        continue

      if sample.type == SampleType.data:
        self.data_hists[hist.getName()] = hist.hist

      data_hist = None
      if hist.getName() in self.data_hists:
        data_hist = self.data_hists[hist.getName()]

      self.normalizer.normalize(hist, sample, data_hist)
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
  
  def __draw_line_at_one(self, hist):
    line = ROOT.TLine(hist.x_min, 1, hist.x_max, 1)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineStyle(ROOT.kDashed)
    line.Draw()
  
  def __setup_canvas(self, canvas):
    if self.backgrounds_included and self.data_included and self.config.show_ratio_plots:
      canvas.Divide(1, 2)
      self.styler.setup_ratio_pad(canvas.GetPad(2))
      self.styler.setup_main_pad_with_ratio(canvas.GetPad(1))
    else:
      self.styler.setup_main_pad_without_ratio(canvas.GetPad(1))
  
  def drawStacks(self):
    if not os.path.exists(self.config.output_path):
      os.makedirs(self.config.output_path)

    for hist in self.config.histograms:
      canvas = TCanvas(hist.getName(), hist.getName(), self.config.canvas_size[0], self.config.canvas_size[1])
      self.__setup_canvas(canvas)
      
      if self.show_ratios:
        canvas.cd(2)
        
        ratio_hist = self.__getRatioStack(hist)
        if ratio_hist:
          ratio_hist.Draw("p")
        self.styler.setupFigure(ratio_hist, hist, is_ratio=True)
        self.__draw_line_at_one(hist)
      
      canvas.cd(1)
      gPad.SetLogy(hist.log_y)
      
      if self.backgrounds_included:
        
        n_entries = 0
        for h in self.stacks[SampleType.background][hist.getName()].GetHists():
          n_entries += h.GetEntries()
        
        self.stacks[SampleType.background][hist.getName()].Draw("hist")
        self.styler.setupFigure(self.stacks[SampleType.background][hist.getName()], hist)
        
        background_uncertainty_hist = self.__getBackgroundUncertaintyHist(hist)
        if background_uncertainty_hist is not None:
          background_uncertainty_hist.Draw("same e2")
        
          if self.show_ratios:
            canvas.cd(2)
            ratio_uncertainty = background_uncertainty_hist.Clone("ratio_uncertainty_"+hist.getName())
            
            ratio_uncertainty.Divide(ratio_uncertainty)
            ratio_uncertainty.Draw("same e2")
            canvas.cd(1)
        
        self.stacks[SampleType.signal][hist.getName()].Draw("nostack same e")
      elif self.signals_included:
        self.stacks[SampleType.signal][hist.getName()].Draw("nostack hist e")
        self.styler.setupFigure(self.stacks[SampleType.signal][hist.getName()], hist)

      if self.data_included:
        
        if self.backgrounds_included or self.signals_included:  
          self.stacks[SampleType.data][hist.getName()].Draw("nostack same pe")
        else:
          self.stacks[SampleType.data][hist.getName()].Draw("nostack hist")
          self.styler.setupFigure(self.stacks[SampleType.data][hist.getName()], hist)

      for sample_type in self.legends.keys():
        if hist.getName() not in self.legends[sample_type].keys():
          continue
        self.legends[sample_type][hist.getName()].Draw()
      
      canvas.Update()
      canvas.SaveAs(self.config.output_path+"/"+hist.getName()+".pdf")
  
  def drawHists2D(self):
    if not os.path.exists(self.config.output_path):
      os.makedirs(self.config.output_path)

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
    
    if hasattr(self.config, "background_uncertainty"):
      color = self.config.background_uncertainty_color
    else:
      color = ROOT.kBlack
    
    if hasattr(self.config, "background_uncertainty_alpha"):
      alpha = self.config.background_uncertainty_alpha
    else:
      alpha = 0.3
    
    if hasattr(self.config, "background_uncertainty_style"):
      style = self.config.background_uncertainty_style
    else:
      style = 3244
    
    uncertainty_hist.SetFillColorAlpha(color, alpha)
    uncertainty_hist.SetLineColor(color)
    uncertainty_hist.SetFillStyle(style)
    
    return uncertainty_hist
  
  def __getStackDict(self, sample_type):
    hists_dict = {}
    
    for name in self.hist_names:
      title = name + sample_type.name
      hists_dict[name] = ROOT.THStack(title, title)

    return hists_dict

  def __getLegendDicts(self, sample_type):
    legends_dict = {}
    
    for name in self.hist_names:
      if sample_type in self.config.legends.keys():
        legends_dict[name] = self.config.legends[sample_type].getRootLegend()

    return legends_dict
  