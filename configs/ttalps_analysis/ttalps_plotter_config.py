import ROOT
from ROOT import TColor
from Sample import Sample, SampleType
from Legend import Legend
from Histogram import Histogram
from HistogramNormalizer import NormalizationType

# base_path = "/nfs/dust/cms/user/jniedzie/ttalps_cms/"
base_path = "/Users/jeremi/Documents/Physics/DESY/ttalps_cms.nosync/data/"
output_path = "../plots"

# skim = ""
skim = "skimmed_looseSemileptonic"
# skim = "skimmed_signalLike"
# skim = "skimmed_ttbarLike"

luminosity = 63670. # pb^-1

legends = {
  SampleType.signal: Legend(0.15,0.85,0.25,0.89, "l"),
  SampleType.background: Legend(0.7,0.5,0.85,0.85, "f"),
  SampleType.data: Legend(0.15,0.8,0.25,0.85, "pl"),
}

canvas_size = (800, 600)
show_ratio_plots = True

color_palette = [
  TColor.GetColor(230, 159, 0),
  TColor.GetColor(86, 180, 233),
  TColor.GetColor(0, 158, 115),
  TColor.GetColor(0, 114, 178),
  TColor.GetColor(213, 94, 0),
]


histograms = (
#           name       title                                    logy  norm_type                       rebin xmin xmax ymin ymax,  xlabel              ylabel
  Histogram("n_muons", "Number of muons",                       True, NormalizationType.to_background, 1,   0, 20,    1e1, 1e9,   "Number of muons",                    "# events (2018)"),
  Histogram("muon_pt", "Muon p_{T}",                            True, NormalizationType.to_background, 5,   0, 500,   1e-2, 1e6,   "p_{T}^{#mu} [GeV]",                 "# events (2018)"),
  Histogram("muon_leading_pt", "Leading muon p_{T}",            True, NormalizationType.to_background, 5,   0, 500,   1e-2, 1e6,   "Leading p_{T}^{#mu} [GeV]",         "# events (2018)"),
  Histogram("muon_subleading_pt", "All subleading muons p_{T}", True, NormalizationType.to_background, 5,   0, 500,   1e-2, 1e6,   "All subleading p_{T}^{#mu} [GeV]",  "# events (2018)"),
  Histogram("muon_eta","Muon #eta",                             True, NormalizationType.to_background, 5,-3.5, 3.5,    1e0, 1e6,  "#eta^{#mu}",                         "# events (2018)"),
  Histogram("muon_dxy","Muon d_{xy}",                           True, NormalizationType.to_background, 2,  -10, 10,   1e-2, 1e6,  "d_{xy}^{#mu}",                       "# events (2018)"),
  Histogram("muon_dz", "Muon d_{z}",                            True, NormalizationType.to_background, 2,  -10, 10,   1e-2, 1e6,  "d_{z}^{#mu}",                        "# events (2018)"),
  
  Histogram("n_good_muons", "Number of muons",                       True, NormalizationType.to_background, 1,   0, 20,    1e1, 1e9,   "Number of muons",                    "# events (2018)"),
  Histogram("good_muon_pt", "Muon p_{T}",                            True, NormalizationType.to_background, 5,   0, 500,   1e-2, 1e6,   "p_{T}^{#mu} [GeV]",                 "# events (2018)"),
  Histogram("good_muon_leading_pt", "Leading muon p_{T}",            True, NormalizationType.to_background, 5,   0, 500,   1e-2, 1e6,   "Leading p_{T}^{#mu} [GeV]",         "# events (2018)"),
  Histogram("good_muon_subleading_pt", "All subleading muons p_{T}", True, NormalizationType.to_background, 5,   0, 500,   1e-2, 1e6,   "All subleading p_{T}^{#mu} [GeV]",  "# events (2018)"),
  Histogram("good_muon_eta","Muon #eta",                             True, NormalizationType.to_background, 5,-3.5, 3.5,    1e0, 1e6,  "#eta^{#mu}",                         "# events (2018)"),
  Histogram("good_muon_dxy","Muon d_{xy}",                           True, NormalizationType.to_background, 2,  -10, 10,   1e-2, 1e6,  "d_{xy}^{#mu}",                       "# events (2018)"),
  Histogram("good_muon_dz", "Muon d_{z}",                            True, NormalizationType.to_background, 2,  -10, 10,   1e-2, 1e6,  "d_{z}^{#mu}",                        "# events (2018)"),
  
  Histogram("n_electrons",  "Number of electrons",                   True, NormalizationType.to_background, 1,   0, 10,    1e1, 1e9,   "Number of electrons", "# events (2018)"),
  Histogram("electron_pt",  "Electron p_{T}",                        True, NormalizationType.to_background, 5,   0, 500,   1e-2, 1e6,   "p_{T}^{e} [GeV]",  "# events (2018)"),
  Histogram("electron_leading_pt",  "Leading electron p_{T}",        True, NormalizationType.to_background, 5,   0, 200,   1e-2, 1e6,   "Leading p_{T}^{e} [GeV]",  "# events (2018)"),
  Histogram("electron_subleading_pt","All subleading electron p_{T}",True, NormalizationType.to_background, 5,   0, 200,   1e-2, 1e6,   "All subleading p_{T}^{e} [GeV]",  "# events (2018)"),
  Histogram("electron_eta", "Electron #eta",                         True, NormalizationType.to_background, 10, -3.5, 3.5, 1e-2,  1e6,  "#eta^{e}",         "# events (2018)"),
  Histogram("electron_dxy", "Electron d_{xy}",                       True, NormalizationType.to_background, 2,   -10, 10,  1e-2, 1e6,  "d_{xy}^{e}",       "# events (2018)"),
  Histogram("electron_dz",  "Electron d_{z}",                        True, NormalizationType.to_background, 2,   -10, 10,  1e-2, 1e6,  "d_{z}^{e}",        "# events (2018)"),
  
  Histogram("n_good_electrons",  "Number of electrons",                   True, NormalizationType.to_background, 1,   0, 10,    1e1, 1e9,   "Number of electrons", "# events (2018)"),
  Histogram("good_electron_pt",  "Electron p_{T}",                        True, NormalizationType.to_background, 5,   0, 500,   1e-2, 1e6,   "p_{T}^{e} [GeV]",  "# events (2018)"),
  Histogram("good_electron_leading_pt",  "Leading electron p_{T}",        True, NormalizationType.to_background, 5,   0, 200,   1e-2, 1e6,   "Leading p_{T}^{e} [GeV]",  "# events (2018)"),
  Histogram("good_electron_subleading_pt","All subleading electron p_{T}",True, NormalizationType.to_background, 5,   0, 200,   1e-2, 1e6,   "All subleading p_{T}^{e} [GeV]",  "# events (2018)"),
  Histogram("good_electron_eta", "Electron #eta",                         True, NormalizationType.to_background, 10, -3.5, 3.5, 1e-2,  1e6,  "#eta^{e}",         "# events (2018)"),
  Histogram("good_electron_dxy", "Electron d_{xy}",                       True, NormalizationType.to_background, 2,   -10, 10,  1e-2, 1e6,  "d_{xy}^{e}",       "# events (2018)"),
  Histogram("good_electron_dz",  "Electron d_{z}",                        True, NormalizationType.to_background, 2,   -10, 10,  1e-2, 1e6,  "d_{z}^{e}",        "# events (2018)"),
  
  Histogram("n_jets",  "Number of jets",                        True, NormalizationType.to_background, 1,   0, 30,    1e0, 1e9,   "Number of jets",   "# events (2018)"),
  Histogram("jet_pt",  "Jet p_{T}",                             True, NormalizationType.to_background, 5,   0, 500,   10, 1e8,    "p_{T}^{j} [GeV]",  "# events (2018)"),
  Histogram("jet_eta", "Jet #eta",                              True, NormalizationType.to_background, 10, -3.5, 3.5, 1e0, 1e10,  "#eta^{j}",         "# events (2018)"),
  Histogram("jet_btagDeepB", "Jet btagDeepB",                   True, NormalizationType.to_background, 2,  -1, 1,     1e0, 1e7,  "jet btagDeepB",    "# events (2018)"),
  
  Histogram("n_good_jets",  "Number of jets",                        True, NormalizationType.to_background, 1,   0, 30,    1e0, 1e9,   "Number of jets",   "# events (2018)"),
  Histogram("good_jet_pt",  "Jet p_{T}",                             True, NormalizationType.to_background, 5,   0, 500,   10, 1e8,    "p_{T}^{j} [GeV]",  "# events (2018)"),
  Histogram("good_jet_eta", "Jet #eta",                              True, NormalizationType.to_background, 10, -3.5, 3.5, 1e0, 1e10,  "#eta^{j}",         "# events (2018)"),
  Histogram("good_jet_btagDeepB", "Jet btagDeepB",                   True, NormalizationType.to_background, 2,  -1, 1,     1e0, 1e7,  "jet btagDeepB",    "# events (2018)"),
  
  Histogram("cutFlow", "cutflow",                               True, NormalizationType.to_background, 1,   0, 7,     1e2, 1e10,     "Selection",        "Number of events"),
  Histogram("norm_check", "Norm check",                         True, NormalizationType.to_background, 1,  0, 1,      1e-2, 1e7,  "norm check",    "# events (2018)"),
)

weightsBranchName = "weight"

# data&signals must be listed after backgrounds for now
samples = (
  Sample(
    name="ttZJets",
    file_path=f"{base_path}/backgrounds/ttZJets/{skim}/EB2F627D-0570-7C4C-A561-C29B6E4F123A_hists.root",
    type=SampleType.background,
    cross_section=0.4611,
    line_alpha=0,
    fill_color=41,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttZJets",
  ),
  # Sample(
  #   name="ttHToMuMu",
  #   file_path=f"{base_path}/backgrounds/ttHToMuMu/{skim}/D41A5AFC-EC31-A64F-9E87-6F1C22ED6DCB_hists.root",
  #   type=SampleType.background,
  #   cross_section=0.5269,
  #   line_alpha=0,
  #   fill_color=50,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="ttHToMuMu",
  # ),
  Sample(
    name="ttWJets",
    file_path=f"{base_path}/backgrounds/ttWJets/{skim}/5B123882-8484-1B47-9A07-57F8F526F6EF_hists.root",
    type=SampleType.background,
    cross_section=0.5407,
    line_alpha=0,
    fill_color=ROOT.kMagenta,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttWJets",
  ),
  # Sample(
  #   name="ST_tW_top",
  #   file_path=f"{base_path}/backgrounds/ST_tW_top/{skim}/776A38DC-FF27-6F4E-9B16-C55B696BAA92_hists.root",
  #   type=SampleType.background,
  #   cross_section=32.45,
  #   line_alpha=0,
  #   fill_color=38,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="ST_tW_top",
  # ),
  # Sample(
  #   name="ST_tW_antitop",
  #   file_path=f"{base_path}/backgrounds/ST_tW_antitop/{skim}/09B1D3CA-5FCC-0A48-BFA6-E1759D5D7D02_hists.root",
  #   type=SampleType.background,
  #   cross_section=32.51,
  #   line_alpha=0,
  #   fill_color=30,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="ST_tW_antitop",
  # ),
  Sample(
    name="TTbar_inclusive",
    file_path=f"{base_path}/backgrounds/TTbar_inclusive/{skim}/FCA55055-C8F3-C44B-8DCC-6DCBC0B8B992_hists.root",
    type=SampleType.background,
    cross_section=494.8, # that's for 14 TeV, not sure where to find the correct one...
    line_alpha=0,
    fill_color=33,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="TTbar_inclusive",
  ),
  Sample(
    name="tta_mAlp-0p35GeV",
    file_path=f"{base_path}/signals/tta_mAlp-0p35GeV/{skim}/tta_mAlp-0p35GeV_nEvents-100000_hists.root",
    type=SampleType.signal,
    cross_section=1,
    line_alpha=1,
    line_color=ROOT.kRed,
    fill_color=ROOT.kWhite,
    fill_alpha=0,
    marker_size=0,
    legend_description="tta_mAlp-0p35GeV",
  ),
  Sample(
    name="SingleMuon2018",
    file_path=f"{base_path}/collision_data/SingleMuon2018/{skim}/36ED9511-D46A-0C4F-A485-C2DF1C874906_hists.root",
    type=SampleType.data,
    cross_section=1,
    line_alpha=0,
    fill_alpha=0,
    marker_size=1,
    marker_style=20,
    marker_color=ROOT.kBlack,
    legend_description="SingleMuon2018",
  ),
)


# TODO: these are not perfect, verify them!
  # "QCD_Pt_30to50": 106800000.0,
  # "QCD_Pt_50to80": 15720000.0,
  # "QCD_Pt_80to120": 2363000.0,
  # "QCD_Pt_120to170": 407600.0,
  # "QCD_Pt_170to300": 104000.0,
  # "QCD_Pt_300to470": 6806.0,
  # "QCD_Pt_470to600": 552.0,
  # "QCD_Pt_600to800": 154.6,
  # "QCD_Pt_800to1000": 26.15,
  # "QCD_Pt_1000to1400": 7.501,
  # "QCD_Pt_1400to1800": 0.6419,
  # "QCD_Pt_1800to2400": 0.0877,
  # "QCD_Pt_2400to3200": 0.005241,
  # "QCD_Pt_3200toInf": 0.0001346,
  
  # "QCD_Pt_30to50": [60, ROOT.kSolid],
  # "QCD_Pt_50to80": [61, ROOT.kSolid],
  # "QCD_Pt_80to120": [62, ROOT.kSolid],
  # "QCD_Pt_120to170": [63, ROOT.kSolid],
  # "QCD_Pt_170to300": [64, ROOT.kSolid],
  # "QCD_Pt_300to470": [65, ROOT.kSolid],
  # "QCD_Pt_470to600": [66, ROOT.kSolid],
  # "QCD_Pt_600to800": [67, ROOT.kSolid],
  # "QCD_Pt_800to1000": [68, ROOT.kSolid],
  # "QCD_Pt_1000to1400": [69, ROOT.kSolid],
  # "QCD_Pt_1400to1800": [70, ROOT.kSolid],
  # "QCD_Pt_1800to2400": [71, ROOT.kSolid],
  # "QCD_Pt_2400to3200": [72, ROOT.kSolid],
  # "QCD_Pt_3200toInf": [73, ROOT.kSolid],