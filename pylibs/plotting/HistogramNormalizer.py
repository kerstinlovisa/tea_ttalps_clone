from enum import Enum
from ROOT import TFile
from Sample import SampleType

class NormalizationType(Enum):
  to_one = 0 # normalize all histograms to 1
  to_background = 1 # normalize background with cross section and luminosity, normalize signal and data to background
  to_lumi = 3 # normalize signal/background to lumi*crosssection, keep data unchanged
  to_data = 4 # normalize signal/background to data, keep data unchanged

class HistogramNormalizer:
  
  def __init__(self, config):
    self.config = config
    self.__setBackgroundEntries()
  
  def normalize(self, hist, sample, data_hist=None):
    if hist.norm_type == NormalizationType.to_one:
      self.__normalizeToOne(hist, sample)
    elif hist.norm_type == NormalizationType.to_background:
      self.__normalizeToBackground(hist, sample)
    elif hist.norm_type == NormalizationType.to_lumi:
      self.__normalizeToLumi(hist, sample)
    elif hist.norm_type == NormalizationType.to_data:
      self.__normalizeToData(hist, sample, data_hist)
  
  def __normalizeToOne(self, hist, sample):
    if sample.type == SampleType.background:
      hist.hist.Scale(1./self.total_background)
    else:
      hist.hist.Scale(1./hist.Integral())
  
  def __normalizeToBackground(self, hist, sample):
    if sample.type == SampleType.background:
        hist.hist.Scale(self.config.luminosity*sample.cross_section/self.background_initial_sum_weights[sample.name])
    elif sample.type == SampleType.signal:
      hist.hist.Scale(self.total_background/self.signal_final_sum_weights[sample.name])
    elif sample.type == SampleType.data:
      hist.hist.Scale(self.total_background/self.data_final_entries[sample.name])
  
  def __normalizeToLumi(self, hist, sample):
    scale = self.config.luminosity*sample.cross_section
    
    if sample.type == SampleType.background:
      scale /= self.background_initial_sum_weights[sample.name]
    elif sample.type == SampleType.signal:
      scale /= self.signal_final_sum_weights[sample.name]
    elif sample.type == SampleType.data:
      scale = 1
    
    hist.hist.Scale(scale)
  
  def __normalizeToData(self, hist, sample, data_hist):
    if hist.hist.Integral() == 0:
        return  
    
    scale = hist.rebin * data_hist.Integral()/hist.hist.Integral()
    
    if sample.type == SampleType.background:
      scale *= sample.cross_section/self.total_background_cross_section
    elif sample.type == SampleType.data:
      scale = 1
    
    hist.hist.Scale(scale)
  
  def __setBackgroundEntries(self):
    
    self.signal_final_sum_weights = {}
    self.data_final_entries = {}
    self.background_final_sum_weights = {}
    self.background_initial_sum_weights = {}
    self.total_background = 0
    self.total_background_cross_section = 0
    
    for sample in self.config.samples:
      file = TFile.Open(sample.file_path, "READ")

      cut_flow = file.Get("cutFlow")
      initial_weight_sum = cut_flow.GetBinContent(1)
      final_weight_sum = cut_flow.GetBinContent(cut_flow.GetNbinsX())
      
      if initial_weight_sum == 0:
        print(f"Initial sum of weights is zero for sample: {sample.name}. Setting efficeincy to zero.")
        efficiency = 0
      else:
        efficiency = final_weight_sum/initial_weight_sum
      
      if sample.type == SampleType.background:
        print(f"{sample.name}: {sample.cross_section * self.config.luminosity * efficiency:.1e}")
        print(f"{initial_weight_sum=:.1e}")
        
        self.total_background += sample.cross_section * self.config.luminosity * efficiency
        self.background_initial_sum_weights[sample.name] = initial_weight_sum
        self.total_background_cross_section += sample.cross_section
        
        self.background_final_sum_weights[sample.name] = final_weight_sum
        
      elif sample.type == SampleType.signal:
        print(f"{sample.name}: {final_weight_sum}")
        self.signal_final_sum_weights[sample.name] = final_weight_sum
        
      elif sample.type == SampleType.data:
        print(f"{sample.name}: {final_weight_sum}")
        self.data_final_entries[sample.name] = final_weight_sum
