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
    
    self.data_included = any(sample.type == SampleType.data for sample in self.config.samples)
    self.backgrounds_included = any(sample.type == SampleType.background for sample in self.config.samples)
    
    self.initial_background_weight = None
    
  
  def addHistsToStacks(self, input_file, sample):
    
    for hist in self.config.histograms:
      hist.load(input_file)
      
      if not hist.isGood():
        continue

      self.normalizer.normalize(hist, sample)
      hist.setup(sample)
      
      self.stacks[sample.type][hist.name].Add(hist.hist)
      self.legends[sample.type][hist.name].AddEntry(hist.hist, sample.legend_description, self.config.legends[sample.type].options)  
  
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
        self.stacks[SampleType.background][hist.name].Draw("hist")
        self.__setupFigure(self.stacks[SampleType.background][hist.name], hist)
        
        self.stacks[SampleType.signal][hist.name].Draw("nostack same")
      else:
        self.stacks[SampleType.signal][hist.name].Draw("hist nostack")
        self.__setupFigure(self.stacks[SampleType.signal][hist.name], hist)

      if self.data_included:
        self.stacks[SampleType.data][hist.name].Draw("nostack same P")



      for sample_type in SampleType:
        self.legends[sample_type][hist.name].Draw()
      
      canvas.Update()
      canvas.SaveAs(self.config.output_path+"/"+hist.name+".pdf")
  
  def __getRatioStack(self, hist):
    data_hist = self.stacks[SampleType.data][hist.name].GetHists()[0]
    ratio_hist = data_hist.Clone("ratio_"+hist.name)
    
    print(f"{hist.name=}")
    
    print(f"{data_hist.GetNbinsX()*hist.rebin=}")
    print(f"{data_hist.GetXaxis().GetBinLowEdge(1)=}")
    print(f"{data_hist.GetXaxis().GetBinUpEdge(data_hist.GetNbinsX())=}")
    
    backgrounds_sum = ROOT.TH1D("backgrounds_sum_"+hist.name, "backgrounds_sum_"+hist.name,
                                int(data_hist.GetNbinsX()*hist.rebin),
                                data_hist.GetXaxis().GetBinLowEdge(1), 
                                data_hist.GetXaxis().GetBinUpEdge(data_hist.GetNbinsX()))
    
    for background_hist in self.stacks[SampleType.background][hist.name].GetHists():
      backgrounds_sum.Add(background_hist)
    
    ratio_hist.Divide(backgrounds_sum)
    
    ratio_stack = THStack("ratio_stack_"+hist.name, "ratio_stack_"+hist.name)
    ratio_stack.Add(ratio_hist)
    
    return ratio_stack
  
  def __getStackDict(self, sample_type):
    hists_dict = {}
    
    for hist_name in self.hist_names:
      title = hist_name + sample_type.name
      hists_dict[hist_name] = ROOT.THStack(title, title)

    return hists_dict

  def __getLegendDicts(self, sample_type):
    legends_dict = {}
    
    for hist_name in self.hist_names:
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
      stack.GetXaxis().SetTitleSize(0.12)
      stack.GetXaxis().SetTitleOffset(1.0)
      stack.GetXaxis().SetLabelSize(0.08)
      
      stack.GetYaxis().SetTitle("Data/MC" if is_ratio else hist.y_label)
      stack.GetYaxis().SetTitleSize(0.09 if is_ratio else 0.06)
      stack.GetYaxis().SetTitleOffset(0.4 if is_ratio else 0.8)
      stack.GetYaxis().CenterTitle()
      stack.GetYaxis().SetLabelSize(0.06)
      stack.GetYaxis().SetNdivisions(505)
    except:
      print("Couldn't set axes limits")
      return
