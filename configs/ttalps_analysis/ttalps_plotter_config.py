import ROOT
from ROOT import TColor
from Sample import Sample, SampleType
from Legend import Legend
from Histogram import Histogram
from HistogramNormalizer import NormalizationType

base_path = "/nfs/dust/cms/user/jniedzie/ttalps_cms/"
# base_path = "/Users/jeremi/Documents/Physics/DESY/ttalps_cms.nosync/data/"
output_path = "../plots"

# skim = ""
# skim = "skimmed_looseSemileptonic"
# skim = "skimmed_signalLike"
skim = "skimmed_ttbarLike"
# skim = "skimmed_ttZLike"

# luminosity = 63670. # pb^-1
luminosity = 59830. # recommended lumi from https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2

legends = {
  SampleType.signal: Legend(0.15,0.85,0.25,0.89, "l"),
  SampleType.background: Legend(0.7,0.65,0.85,0.89, "f"),
  SampleType.data: Legend(0.15,0.8,0.25,0.85, "pl"),
}

canvas_size = (800, 600)
show_ratio_plots = True
background_uncertainty_style = 3244 # available styles: https://root.cern.ch/doc/master/classTAttFill.html
background_uncertainty_color = ROOT.kBlack
background_uncertainty_alpha = 0.3


histograms = (
#           name       title                                              logy  norm_type                 rebin xmin xmax ymin ymax,  xlabel              ylabel
  Histogram("n_good_muons", "Number of good muons",                       True, NormalizationType.to_data, 1,   0, 20,    1e1, 1e9,   "Number of good muons",                    "# events (2018)"),
  Histogram("n_almost_good_muons", "Number of almost good muons",         True, NormalizationType.to_data, 1,   0, 20,    1e1, 1e9,   "Number of almost good muons",                    "# events (2018)"),
  Histogram("good_muon_pt", "Muon p_{T}",                                 True, NormalizationType.to_data, 10,   0, 500,   1e-2, 1e6,   "p_{T}^{#mu} [GeV]",                 "# events (2018)"),
  Histogram("good_muon_leading_pt", "Leading muon p_{T}",                 True, NormalizationType.to_data, 10,   0, 500,   1e-2, 1e6,   "Leading p_{T}^{#mu} [GeV]",         "# events (2018)"),
  Histogram("good_muon_subleading_pt", "All subleading muons p_{T}",      True, NormalizationType.to_data, 10,   0, 500,   1e-2, 1e6,   "All subleading p_{T}^{#mu} [GeV]",  "# events (2018)"),
  Histogram("good_muon_eta","Muon #eta",                                  True, NormalizationType.to_data, 5,-3.5, 3.5,    1e0, 1e6,  "#eta^{#mu}",                         "# events (2018)"),
  Histogram("good_muon_dxy","Muon d_{xy}",                                True, NormalizationType.to_data, 10,  -10, 10,   1e-2, 1e6,  "d_{xy}^{#mu}",                       "# events (2018)"),
  Histogram("good_muon_dz", "Muon d_{z}",                                 True, NormalizationType.to_data, 10,  -10, 10,   1e-2, 1e6,  "d_{z}^{#mu}",                        "# events (2018)"),
  
  Histogram("n_good_electrons",  "Number of electrons",                   True, NormalizationType.to_data, 1,   0, 10,    1e1, 1e9,   "Number of electrons", "# events (2018)"),
  Histogram("good_electron_pt",  "Electron p_{T}",                        True, NormalizationType.to_data, 10,   0, 500,   1e-2, 1e6,   "p_{T}^{e} [GeV]",  "# events (2018)"),
  Histogram("good_electron_leading_pt",  "Leading electron p_{T}",        True, NormalizationType.to_data, 10,   0, 500,   1e-2, 1e6,   "Leading p_{T}^{e} [GeV]",  "# events (2018)"),
  Histogram("good_electron_subleading_pt","All subleading electron p_{T}",True, NormalizationType.to_data, 10,   0, 500,   1e-2, 1e6,   "All subleading p_{T}^{e} [GeV]",  "# events (2018)"),
  Histogram("good_electron_eta", "Electron #eta",                         True, NormalizationType.to_data, 5, -3.5, 3.5, 1e-2,  1e6,  "#eta^{e}",         "# events (2018)"),
  Histogram("good_electron_dxy", "Electron d_{xy}",                       True, NormalizationType.to_data, 10,   -10, 10,  1e-2, 1e6,  "d_{xy}^{e}",       "# events (2018)"),
  Histogram("good_electron_dz",  "Electron d_{z}",                        True, NormalizationType.to_data, 10,   -10, 10,  1e-2, 1e6,  "d_{z}^{e}",        "# events (2018)"),
  
  Histogram("n_good_jets",  "Number of jets",                             True, NormalizationType.to_data, 1,   0, 30,    1e0, 1e9,   "Number of jets",   "# events (2018)"),
  Histogram("good_jet_pt",  "Jet p_{T}",                                  True, NormalizationType.to_data, 5,   0, 500,   10, 1e8,    "p_{T}^{j} [GeV]",  "# events (2018)"),
  Histogram("good_jet_eta", "Jet #eta",                                   True, NormalizationType.to_data, 5, -3.5, 3.5, 1e0, 1e10,  "#eta^{j}",         "# events (2018)"),
  Histogram("good_jet_btagDeepB", "Jet btagDeepB",                        True, NormalizationType.to_data, 2,  -1, 1,     1e0, 1e7,  "jet btagDeepB",    "# events (2018)"),
  
  Histogram("n_good_bjets",  "Number of b-jets",                          True, NormalizationType.to_data, 1,   0, 30,    1e0, 1e9,   "Number of b-jets",   "# events (2018)"),
  Histogram("good_bjet_pt",  "b-jet p_{T}",                               True, NormalizationType.to_data, 5,   0, 500,   10, 1e8,    "p_{T}^{j} [GeV]",  "# events (2018)"),
  Histogram("good_bjet_eta", "b-jet #eta",                                True, NormalizationType.to_data, 5, -3.5, 3.5, 1e0, 1e10,  "#eta^{j}",         "# events (2018)"),
  Histogram("good_bjet_btagDeepB", "b-jet btagDeepB",                     True, NormalizationType.to_data, 2,  -1, 1,     1e0, 1e7,  "b-jet btagDeepB",    "# events (2018)"),
  
  Histogram("n_good_nonbjets",  "Number of non-b jets",                   True, NormalizationType.to_data, 1,   0, 30,    1e0, 1e9,   "Number of non-b jets",   "# events (2018)"),
  Histogram("good_nonbjet_pt",  "non-b jet p_{T}",                        True, NormalizationType.to_data, 5,   0, 500,   10, 1e8,    "p_{T}^{j} [GeV]",  "# events (2018)"),
  Histogram("good_nonbjet_eta", "non-b jet #eta",                         True, NormalizationType.to_data, 5, -3.5, 3.5, 1e0, 1e10,  "#eta^{j}",         "# events (2018)"),
  Histogram("good_nonbjet_btagDeepB", "non-b jet btagDeepB",              True, NormalizationType.to_data, 2,  -1, 1,     1e0, 1e7,  "non-b jet btagDeepB",    "# events (2018)"),
  
  Histogram("MET_pt", "MET p_{T}",                                        True, NormalizationType.to_data, 5,  0, 1000,     1e0, 1e5,  "MET p_{T} (GeV)",    "# events (2018)"),
  Histogram("almost_good_dimuon_minv", "Dimuon Mass",                     True, NormalizationType.to_data, 1,  70, 110,     1e0, 1e6,  "m_{#mu#mu} (GeV)",    "# events (2018)"),
  Histogram("dimuon_minv_closestToZ", "Dimuon Mass (Closest to Z mass)",  True, NormalizationType.to_data, 1,  70, 110,     1e0, 1e6,  "m_{#mu#mu} (GeV)",    "# events (2018)"),
  Histogram("dimuon_deltaR_closestToZ", "#Delta R_{#mu#mu} (Closest to Z mass)", True, NormalizationType.to_data, 1,  -1, 6,     1e0, 1e5,  "#Delta R_{#mu#mu}",    "# events (2018)"),
  Histogram("deltaPhi_lepton_MET", "#Delta #phi (MET, l)",                True, NormalizationType.to_data, 1,  -4, 4,     1e0, 1e5,  "#Delta #phi(MET, l)",    "# events (2018)"),
  Histogram("minv_lepton_MET", "m_{MET, l}",                              True, NormalizationType.to_data, 2,  0, 500,     1e0, 1e6,  "m_{MET, l} (GeV)",    "# events (2018)"),
  Histogram("minv_bjet_2jets", "m_(bjj)",                                 True, NormalizationType.to_data, 5,  0, 500,     1e0, 1e6,  "m_(bjj) (GeV)",    "# events (2018)"),
  
  Histogram("cutFlow", "cutflow",                                         True, NormalizationType.to_data, 1,   0, 8,     1e2, 1e10,     "Selection",        "Number of events"),
  Histogram("norm_check", "Norm check",                                   True, NormalizationType.to_data, 1,  0, 1,      1e-2, 1e7,  "norm check",    "# events (2018)"),
)

weightsBranchName = "genWeight"

# data&signals must be listed after backgrounds for now
samples = (
  Sample(
    name="SingleMuon2018",
    file_path=f"{base_path}/collision_data2018/SingleMuon2018_{skim}_histograms.root",
    type=SampleType.data,
    cross_section=1,
    line_alpha=0,
    fill_alpha=0,
    marker_size=1,
    marker_style=20,
    marker_color=ROOT.kBlack,
    legend_description="SingleMuon2018",
  ),
  Sample(
    name="ttZJets",
    file_path=f"{base_path}/backgrounds2018/ttZJets/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=0.5407,
    line_alpha=0,
    fill_color=41,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttZJets",
  ),
  Sample(
    name="ttHToMuMu",
    file_path=f"{base_path}/backgrounds2018/ttHToMuMu/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=0.5269,
    line_alpha=0,
    fill_color=50,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttHToMuMu",
  ),
  Sample(
    name="ttHTobb",
    file_path=f"{base_path}/backgrounds2018/ttHTobb/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=0.5418,
    line_alpha=0,
    fill_color=52,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttHTobb",
  ),
  Sample(
    name="ttWJets",
    file_path=f"{base_path}/backgrounds2018/ttWJets/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=0.4611,
    line_alpha=0,
    fill_color=ROOT.kMagenta,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttWJets",
  ),
  Sample(
    name="ST_tW_top",
    file_path=f"{base_path}/backgrounds2018/ST_tW_top/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=32.45,
    line_alpha=0,
    fill_color=38,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ST_tW_top",
  ),
  Sample(
    name="ST_tW_antitop",
    file_path=f"{base_path}/backgrounds2018/ST_tW_antitop/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=32.51,
    line_alpha=0,
    fill_color=30,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ST_tW_antitop",
  ),
  Sample(
    name="TTToSemiLeptonic",
    file_path=f"{base_path}/backgrounds2018/TTToSemiLeptonic/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=687.1,
    line_alpha=0,
    fill_color=33,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="TTToSemiLeptonic",
  ),
  # Sample(
  #   name="DYJetsToMuMu_M-50",
  #   file_path=f"{base_path}/backgrounds2018/DYJetsToMuMu_M-50/{skim}/histograms/histograms.root",
  #   type=SampleType.background,
  #   cross_section=1976.0,
  #   line_alpha=0,
  #   fill_color=42,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="DYJetsToMuMu_M-50",
  # ),

  # Sample(
  #   name="tta_mAlp-0p35GeV",
  #   file_path=f"{base_path}/signals/tta_mAlp-0p35GeV/{skim}/histograms/tta_mAlp-0p35GeV_nEvents-100000.root",
  #   type=SampleType.signal,
  #   cross_section=1,
  #   line_alpha=1,
  #   line_color=ROOT.kRed,
  #   fill_color=ROOT.kWhite,
  #   fill_alpha=0,
  #   marker_size=0,
  #   legend_description="tta_mAlp-0p35GeV",
  # ),

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