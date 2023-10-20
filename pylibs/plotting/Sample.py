import ROOT
from dataclasses import dataclass
from enum import Enum

# enum class with signal, background, data
class SampleType(Enum):
  signal = 0
  background = 1
  data = 2

@dataclass
class Sample:
  name: str = ""
  file_path: str = ""
  type: SampleType = SampleType.background
  cross_section: float = 1.0
  line_color: int = ROOT.kBlack
  line_style: int = ROOT.kSolid
  line_alpha: float = 1.0
  marker_color: int = ROOT.kBlack
  marker_style: int = 20
  marker_size: float = 1.0
  fill_color: int = ROOT.kGreen
  fill_alpha: float = 0.7
  legend_description: str = ""
  plotting_options: str = ""
