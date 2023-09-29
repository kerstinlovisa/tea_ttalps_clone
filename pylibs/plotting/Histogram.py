from dataclasses import dataclass
from ROOT import TObject

from Sample import SampleType

@dataclass
class Histogram:
  name: str = ""
  title: str = ""
  log_y: bool = False
  norm_type: str = "norm1"
  rebin: int = 1
  x_min: float = 0.0
  x_max: float = 0.0
  y_min: float = 0.0
  y_max: float = 0.0
  x_label: str = ""
  y_label: str = ""
  
  def load(self, input_file):
    self.hist = input_file.Get(self.name)
    
  def isGood(self):
    if not self.__checkHist():
        print(f"Couldn't find hist or it is empty: {self.name}")
        return False
    return True
    
  def setup(self, sample):
    self.hist.SetLineStyle(sample.line_style)
    self.hist.SetLineColor(sample.line_color)
    self.hist.SetMarkerStyle(sample.marker_style)
    self.hist.SetMarkerSize(sample.marker_size)
    self.hist.SetMarkerColor(sample.marker_color)
    self.hist.SetLineColorAlpha(sample.line_color, sample.line_alpha)
    self.hist.SetFillColorAlpha(sample.fill_color, sample.fill_alpha)
    self.hist.Rebin(self.rebin)
    self.hist.Scale(1./self.rebin)
    self.hist.Sumw2(False)
  
  def __checkHist(self):
    if self.hist is None or type(self.hist) is TObject:
      return False
    if self.hist.GetEntries() == 0:
      return False
    return True