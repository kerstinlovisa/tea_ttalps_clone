import ROOT
from ROOT import TColor
from Sample import Sample, SampleType
from Legend import Legend
from Histogram import Histogram
from HistogramNormalizer import NormalizationType

base_path = "../samples/"
skim = ""

output_path = "../plots"

luminosity = 63670. # pb^-1 (2018)

# data&signals must be listed after backgrounds for now

samples = (
  Sample(
    name="my_background", 
    file_path=f"{base_path}/backgrounds/nanoAOD_hists.root", 
    type=SampleType.background,
    cross_section=0.4, 
    line_alpha=0.0,
    fill_color=41,
    fill_alpha=0.7,
    marker_size=0.0,
    legend_description="my_background"
  ),
  Sample(
    name="my_signal", 
    file_path=f"{base_path}/signals/nanoAOD_hists.root", 
    type=SampleType.signal,
    cross_section=1, 
    line_color=TColor.GetColor(230, 159, 0), 
    line_style=ROOT.kSolid,
    fill_alpha=0.0,
    marker_size=0.0,
    legend_description="my_signal"
  ),
  Sample(
    name="my_data", 
    file_path=f"{base_path}/data/nanoAOD_hists.root", 
    type=SampleType.data,
    cross_section=1, 
    line_color=ROOT.kBlack,
    line_style=ROOT.kSolid,
    marker_style=20,
    marker_size=1.0,
    marker_color=ROOT.kBlack,
    fill_alpha=0.0,
    legend_description="my_data"
  ),
)

histograms = (
#           name       title              logy  norm_type                       rebin xmin xmax ymin ymax,  xlabel              ylabel
  Histogram("n_muons", "Number of muons", True, NormalizationType.to_background, 1,   0, 20,    1e1, 1e9,   "Number of muons",  "# events (2018)"),
  Histogram("muon_pt", "Muon p_{T}",      True, NormalizationType.to_background, 5,   0, 500,   1e-2, 1e3,   "p_{T}^{#mu} [GeV]","# events (2018)"),
  Histogram("muon_eta","Muon #eta",       True, NormalizationType.to_background, 10, -3.5, 3.5, 1e0, 1e3,  "#eta^{#mu}",       "# events (2018)"),
  Histogram("n_jets",  "Number of jets",  True, NormalizationType.to_background, 1,   0, 30,    1e0, 1e9,   "Number of jets",   "# events (2018)"),
  Histogram("jet_pt",  "Jet p_{T}",       True, NormalizationType.to_background, 5,   0, 500,   10, 1e8,    "p_{T}^{j} [GeV]",  "# events (2018)"),
  Histogram("jet_eta", "Jet #eta",        True, NormalizationType.to_background, 10, -3.5, 3.5, 1e0, 1e10,  "#eta^{j}",         "# events (2018)"),
  Histogram("cutFlow", "cutflow",         True, NormalizationType.to_background, 1,   0, 8,     1e2, 1e6,     "Selection",        "Number of events"),
)

legends = {
  SampleType.signal: Legend(0.15,0.85,0.25,0.89, "l"),
  SampleType.background: Legend(0.7,0.5,0.85,0.85, "f"),
  SampleType.data: Legend(0.15,0.8,0.25,0.85, "pl"),
}

canvas_size = (800, 600)
show_ratio_plots = True
