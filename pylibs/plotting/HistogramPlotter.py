from ROOT import TCanvas, TObject, gPad, gStyle, THStack
import ROOT
import os
import os.path

from Sample import SampleType
from HistogramNormalizer import HistogramNormalizer


class HistogramPlotter:
  def __init__(self, config):
    gStyle.SetOptStat(0)
    
    self.config = config
    
    self.normalizer = HistogramNormalizer(config)
    
    self.hist_names = [hist.name for hist in self.config.histograms]
    
    self.legends = {sample_type: self.__getLegendDicts(sample_type) for sample_type in SampleType}
    self.stacks = {sample_type: self.__getStackDict(sample_type) for sample_type in SampleType}
    self.hists2d = {sample_type: {} for sample_type in SampleType}
    
    self.data_included = any(sample.type == SampleType.data for sample in self.config.samples)
    self.backgrounds_included = any(sample.type == SampleType.background for sample in self.config.samples)
    self.signals_included = any(sample.type == SampleType.signal for sample in self.config.samples)
    
    self.initial_background_weight = None
    
    self.data_hists = {}
    
  
  def addHistsToStacks(self, input_file, sample):
    
    for hist in self.config.histograms:
      hist.load(input_file)
      
      if not hist.isGood():
        continue

      if sample.type == SampleType.data:
        self.data_hists[hist.name] = hist.hist

      data_hist = None
      if hist.name in self.data_hists:
        data_hist = self.data_hists[hist.name]

      self.normalizer.normalize(hist, sample, data_hist)
      hist.setup(sample)
      
      self.stacks[sample.type][hist.name].Add(hist.hist)
      self.legends[sample.type][hist.name].AddEntry(hist.hist, sample.legend_description, self.config.legends[sample.type].options)  
  
  def addHists2D(self, input_file, sample):
    for hist in self.config.histograms2D:
      hist.load(input_file)
      
      if not hist.isGood():
        continue
      
      hist.setup()
      self.hists2d[sample.type][hist.name] = hist.hist
  
  def drawStacks(self):
    if not os.path.exists(self.config.output_path):
      os.makedirs(self.config.output_path)

    for hist in self.config.histograms:
      canvas = TCanvas(hist.name, hist.name, self.config.canvas_size[0], self.config.canvas_size[1])
      
      if self.backgrounds_included and self.data_included and self.config.show_ratio_plots:
        
        canvas.Divide(1, 2)
        canvas.cd(2)
        gPad.SetPad(0, 0, 1, 0.3)
        gPad.SetTopMargin(0)
        gPad.SetBottomMargin(0.3)
        gPad.SetLogy(False)
        
        ratio_hist = self.__getRatioStack(hist)
        if ratio_hist:
          ratio_hist.Draw("p")
        self.__setupFigure(ratio_hist, hist, is_ratio=True)
        
        # draw a line at 1
        line = ROOT.TLine(hist.x_min, 1, hist.x_max, 1)
        line.SetLineColor(ROOT.kBlack)
        line.SetLineStyle(ROOT.kDashed)
        line.Draw()
        
        canvas.cd(1)
        gPad.SetPad(0, 0.3, 1, 1)
        gPad.SetBottomMargin(0)
        gPad.SetLogy(hist.log_y)
      else:
        canvas.cd()
      
      gPad.SetLogy(hist.log_y)
      
      if self.backgrounds_included:
        
        n_entries = 0
        for h in self.stacks[SampleType.background][hist.name].GetHists():
          n_entries += h.GetEntries()
        
        print(f"Plotting hist: {hist.name} with {n_entries} entries")
        
        self.stacks[SampleType.background][hist.name].Draw("hist")
        self.__setupFigure(self.stacks[SampleType.background][hist.name], hist)
        
        background_uncertainty_hist = self.__getBackgroundUncertaintyHist(hist)
        if background_uncertainty_hist is not None:
          background_uncertainty_hist.Draw("same e2")
        
          canvas.cd(2)
          ratio_uncertainty = background_uncertainty_hist.Clone("ratio_uncertainty_"+hist.name)
          
          ratio_uncertainty.Divide(ratio_uncertainty)
          ratio_uncertainty.SetFillColorAlpha(self.config.background_uncertainty_color, 
                                              self.config.background_uncertainty_alpha)
          ratio_uncertainty.SetLineColor(self.config.background_uncertainty_color)
          ratio_uncertainty.SetFillStyle(self.config.background_uncertainty_style)
          ratio_uncertainty.Draw("same e2")
          canvas.cd(1)
        
        self.stacks[SampleType.signal][hist.name].Draw("nostack same e")
      elif self.signals_included:
        self.stacks[SampleType.signal][hist.name].Draw("nostack hist e")
        self.__setupFigure(self.stacks[SampleType.signal][hist.name], hist)

      if self.data_included:
        
        if self.backgrounds_included or self.signals_included:  
          self.stacks[SampleType.data][hist.name].Draw("nostack same pe")
        else:
          self.stacks[SampleType.data][hist.name].Draw("nostack hist")
          self.__setupFigure(self.stacks[SampleType.data][hist.name], hist)

      for sample_type in SampleType:
        self.legends[sample_type][hist.name].Draw()
      
      canvas.Update()
      canvas.SaveAs(self.config.output_path+"/"+hist.name+".pdf")
  
  def drawHists2D(self):
    if not os.path.exists(self.config.output_path):
      os.makedirs(self.config.output_path)

    for hist in self.config.histograms2D:
      for sample in self.config.samples:
        title = hist.name + "_" + sample.name
        canvas = TCanvas(title, title, self.config.canvas_size[0], self.config.canvas_size[1])  
        canvas.cd()
      
        self.hists2d[sample.type][hist.name].Draw("colz")
        self.__setupFigure2D(self.hists2d[sample.type][hist.name], hist)
      
        canvas.Update()
        canvas.SaveAs(self.config.output_path+"/"+title+".pdf")
  
  def __getRatioStack(self, hist):
    
    try:
      data_hist = self.stacks[SampleType.data][hist.name].GetHists()[0]
    except:
      return None
    ratio_hist = data_hist.Clone("ratio_"+hist.name)
    
    backgrounds_sum = ROOT.TH1D("backgrounds_sum_"+hist.name, "backgrounds_sum_"+hist.name,
                                data_hist.GetNbinsX(),
                                data_hist.GetXaxis().GetBinLowEdge(1), 
                                data_hist.GetXaxis().GetBinUpEdge(data_hist.GetNbinsX()))
    
    for background_hist in self.stacks[SampleType.background][hist.name].GetHists():  
      backgrounds_sum.Add(background_hist)
    
    ratio_hist.Divide(backgrounds_sum)
    
    ratio_stack = THStack("ratio_stack_"+hist.name, "ratio_stack_"+hist.name)
    ratio_stack.Add(ratio_hist)
    
    return ratio_stack
  
  def __getBackgroundUncertaintyHist(self, hist):
    try:
      background_hist = self.stacks[SampleType.background][hist.name].GetHists()[0]
    except:
      return None
    
    uncertainty_hist = ROOT.TH1D("backgrounds_unc_"+hist.name, "backgrounds_unc_"+hist.name,
                                  background_hist.GetNbinsX(),
                                  background_hist.GetXaxis().GetBinLowEdge(1), 
                                  background_hist.GetXaxis().GetBinUpEdge(background_hist.GetNbinsX()))
    
      
    for background_hist in self.stacks[SampleType.background][hist.name].GetHists():  
      uncertainty_hist.Add(background_hist)
    
    uncertainty_hist.SetFillColorAlpha(self.config.background_uncertainty_color,
                                       self.config.background_uncertainty_alpha)
    uncertainty_hist.SetLineColor(self.config.background_uncertainty_color)
    uncertainty_hist.SetFillStyle(self.config.background_uncertainty_style)
    
    return uncertainty_hist
  
  def __getStackDict(self, sample_type):
    hists_dict = {}
    
    for hist_name in self.hist_names:
      title = hist_name + sample_type.name
      hists_dict[hist_name] = ROOT.THStack(title, title)

    return hists_dict

  def __getLegendDicts(self, sample_type):
    legends_dict = {}
    
    for hist_name in self.hist_names:
      if sample_type in self.config.legends.keys():
        legends_dict[hist_name] = self.config.legends[sample_type].getRootLegend()

    return legends_dict

  def __setupFigure(self, stack, hist, is_ratio=False):
    if stack is None or type(stack) is TObject:
      return

    if is_ratio:
      stack.SetMinimum(0.8)
      stack.SetMaximum(1.2)
    else:
      if (hist.y_min > 0):
        stack.SetMinimum(hist.y_min)
      if (hist.y_max > 0):
        stack.SetMaximum(hist.y_max)
      
    try:
      stack.SetTitle("" if is_ratio else hist.title)
      stack.GetXaxis().SetLimits(hist.x_min, hist.x_max)
      stack.GetXaxis().SetTitle(hist.x_label)
      stack.GetXaxis().SetTitleSize(0.12 if is_ratio else 0.06)
      stack.GetXaxis().SetTitleOffset(1.0 if is_ratio else 1.0)
      stack.GetXaxis().SetLabelSize(0.08 if is_ratio else 0.06)
      
      stack.GetYaxis().SetTitle("Data/MC" if is_ratio else hist.y_label)
      stack.GetYaxis().SetTitleSize(0.09 if is_ratio else 0.06)
      stack.GetYaxis().SetTitleOffset(0.4 if is_ratio else 1.2)
      stack.GetYaxis().CenterTitle()
      stack.GetYaxis().SetLabelSize(0.06)
      stack.GetYaxis().SetNdivisions(505)
      
      if not is_ratio:
        gPad.SetLeftMargin(0.15)
        gPad.SetBottomMargin(0.15)
    except:
      print("Couldn't set axes limits")
      return

  def __setupFigure2D(self, plot, hist):
    if plot is None or type(plot) is TObject:
      return

    if (hist.y_min > 0):
      plot.SetMinimum(hist.y_min)
    if (hist.y_max > 0):
      plot.SetMaximum(hist.y_max)
      
    if (hist.z_min > 0):
      plot.SetMinimum(hist.z_min)
    if (hist.z_max > 0):
      plot.SetMaximum(hist.z_max)
    
    try:
      plot.SetTitle(hist.title)
      plot.GetXaxis().SetRangeUser(hist.x_min, hist.x_max)
      plot.GetXaxis().SetTitle(hist.x_label)
      plot.GetXaxis().SetTitleSize(0.06)
      plot.GetXaxis().SetTitleOffset(1.0)
      plot.GetXaxis().SetLabelSize(0.06)
      
      plot.GetYaxis().SetRangeUser(hist.y_min, hist.y_max)
      plot.GetYaxis().SetTitle(hist.y_label)
      plot.GetYaxis().SetTitleSize(0.06)
      plot.GetYaxis().SetTitleOffset(1.2)
      plot.GetYaxis().CenterTitle()
      plot.GetYaxis().SetLabelSize(0.06)
      plot.GetYaxis().SetNdivisions(505)
      
      plot.GetZaxis().SetTitle(hist.z_label)
      plot.GetZaxis().SetTitleSize(0.06)
      plot.GetZaxis().SetTitleOffset(0.8)
      plot.GetZaxis().CenterTitle()
      plot.GetZaxis().SetLabelSize(0.06)
      plot.GetZaxis().SetNdivisions(505)

      gPad.SetLeftMargin(0.15)
      gPad.SetBottomMargin(0.15)
      gPad.SetRightMargin(0.20)
    except:
      print("Couldn't set axes limits")
      return
