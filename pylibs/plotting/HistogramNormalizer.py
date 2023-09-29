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
        hist.hist.Scale(lumi*sample.cross_section/self.total_backgrounds_integral)
      else:
        hist.hist.Scale(1./hist.Integral())
    elif hist.norm_type == NormalizationType.to_background:
      if sample.type == SampleType.background:
        hist.hist.Scale(lumi*sample.cross_section/self.total_backgrounds_initial_weight)
      else:
        hist.hist.Scale(self.total_backgrounds_integral/hist.hist.Integral())
  
  def __setBackgroundEntries(self):
    
    self.total_backgrounds_entries = 0
    self.total_backgrounds_integral = 0
    self.total_backgrounds_cross_section = 0
    self.total_backgrounds_initial_weight = 0
    
    for sample in self.config.samples:
      if sample.type != SampleType.background:
        continue
      
      file = TFile.Open(sample.file_path, "READ")

      hist_name = next(iter(self.config.histograms)).name
      hist = file.Get(hist_name) 

      initial_weight = file.Get("cutFlow").GetBinContent(1)

      self.total_backgrounds_entries += hist.Integral()
      self.total_backgrounds_integral += hist.Integral() * self.config.luminosity * sample.cross_section / initial_weight
      self.total_backgrounds_cross_section += sample.cross_section
      self.total_backgrounds_initial_weight += initial_weight
