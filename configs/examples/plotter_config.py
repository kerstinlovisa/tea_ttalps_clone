import ROOT
from ROOT import TColor
from Sample import Sample

base_path = "../samples/"
skim = ""

output_path = "../plots"

# data&signals must be listed after backgrounds for now

samples = (
  Sample(
    name="my_background", 
    file_path=f"{base_path}/backgrounds/nanoAOD_hists.root", 
    sample_type="background",
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
    sample_type="signal",
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
    sample_type="data",
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


luminosity_2018 = 63670. # pb^-1

legend_types = {
  "signal": "l",
  "background": "f",
  "data": "pl",
}

legend_position = {
  "signal": (0.15,0.85,0.25,0.89),
  "background": (0.7,0.5,0.85,0.85),
  "data": (0.15,0.8,0.25,0.85),
}

# normalization options:
#   norm1: normalize to 1
#   to_background: normalize background with cross section and luminosity, 
#                  normalize signal and data to background

variables = {
# key                    title         logy   norm_type   rebin    xmin     xmax     ymin,  ymax,  xlabel                 ylabel
  "n_muons"   :          ("",          True,   "to_background",   1,       0,       20,      1e1,    1e9,    "Number of muons",    "# events (2018)"  ),
  "muon_pt"   :          ("",          True,   "to_background",   5,       0,       500,     1e2,    1e8,    "p_{T}^{#mu} [GeV]",  "# events (2018)"  ),
  "muon_eta"  :          ("",          True,   "to_background",   10,      -3.5,    3.5,     1e0,    1e10,    "#eta^{#mu}",         "# events (2018)"  ),
  "n_jets"    :          ("",          True,   "to_background",   1,       0,       30,      1e0,   1e9,    "Number of jets",     "# events (2018)"  ),
  "jet_pt"    :          ("",          True,   "to_background",   5,       0,       500,     10,    1e8,    "p_{T}^{j} [GeV]",    "# events (2018)"  ),
  "jet_eta"   :          ("",          True,   "to_background",   10,      -3.5,    3.5,     1e0,    1e10,    "#eta^{j}",           "# events (2018)"  ),
  "cutFlow"   :          ("cutflow",   True,   "to_background",  1,       0,       7,       -1,    -1,    "Selection",          "Number of events"  ),
}

efficiency_plots = {
# key                     from hist  title                  xlabel       ylabel
  "cutFlowEfficiency":   ("cutFlow", "Cutflow efficiency",  "Selection", "Number of events"  ),
}
