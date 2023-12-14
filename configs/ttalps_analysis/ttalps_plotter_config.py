import ROOT
from ROOT import TColor
from Sample import Sample, SampleType
from Legend import Legend
from Histogram import Histogram
from HistogramNormalizer import NormalizationType

from ttalps_cross_sections import *

base_path = "/nfs/dust/cms/user/jniedzie/ttalps_cms/"
# base_path = "/Users/jeremi/Documents/Physics/DESY/ttalps_cms.nosync/data/"

# hist_path = "histograms"
# hist_path = "histograms_pileup"
hist_path = "histograms_pileupSFs"

# skim = ""
# skim = "skimmed_looseSemileptonic"
# skim = "skimmed_signalLike"
# skim = "skimmed_ttbarLike"

# skim = "skimmed_ttbarSemimuonicCR_tightMuon"
# skim = "skimmed_ttbarSemimuonicCR_tightMuon_newBtag"
# skim = "skimmed_ttbarSemimuonicCR"
# skim = "skimmed_ttbarSemimuonicCR_Met30GeV"
# skim = "skimmed_ttbarSemimuonicCR_Met50GeV"
# skim = "skimmed_ttbarSemimuonicCR_Met50GeV_2mediumBjets"
# skim = "skimmed_ttbarSemimuonicCR_Met50GeV_2tightBjets"
# skim = "skimmed_ttbarSemimuonicCR_Met50GeV_1mediumBjets"
skim = "skimmed_ttbarSemimuonicCR_Met50GeV_1mediumBjets_muonIdIso"

# skim = "skimmed_ttZLike"
# skim = "skimmed_ttZSemimuonicCR_tightMuon_noLooseMuonIso"
# skim = "skimmed_ttZSemimuonicCR_Met50GeV"

# skim = "skimmed_SR_Met50GeV"

output_path = f"../plots_{skim.replace('skimmed_', '')}_{hist_path.replace('histograms_', '').replace('histograms', '')}/"

# luminosity = 63670. # pb^-1
luminosity = 59830. # recommended lumi from https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2

canvas_size = (800, 600)
show_ratio_plots = True
ratio_limits = (0.5, 1.5)

legend_width = 0.17 if show_ratio_plots else 0.20
legend_min_x = 0.45
legend_max_x = 0.83

legend_height = 0.045 if show_ratio_plots else 0.03
legend_max_y = 0.89

n_default_backgrounds = 10

show_cms_labels = True
extraText = "Preliminary"

legends = {
  SampleType.signal: Legend(legend_max_x-3*legend_width, legend_max_y-2*legend_height, legend_max_x-2*legend_width, legend_max_y-legend_height, "l"),
  SampleType.background: Legend(legend_max_x-legend_width, legend_max_y-n_default_backgrounds*legend_height, legend_max_x, legend_max_y, "f"),
  SampleType.data: Legend(legend_max_x-3*(legend_width), legend_max_y-legend_height, legend_max_x-2*(legend_width), legend_max_y, "pl"),
}



background_uncertainty_style = 3244 # available styles: https://root.cern.ch/doc/master/classTAttFill.html
background_uncertainty_color = ROOT.kBlack
background_uncertainty_alpha = 0.3

plotting_options = {
  SampleType.background: "hist",
  SampleType.signal: "nostack e",
  SampleType.data: "nostack e",
}

default_norm = NormalizationType.to_lumi
# default_norm = NormalizationType.to_data

histograms = (
#           name                                  title logy    norm_type                 rebin xmin   xmax    ymin    ymax,   xlabel                                             ylabel
  Histogram("Event_nTightMuons"                   , "", True  , default_norm              , 1  , 0     , 10    , 1e1   , 1e9   , "Number of tight #mu"                            , "# events (2018)"   ),
  Histogram("TightMuons_pt"                       , "", True  , default_norm              , 50 , 0     , 1000  , 1e-6  , 1e8   , "tight #mu p_{T} [GeV]"                          , "# events (2018)"   ),
  # Histogram("TightMuons_leadingPt"                , "", True  , default_norm              , 50 , 0     , 1000  , 1e-5  , 1e5   , "leading tight #mu p_{T} [GeV]"                  , "# events (2018)"   ),
  # # Histogram("TightMuons_subleadingPt"             , "", True  , default_norm              , 50 , 0     , 1000  , 1e-5  , 1e4   , "all subleading tight #mu p_{T} [GeV]"           , "# events (2018)"   ),
  Histogram("TightMuons_eta"                      , "", True  , default_norm              , 10 , -3.0  , 5.0   , 1e0   , 1e5   , "tight #mu #eta"                                 , "# events (2018)"   ),
  Histogram("TightMuons_dxy"                      , "", True  , default_norm              , 2  , -0.5  , 0.5   , 1e-2  , 1e10   , "tight #mu d_{xy} [cm]"                          , "# events (2018)"   ),
  Histogram("TightMuons_dz"                       , "", True  , default_norm              , 2  , -1    , 1     , 1e-2  , 1e8   , "tight #mu d_{z} [cm]"                           , "# events (2018)"   ),
  
  Histogram("TightMuons_pfRelIso04_all"           , "", True  , default_norm              , 1  , 0.0   , 0.2   , 1e-2  , 1e6   , "tight #mu PF Rel Iso 0.4 (all)"                 , "# events (2018)"   ),
  Histogram("TightMuons_pfRelIso03_chg"           , "", True  , default_norm              , 1  , 0     , 0.5   , 1e-2  , 1e6   , "tight #mu PF Rel Iso 0.3 (chg)"                 , "# events (2018)"   ),
  Histogram("TightMuons_pfRelIso03_all"           , "", True  , default_norm              , 1  , 0     , 0.5   , 1e-2  , 1e6   , "tight #mu PF Rel Iso 0.3 (all)"                 , "# events (2018)"   ),
  Histogram("TightMuons_miniPFRelIso_chg"         , "", True  , default_norm              , 10 , -0.1  , 3.5   , 1e-2  , 1e6   , "tight #mu mini PF Rel Iso (chg)"                , "# events (2018)"   ),
  Histogram("TightMuons_miniPFRelIso_all"         , "", True  , default_norm              , 5  , -0.1  , 3.5   , 1e-2  , 1e6   , "tight #mu mini PF Rel Iso (all)"                , "# events (2018)"   ),
  Histogram("TightMuons_jetRelIso"                , "", True  , default_norm              , 50 , -1    , 8.0   , 1e-2  , 1e6   , "tight #mu jet Rel Iso"                          , "# events (2018)"   ),
  Histogram("TightMuons_tkRelIso"                 , "", True  , default_norm              , 20 , -0.1  , 8.0   , 1e-2  , 1e6   , "tight #mu track Rel Iso"                       , "# events (2018)"   ),
  
  Histogram("Event_nLooseMuons"                   , "", True  , default_norm              , 1  , 0     , 10    , 1e1   , 1e9   , "Number of loose #mu"                            , "# events (2018)"   ),
  Histogram("LooseMuons_pt"                       , "", True  , default_norm              , 20 , 0     , 500   , 1e-2  , 1e6   , "loose #mu p_{T} [GeV]"                          , "# events (2018)"   ),
  Histogram("LooseMuons_leadingPt"                , "", True  , default_norm              , 20 , 0     , 500   , 1e-2  , 1e6   , "leading loose #mu p_{T} [GeV]"                  , "# events (2018)"   ),
  # Histogram("LooseMuons_subleadingPt"             , "", True  , default_norm              , 20 , 0     , 500   , 1e-2  , 1e6   , "all subleading loose #mu p_{T} [GeV]"           , "# events (2018)"   ),
  Histogram("LooseMuons_eta"                      , "", True  , default_norm              , 5  , -3.5  , 3.5   , 1e0   , 1e6   , "loose #mu #eta"                                 , "# events (2018)"   ),
  Histogram("LooseMuons_dxy"                      , "", True  , default_norm              , 20 , -10   , 10    , 1e-2  , 1e6   , "loose #mu d_{xy} [cm]"                          , "# events (2018)"   ),
  Histogram("LooseMuons_dz"                       , "", True  , default_norm              , 20 , -10   , 10    , 1e-2  , 1e6   , "loose #mu d_{z} [cm]"                           , "# events (2018)"   ),
  
  Histogram("LooseMuons_pfRelIso04_all"           , "", True  , default_norm              , 1  , 0.0   , 0.2   , 1e-2  , 1e6   , "Loose #mu PF Rel Iso 0.4 (all)"                 , "# events (2018)"   ),
  Histogram("LooseMuons_pfRelIso03_chg"           , "", True  , default_norm              , 1  , 0     , 0.5   , 1e-2  , 1e6   , "Loose #mu PF Rel Iso 0.3 (chg)"                 , "# events (2018)"   ),
  Histogram("LooseMuons_pfRelIso03_all"           , "", True  , default_norm              , 1  , 0     , 0.5   , 1e-2  , 1e6   , "Loose #mu PF Rel Iso 0.3 (all)"                 , "# events (2018)"   ),
  Histogram("LooseMuons_miniPFRelIso_chg"         , "", True  , default_norm              , 10 , -0.1  , 3.5   , 1e-2  , 1e6   , "Loose #mu mini PF Rel Iso (chg)"                , "# events (2018)"   ),
  Histogram("LooseMuons_miniPFRelIso_all"         , "", True  , default_norm              , 5  , -0.1  , 3.5   , 1e-2  , 1e6   , "Loose #mu mini PF Rel Iso (all)"                , "# events (2018)"   ),
  Histogram("LooseMuons_jetRelIso"                , "", True  , default_norm              , 50 , -1    , 8.0   , 1e-2  , 1e6   , "Loose #mu jet Rel Iso"                          , "# events (2018)"   ),
  Histogram("LooseMuons_tkRelIso"                 , "", True  , default_norm              , 20 , -0.1  , 8.0   , 1e-2  , 1e6   , "Loose #mu track Rel Iso"                       , "# events (2018)"   ),
  
  # Histogram("Event_nLooseDSAMuons"                 , "", True  , default_norm              , 1  , 0     , 10    , 1e1   , 1e9   , "Number of loose dSA #mu"                        , "# events (2018)"   ),
  # Histogram("LooseDSAMuons_pt"                     , "", True  , default_norm              , 20 , 0     , 500   , 1e-2  , 1e6   , "loose dSA #mu p_{T} [GeV]"                      , "# events (2018)"   ),
  # Histogram("LooseDSAMuons_eta"                    , "", True  , default_norm              , 5  , -3.5  , 3.5   , 1e0   , 1e6   , "loose dSA #mu #eta"                             , "# events (2018)"   ),
  # Histogram("LooseDSAMuons_dxy"                    , "", True  , default_norm              , 20 , -10   , 10    , 1e-2  , 1e6   , "loose dSA #mu d_{xy} [cm]"                      , "# events (2018)"   ),
  # Histogram("LooseDSAMuons_dz"                     , "", True  , default_norm              , 20 , -10   , 10    , 1e-2  , 1e6   , "loose dSA #mu d_{z} [cm]"                       , "# events (2018)"   ),
  
  # # Histogram("Event_nLooseElectrons"               , "", True  , default_norm              , 1  , 0     , 10    , 1e1   , 1e9   , "Number of loose electrons"                      , "# events (2018)"   ),
  # # Histogram("LooseElectrons_pt"                   , "", True  , default_norm              , 10 , 0     , 500   , 1e-2  , 1e6   , "loose electron p_{T} [GeV]"                     , "# events (2018)"   ),
  # # Histogram("LooseElectrons_leadingPt"            , "", True  , default_norm              , 10 , 0     , 500   , 1e-2  , 1e6   , "leading loose electron p_{T} [GeV]"             , "# events (2018)"   ),
  # # Histogram("LooseElectrons_subleadingPt"         , "", True  , default_norm              , 10 , 0     , 500   , 1e-2  , 1e6   , "all subleading loose electron p_{T} [GeV]"      , "# events (2018)"   ),
  # # Histogram("LooseElectrons_eta"                  , "", True  , default_norm              , 5  , -3.5  , 3.5   , 1e-2  , 1e6   , "loose electron #eta"                            , "# events (2018)"   ),
  # # Histogram("LooseElectrons_dxy"                  , "", True  , default_norm              , 10 , -10   , 10    , 1e-2  , 1e6   , "loose electron d_{xy}"                          , "# events (2018)"   ),
  # # Histogram("LooseElectrons_dz"                   , "", True  , default_norm              , 10 , -10   , 10    , 1e-2  , 1e6   , "loose electron d_{z}"                           , "# events (2018)"   ),
  
  Histogram("Event_nGoodJets"                     , "", True  , default_norm              , 1  , 2     , 16    , 1e-2  , 1e10   , "Number of good jets"                            , "# events (2018)"   ),
  # Histogram("GoodJets_pt"                         , "", True  , default_norm              , 25 , 0     , 1300  , 1e-3  , 1e6   , "good jet p_{T} [GeV]"                           , "# events (2018)"   ),
  # Histogram("GoodJets_eta"                        , "", True  , default_norm              , 10 , -3    , 5.0   , 1e1   , 1e6   , "good jet #eta"                                  , "# events (2018)"   ),
  # Histogram("GoodJets_btagDeepB"                  , "", True  , default_norm              , 10 , 0     , 1.5   , 2e0   , 1e6   , "good jet deepCSV score"                         , "# events (2018)"   ),
  Histogram("GoodJets_btagDeepFlavB"              , "", True  , default_norm              , 10 , 0     , 1.8   , 1e-1   , 1e8   , "good jet deepJet score"                         , "# events (2018)"   ),
  
  # Histogram("Event_nGoodMediumBtaggedJets"              , "", True  , default_norm              , 1  , 0     , 20    , 1e0   , 1e9   , "Number of good b-jets"                          , "# events (2018)"   ),
  # Histogram("GoodMediumBtaggedJets_pt"                  , "", True  , default_norm              , 50 , 0     , 2000  , 1e-5  , 1e4   , "good b-jet p_{T} [GeV]"                         , "# events (2018)"   ),
  # Histogram("GoodMediumBtaggedJets_eta"                 , "", True  , default_norm              , 5  , -3.5  , 3.5   , 1e0   , 1e10  , "good b-jet #eta"                                , "# events (2018)"   ),
  # Histogram("GoodMediumBtaggedJets_btagDeepB"           , "", True  , default_norm              , 10 , -1    , 1     , 1e0   , 1e8   , "good b-jet btagDeepB"                           , "# events (2018)"   ),
  
  # Histogram("Event_nGoodNonTightBtaggedJets"           , "", True  , default_norm              , 1  , 0     , 20    , 1e0   , 1e9   , "Number of good non-b jets"                      , "# events (2018)"   ),
  # Histogram("GoodNonTightBtaggedJets_pt"               , "", True  , default_norm              , 50 , 0     , 2000  , 1e-5  , 1e4   , "good non-b jet p_{T} [GeV]"                     , "# events (2018)"   ),
  # Histogram("GoodNonTightBtaggedJets_eta"              , "", True  , default_norm              , 5  , -3.5  , 3.5   , 1e0   , 1e10  , "good non-b jet #eta"                            , "# events (2018)"   ),
  # Histogram("GoodNonTightBtaggedJets_btagDeepB"        , "", True  , default_norm              , 10 , -1    , 1     , 1e0   , 1e8   , "good non-b jet btagDeepB"                       , "# events (2018)"   ),
  
  Histogram("Event_METpt"                         , "", True  , default_norm              , 10 , 0     , 800   , 1e-5  , 1e9   , "MET p_{T} [GeV]"                                , "# events (2018)"   ),
  # Histogram("Event_PV_npvs"                       , "", True  , default_norm              , 1  , 0     , 150   , 1e-3  , 1e12   , "# Primary vertices"                             , "# events (2018)"   ),
  # Histogram("Event_PV_npvsGood"                   , "", True  , default_norm              , 1  , 0     , 150   , 1e-3  , 1e6   , "# Good primary vertices"                        , "# events (2018)"   ),
  
  # Histogram("LooseMuons_dimuonMinv"               , "", True  , default_norm              , 1  , 70    , 110   , 1e0   , 1e4   , "loose muons m_{#mu#mu} [GeV]"                   , "# events (2018)"   ),
  # Histogram("LooseMuons_dimuonMinvClosestToZ"     , "", True  , default_norm              , 1  , 70    , 110   , 1e0   , 1e4   , "loose muons closest to Z m_{#mu#mu} [GeV]"      , "# events (2018)"   ),
  # Histogram("LooseMuons_dimuonDeltaRclosestToZ"   , "", True  , default_norm              , 1  , -1    , 6     , 1e0   , 1e3   , "loose muons closest to Z #Delta R_{#mu#mu}"     , "# events (2018)"   ),
  # Histogram("LooseMuons_dimuonDeltaEtaclosestToZ" , "", True  , default_norm              , 1  , -1    , 6     , 1e-1  , 1e3   , "loose muons closest to Z #Delta #eta_{#mu#mu}"  , "# events (2018)"   ),
  # Histogram("LooseMuons_dimuonDeltaPhiclosestToZ" , "", True  , default_norm              , 1  , -3.5  , 6     , 1e-1  , 1e3   , "loose muons closest to Z #Delta #phi_{#mu#mu}"  , "# events (2018)"   ),
  
  # Histogram("TightMuons_deltaPhiMuonMET"          , "", True  , default_norm              , 20 , -4    , 4     , 1e0   , 1e7   , "tight muon #Delta #phi(MET, #mu)"               , "# events (2018)"   ),
  # Histogram("TightMuons_minvMuonMET"              , "", True  , default_norm              , 40 , 0     , 1000  , 1e-4  , 1e5   , "tight muon m_{MET, l} [GeV]"                    , "# events (2018)"   ),
  # Histogram("GoodJets_minvBjet2jets"              , "", True  , default_norm              , 25 , 0     , 1500  , 1e-1  , 1e5   , "good jets m_{bjj} [GeV]"                        , "# events (2018)"   ),
  
  Histogram("cutFlow"                             , "", True  , NormalizationType.to_lumi , 1  , 0     , 12    , 1e1   , 1e15  , "Selection"                                      , "Number of events"  ),
  Histogram("Event_normCheck"                     , "", True  , NormalizationType.to_lumi , 1  , 0     , 1     , 1e-2  , 1e7   , "norm check"                                     , "# events (2018)"   ),
)

weightsBranchName = "genWeight"

color_palette_wong = (
    TColor.GetColor(230, 159, 0),
    TColor.GetColor(86, 180, 233),
    TColor.GetColor(0, 158, 115),
    TColor.GetColor(0, 114, 178),
    TColor.GetColor(213, 94, 0),
)

samples = (
  # Data
  Sample(
    name="SingleMuon",
    file_path=f"{base_path}/collision_data2018/SingleMuon2018_{skim}_{hist_path}.root",
    type=SampleType.data,
    cross_sections=cross_sections,
    line_alpha=1,
    fill_alpha=0,
    marker_size=0.7,
    marker_style=20,
    marker_color=ROOT.kBlack,
    legend_description="SingleMuon2018",
  ),
  
  # Signal
  # Sample(
  #   name="tta_mAlp-0p35GeV_ctau-1e2mm",
  #   file_path=f"{base_path}/signals/tta_mAlp-0p35GeV_ctau-1e2mm/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.signal,
  #   cross_sections=cross_sections,
  #   line_alpha=1,
  #   line_style=2,
  #   fill_alpha=0,
  #   marker_size=0,
  #   line_color=ROOT.kGreen+1,
  #   legend_description="0.35 GeV, 1e2 mm",
  # ),
  # Sample(
  #   name="tta_mAlp-0p35GeV_ctau-1e3mm",
  #   file_path=f"{base_path}/signals/tta_mAlp-0p35GeV_ctau-1e3mm/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.signal,
  #   cross_sections=cross_sections,
  #   line_alpha=1,
  #   line_style=2,
  #   fill_alpha=0,
  #   marker_size=0,
  #   line_color=ROOT.kBlue,
  #   legend_description="0.35 GeV, 1e3 mm",
  # ),
  # Sample(
  #   name="tta_mAlp-0p35GeV_ctau-1e5mm",
  #   file_path=f"{base_path}/signals/tta_mAlp-0p35GeV_ctau-1e5mm/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.signal,
  #   cross_sections=cross_sections,
  #   line_alpha=1,
  #   line_style=2,
  #   fill_alpha=0,
  #   marker_size=0,
  #   line_color=ROOT.kMagenta,
  #   legend_description="0.35 GeV, 1e5 mm",
  # ),
  
  # Backgrounds
  Sample(
    name="TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",
    file_path=f"{base_path}/backgrounds2018/TTToSemiLeptonic/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=ROOT.kRed+1,
    fill_alpha=1.0,
    marker_size=0,
    legend_description="tt (semi-leptonic)",
  ),
  
  Sample(
    name="TTToHadronic_TuneCP5_13TeV-powheg-pythia8",
    file_path=f"{base_path}/backgrounds2018/TTToHadronic/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=ROOT.kRed+3,
    fill_alpha=1.0,
    marker_size=0,
    legend_description="tt (hadronic)",
  ),
    
  Sample(
    name="TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8",
    file_path=f"{base_path}/backgrounds2018/TTTo2L2Nu/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=ROOT.kRed+4,
    fill_alpha=1.0,
    marker_size=0,
    legend_description="tt (leptonic)",
  ),
  
  Sample(
    name="ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5CR1_13TeV-powheg-pythia8",
    file_path=f"{base_path}/backgrounds2018/ST_tW_top/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[1],
    fill_alpha=0.7,
    marker_size=0,
    legend_description="Single top (tW)",
    custom_legend=Legend(legend_max_x-2*legend_width, legend_max_y-1*legend_height, legend_max_x-legend_width, legend_max_y-0*legend_height, "f")
  ),
  Sample(
    name="ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5CR1_13TeV-powheg-pythia8",
    file_path=f"{base_path}/backgrounds2018/ST_tW_antitop/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[1],
    fill_alpha=0.7,
    marker_size=0,
    legend_description=" ",
    custom_legend=Legend(0, 0, 0, 0, "")
  ),
  Sample(
    name="ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
    file_path=f"{base_path}/backgrounds2018/ST_t-channel_top/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[2],
    fill_alpha=0.7,
    marker_size=0,
    legend_description="Single top (t-ch.)",
    custom_legend=Legend(legend_max_x-2*legend_width, legend_max_y-2*legend_height, legend_max_x-legend_width, legend_max_y-1*legend_height, "f")
  ),
  Sample(
    name="ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
    file_path=f"{base_path}/backgrounds2018/ST_t-channel_antitop/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[2],
    fill_alpha=0.7,
    marker_size=0,
    legend_description=" ",
    custom_legend=Legend(0, 0, 0, 0, "")
  ),
  
  # Sample(
  #   name="DYJetsToMuMu_M-10to50_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
  #   file_path=f"{base_path}/backgrounds2018/DYJetsToMuMu_M-10to50/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kMagenta+1,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   # legend_description="DY",
  #   # custom_legend=Legend(legend_max_x-2*legend_width, legend_max_y-3*legend_height, legend_max_x-legend_width, legend_max_y-2*legend_height, "f"),
  #   legend_description=" ",
  #   custom_legend=Legend(0, 0, 0, 0, ""),
  # ),
  # Sample(
  #   name="DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
  #   file_path=f"{base_path}/backgrounds2018/DYJetsToMuMu_M-50/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kMagenta+1,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="DY",
  #   custom_legend=Legend(legend_max_x-2*legend_width, legend_max_y-3*legend_height, legend_max_x-legend_width, legend_max_y-2*legend_height, "f"),
  #   # legend_description=" ",
  #   # custom_legend=Legend(0, 0, 0, 0, ""),
  # ),
  
  Sample(
    name="WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8",
    file_path=f"{base_path}/backgrounds2018/WJetsToLNu/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=ROOT.kViolet+1,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="W+jets",
  ),
  
  # Sample(
  #   name="ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8",
  #   file_path=f"{base_path}/backgrounds2018/ttZJets/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=41,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="ttZJets",
  # ),
  Sample(
    name="TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8",
    file_path=f"{base_path}/backgrounds2018/TTZToLLNuNu/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=ROOT.kYellow+3,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttZ",
  ),
  Sample(
    name="TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8",
    file_path=f"{base_path}/backgrounds2018/TTZToLLNuNu_M-1to10/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=ROOT.kGray,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttZ (1-10)",
  ),
  
  # Sample(
  #   name="ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8",
  #   file_path=f"{base_path}/backgrounds2018/ttWJets/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kOrange,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="ttWJets",
  # ),
  Sample(
    name="TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8",
    file_path=f"{base_path}/backgrounds2018/TTWJetsToLNu/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=ROOT.kYellow+1,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttW",
  ),
  
  # Sample(
  #   name="ttHToMuMu_M125_TuneCP5_13TeV-powheg-pythia8",
  #   file_path=f"{base_path}/backgrounds2018/ttHToMuMu/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=color_palette_wong[3],
  #   fill_alpha=1.0,
  #   marker_size=0,
  #   legend_description="ttH (#mu#mu)",
  # ),
  Sample(
    name="ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8",
    file_path=f"{base_path}/backgrounds2018/ttHTobb/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[4],
    fill_alpha=1.0,
    marker_size=0,
    legend_description="ttH (bb)",
  ),
  Sample(
    name="ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8",
    file_path=f"{base_path}/backgrounds2018/ttHToNonbb/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=ROOT.kBlue+1,
    fill_alpha=1.0,
    marker_size=0,
    legend_description="ttH (non-bb)",
  ),
  
  Sample(
    name="TTZZ_TuneCP5_13TeV-madgraph-pythia8",
    file_path=f"{base_path}/backgrounds2018/TTZZ/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=ROOT.kGray+1,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttZZ",
  ),
  Sample(
    name="TTZH_TuneCP5_13TeV-madgraph-pythia8",
    file_path=f"{base_path}/backgrounds2018/TTZH/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=ROOT.kGray+2,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttZH",
  ),
  # Sample(
  #   name="TTTT_TuneCP5_13TeV-amcatnlo-pythia8",
  #   file_path=f"{base_path}/backgrounds2018/TTTT/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kGray+3,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="TTTT",
  # ),
    
  # Sample(
  #   name="QCD_Pt_120to170_TuneCP5_13TeV_pythia8",
  #   file_path=f"{base_path}/backgrounds2018/QCD_Pt_120to170/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kGreen+2,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="QCD pt = 120to170 GeV",
  # ),
  # Sample(
  #   name="QCD_Pt_170to300_TuneCP5_13TeV_pythia8",
  #   file_path=f"{base_path}/backgrounds2018/QCD_Pt_170to300/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kGreen-3,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="QCD pt = 170to300 GeV",
  # ),
  # Sample(
  #   name="QCD_Pt_300to470_TuneCP5_13TeV_pythia8",
  #   file_path=f"{base_path}/backgrounds2018/QCD_Pt_300to470/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kGreen-2,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="QCD pt = 300to470 GeV",
  # ),
  # Sample(
  #   name="QCD_Pt_470to600_TuneCP5_13TeV_pythia8",
  #   file_path=f"{base_path}/backgrounds2018/QCD_Pt_470to600/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kGreen,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="QCD pt = 470to600 GeV",
  # ),
  # Sample(
  #   name="QCD_Pt_600to800_TuneCP5_13TeV_pythia8",
  #   file_path=f"{base_path}/backgrounds2018/QCD_Pt_600to800/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kGreen+2,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="QCD pt = 600to800 GeV",
  # ),
  # Sample(
  #   name="QCD_Pt_800to1000_TuneCP5_13TeV_pythia8",
  #   file_path=f"{base_path}/backgrounds2018/QCD_Pt_800to1000/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kGreen+3,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="QCD pt = 800to1000 GeV",
  # ),
  # Sample(
  #   name="QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8",
  #   file_path=f"{base_path}/backgrounds2018/QCD_Pt_1000to1400/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kGreen+4,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="QCD pt = 1000to1400 GeV",
  # ),
  # Sample(
  #   name="QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8",
  #   file_path=f"{base_path}/backgrounds2018/QCD_Pt_1400to1800/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kGreen+4,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="QCD pt = 1400to1800 GeV",
  # ),
  Sample(
    name="QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_50to80_MuEnriched/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[0],
    fill_alpha=1.0,
    marker_size=0,
    legend_description=" ",
    custom_legend=Legend(0, 0, 0, 0, "")
  ),
  Sample(
    name="QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_80to120_MuEnriched/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[0],
    fill_alpha=1.0,
    marker_size=0,
    legend_description=" ",
    custom_legend=Legend(0, 0, 0, 0, "")
  ),
  Sample(
    name="QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_120to170_MuEnriched/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[0],
    fill_alpha=1.0,
    marker_size=0,
    # legend_description="QCD (#mu enriched)",
    # custom_legend=Legend(legend_max_x-2*legend_width, legend_max_y-4*legend_height, legend_max_x-legend_width, legend_max_y-3*legend_height, "f"),
    legend_description=" ",
    custom_legend=Legend(0, 0, 0, 0, ""),
  ),
  Sample(
    name="QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_170to300_MuEnriched/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[0],
    fill_alpha=1.0,
    marker_size=0,
    legend_description="QCD (#mu enriched)",
    custom_legend=Legend(legend_max_x-2*legend_width, legend_max_y-3*legend_height, legend_max_x-legend_width, legend_max_y-2*legend_height, "f"),
    # legend_description=" ",
    # custom_legend=Legend(0, 0, 0, 0, ""),
  ),
  Sample(
    name="QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_300to470_MuEnriched/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[0],
    fill_alpha=1.0,
    marker_size=0,
    legend_description=" ",
    custom_legend=Legend(0, 0, 0, 0, "")
  ),
  Sample(
    name="QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_470to600_MuEnriched/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[0],
    fill_alpha=1.0,
    marker_size=0,
    legend_description=" ",
    custom_legend=Legend(0, 0, 0, 0, "")
  ),
  Sample(
    name="QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_600to800_MuEnriched/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[0],
    fill_alpha=1.0,
    marker_size=0,
    legend_description=" ",
    custom_legend=Legend(0, 0, 0, 0, "")
  ),
  Sample(
    name="QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_800to1000_MuEnriched/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[0],
    fill_alpha=1.0,
    marker_size=0,
    legend_description=" ",
    custom_legend=Legend(0, 0, 0, 0, "")
  ),
  Sample(
    name="QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_1000_MuEnriched/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[0],
    fill_alpha=1.0,
    marker_size=0,
    legend_description=" ",
    custom_legend=Legend(0, 0, 0, 0, "")
  ),
)


custom_stacks_order = (
  "SingleMuon",
  
  
  "ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8",
  "TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8",
  "TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8",
  
  "TTZZ_TuneCP5_13TeV-madgraph-pythia8",
  "TTZH_TuneCP5_13TeV-madgraph-pythia8",
  "TTTT_TuneCP5_13TeV-amcatnlo-pythia8",
  
  "ttHToMuMu_M125_TuneCP5_13TeV-powheg-pythia8",
  "ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8",
  "ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8",
  
  "DYJetsToMuMu_M-10to50_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
  "DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
  
  "ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
  "ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
  
  
  "TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8",
  "WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8",
  
  "ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5CR1_13TeV-powheg-pythia8",
  "ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5CR1_13TeV-powheg-pythia8",
  
  "QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8", 
  "QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
  "QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8", 
  "QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8", 
  "QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8", 
  "QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8", 
  "QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8", 
  "QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
  "QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
  
  "QCD_Pt_120to170_TuneCP5_13TeV_pythia8",
  "QCD_Pt_170to300_TuneCP5_13TeV_pythia8",
  "QCD_Pt_300to470_TuneCP5_13TeV_pythia8",
  "QCD_Pt_470to600_TuneCP5_13TeV_pythia8",
  "QCD_Pt_600to800_TuneCP5_13TeV_pythia8",
  "QCD_Pt_800to1000_TuneCP5_13TeV_pythia8",
  "QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8",
  "QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8",
  
  "TTToHadronic_TuneCP5_13TeV-powheg-pythia8",
  "TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8",
  "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",
  
  "tta_mAlp-0p35GeV_ctau-1e2mm",
  "tta_mAlp-0p35GeV_ctau-1e3mm",
  "tta_mAlp-0p35GeV_ctau-1e5mm",
)