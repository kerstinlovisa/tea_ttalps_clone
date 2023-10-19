import ROOT
from ROOT import TColor
from Sample import Sample, SampleType
from Legend import Legend
from Histogram import Histogram, Histogram2D
from HistogramNormalizer import NormalizationType

base_path = "../samples/"
skim = ""

output_path = "../plots"

luminosity = 63670. # pb^-1 (2018)

# data&signals must be listed after backgrounds for now

samples = (
  Sample(
    name="DY", 
    file_path=f"{base_path}/histograms/background_dy.root", 
    type=SampleType.background,
    cross_section=0.4, 
    line_alpha=0.0,
    fill_color=41,
    fill_alpha=0.7,
    marker_size=0.0,
    legend_description="DY"
  ),
  Sample(
    name="tt", 
    file_path=f"{base_path}/histograms/background_tt.root", 
    type=SampleType.background,
    cross_section=0.4, 
    line_alpha=0.0,
    fill_color=42,
    fill_alpha=0.7,
    marker_size=0.0,
    legend_description="tt"
  ),
  Sample(
    name="ttZ", 
    file_path=f"{base_path}/histograms/signal_ttz.root", 
    type=SampleType.signal,
    cross_section=1, 
    line_color=TColor.GetColor(230, 159, 0), 
    line_style=ROOT.kSolid,
    fill_alpha=0.0,
    marker_size=0.0,
    legend_description="ttZ"
  ),
  Sample(
    name="data", 
    file_path=f"{base_path}/histograms/data.root", 
    type=SampleType.data,
    cross_section=1, 
    line_color=ROOT.kBlack,
    line_style=ROOT.kSolid,
    marker_style=20,
    marker_size=1.0,
    marker_color=ROOT.kBlack,
    fill_alpha=0.0,
    legend_description="data"
  ),
)

y_label = "# events (2018)"

histograms = (
#           name                  title logy    norm_type                       rebin xmin   xmax  ymin    ymax,    xlabel                ylabel            suffix
  # Histogram("Event_nMuon"         , "", False , NormalizationType.to_background, 1  ,   0   , 20  , 1e1   , 5e4   , "Number of muons"   , y_label           ),
  Histogram("Event_nMuon"         , "", True  , NormalizationType.to_background, 1  ,   0   , 20  , 1e1   , 1e9   , "Number of muons"   , y_label          , "_log" ),
  Histogram("Muon_pt"             , "", True  , NormalizationType.to_background, 5  ,   0   , 500 , 1e-2  , 1e3   , "p_{T}^{#mu} [GeV]" , y_label           ),
  Histogram("Muon_eta"            , "", True  , NormalizationType.to_background, 10 , -3.5  , 3.5 , 1e0   , 1e3   , "#eta^{#mu}"        , y_label           ),
  Histogram("Event_nGoodLeptons"  , "", True  , NormalizationType.to_background, 1  ,   0   , 30  , 1e0   , 1e9   , "Number of jets"    , y_label           ),
  Histogram("GoodLeptons_pt"      , "", True  , NormalizationType.to_background, 5  ,   0   , 500 , 10    , 1e8   , "p_{T}^{j} [GeV]"   , y_label           ),
  Histogram("GoodLeptons_eta"     , "", True  , NormalizationType.to_background, 10 , -3.5  , 3.5 , 1e0   , 1e10  , "#eta^{j}"          , y_label           ),
  Histogram("cutFlow"             , "", True  , NormalizationType.to_background, 1  ,   0   , 8   , 1e2   , 1e6   , "Selection"         , "#sum genWeight"  ),
)

histograms2D = (
#           name              title                rebin  xmin    xmax       ymin   ymax     zmin zmax xlabel               ylabel                        zlabel
  # Histogram2D("hit_xy",         "hit_xy"          , 1, 1, -15     , 15      , -15   , 15    , 0,  1e5, "x"             , "y"                         , "Counts"),
  # Histogram2D("time_vs_toa",    "time_vs_toa"     , 1, 1, -10     , 100     , -10   , 2000  , 0,  1e3, "Time (ns)"     , "Time of Arrival (ToA)"     , "Counts"),
)

legends = {
  SampleType.signal: Legend(0.15,0.85,0.25,0.89, "l"),
  SampleType.background: Legend(0.7,0.5,0.85,0.85, "f"),
  SampleType.data: Legend(0.15,0.8,0.25,0.85, "pl"),
}

canvas_size = (800, 600)
show_ratio_plots = True
