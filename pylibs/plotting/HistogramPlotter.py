from ROOT import TFile, TCanvas, TObject
import ROOT
import os
import os.path

from Sample import SampleType
from HistogramNormalizer import HistogramNormalizer


class HistogramPlotter:
  def __init__(self, config):
    self.config = config
    
    self.normalizer = HistogramNormalizer(config)
    
    self.hist_names = [hist.name for hist in self.config.histograms]
    
    self.legends = {sample_type: self.__getLegendDicts(sample_type) for sample_type in SampleType}
    self.hists = {sample_type: self.__getStackDict(sample_type) for sample_type in SampleType}
    
    self.data_included = any(sample.type == SampleType.data for sample in self.config.samples)
    self.backgrounds_included = any(sample.type == SampleType.background for sample in self.config.samples)
    
  
  def addHistsToStacks(self, input_file, sample):
    for hist in self.config.histograms:
      hist.load(input_file)
      
      if not hist.isGood():
        continue

      self.normalizer.normalize(hist, sample)
      hist.setup(sample)
      
      self.hists[sample.type][hist.name].Add(hist.hist)
      self.legends[sample.type][hist.name].AddEntry(hist.hist, sample.legend_description, self.config.legends[sample.type].options)  
  
  def drawStacks(self):
    if not os.path.exists(self.config.output_path):
      os.makedirs(self.config.output_path)

    for hist in self.config.histograms:
      canvas = TCanvas(hist.name, hist.name, self.config.canvas_size[0], self.config.canvas_size[1])
      canvas.cd()
      canvas.SetLogy(hist.log_y)
      
      if self.backgrounds_included:
        self.hists[SampleType.background][hist.name].Draw("hist")
        self.__setupFigure(self.hists[SampleType.background][hist.name], hist)
        
        self.hists[SampleType.signal][hist.name].Draw("nostack same")
      else:
        self.hists[SampleType.signal][hist.name].Draw("hist nostack")
        self.__setupFigure(self.hists[SampleType.signal][hist.name], hist)

      if self.data_included:
        self.hists[SampleType.data][hist.name].Draw("nostack same P")

      for sample_type in SampleType:
        self.legends[sample_type][hist.name].Draw()
      
      canvas.Update()
      canvas.SaveAs(self.config.output_path+"/"+hist.name+".pdf")
  
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

  def __setupFigure(self, stack, hist):
    if stack is None or type(stack) is TObject:
      return

    if (hist.y_min > 0):
      stack.SetMinimum(hist.y_min)
    if (hist.y_max > 0):
      stack.SetMaximum(hist.y_max)
      
    try:
      stack.GetXaxis().SetLimits(hist.x_min, hist.x_max)
      stack.GetXaxis().SetTitle(hist.x_label)
      stack.GetYaxis().SetTitle(hist.y_label)
      stack.SetTitle(hist.title)
    except:
      print("Couldn't set axes limits")
      return
