import ROOT
from ROOT import TColor

base_path = "../samples/"
skim = ""

input_paths = {
  "signal": f"{base_path}/signals/",
  "background": f"{base_path}/backgrounds/",
  "data": f"{base_path}/collision_data/",
}

output_path = "../plots"

# data&signals must be listed after backgrounds for now
files = {
  #name                  filename     type(signal/background)
  "my_background": ("nanoAOD_hists.root", "background"),
  "my_signal": ("nanoAOD_hists.root", "signal"),
  "my_data": ("nanoAOD_hists.root", "data"),
}

luminosity_2018 = 63670. # pb^-1

cross_sections = {
  #name                   cross section [pb]
  "my_background": 0.4, 
  "my_signal": 1,
  "my_data": 1,
}

lines = {
  #name                   color
  "my_background": [41, ROOT.kSolid],
  "my_signal": [TColor.GetColor(230, 159, 0), ROOT.kSolid],
  "my_data": [ROOT.kBlack, ROOT.kSolid],
} 

legends = {
  #name                   title
  "my_background": "my_background",
  "my_signal":"my_signal",
  "my_data": "my_data",
}

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
