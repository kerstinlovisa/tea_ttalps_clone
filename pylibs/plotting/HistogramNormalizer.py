from enum import Enum
from ROOT import TFile
from Sample import SampleType

class NormalizationType(Enum):
  to_one = 0 # normalize all histograms to 1
  to_background = 1 # normalize background with cross section and luminosity, normalize signal and data to background

class HistogramNormalizer:
  
  def __init__(self, config):
    self.config = config
    self.__setBackgroundEntries()
    
  def normalize(self, hist, sample):
    lumi = self.config.luminosity
    
    if hist.norm_type == NormalizationType.to_one:
      if sample.type == SampleType.background:
        hist.hist.Scale(1./self.total_background)
      else:
        hist.hist.Scale(1./hist.Integral())
        
    elif hist.norm_type == NormalizationType.to_background:
      
      if sample.type == SampleType.background:
        hist.hist.Scale(lumi*sample.cross_section/self.background_initial_sum_weights[sample.name])
      
      elif sample.type == SampleType.signal:
        hist.hist.Scale(self.total_background/self.signal_final_sum_weights[sample.name])
      
      elif sample.type == SampleType.data:
        hist.hist.Scale(self.total_background/self.data_final_entries[sample.name])
  
  def __setBackgroundEntries(self):
    
    self.signal_final_sum_weights = {}
    self.data_final_entries = {}
    self.background_initial_sum_weights = {}
    self.total_background = 0
    
    for sample in self.config.samples:
      file = TFile.Open(sample.file_path, "READ")

      initial_weight_sum = file.Get("cutFlow").GetBinContent(1)
      final_weight_sum = file.Get("cutFlow").GetBinContent(file.Get("cutFlow").GetNbinsX())
      efficiency = final_weight_sum/initial_weight_sum
      
      if sample.type == SampleType.background:
        self.total_background += sample.cross_section * self.config.luminosity * efficiency
        self.background_initial_sum_weights[sample.name] = initial_weight_sum
        
      elif sample.type == SampleType.signal:
        self.signal_final_sum_weights[sample.name] = final_weight_sum
        
      elif sample.type == SampleType.data:
        self.data_final_entries[sample.name] = final_weight_sum
