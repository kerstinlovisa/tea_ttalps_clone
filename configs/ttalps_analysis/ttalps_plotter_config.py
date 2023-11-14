import ROOT
from ROOT import TColor
from Sample import Sample, SampleType
from Legend import Legend
from Histogram import Histogram
from HistogramNormalizer import NormalizationType

from ttalps_cross_sections import *

base_path = "/nfs/dust/cms/user/jniedzie/ttalps_cms/"
# base_path = "/Users/jeremi/Documents/Physics/DESY/ttalps_cms.nosync/data/"

output_path = "../plots"
# output_path = "../plots_noSFs"

# hist_path = "histograms"
# hist_path = "histograms_noSFs"
hist_path = "histograms_noTriggerSFs"

# skim = ""
# skim = "skimmed_looseSemileptonic"
# skim = "skimmed_signalLike"
# skim = "skimmed_ttbarLike"
# skim = "skimmed_ttZLike"
# skim = "skimmed_ttbarSemimuonicCR_tightMuon"
skim = "skimmed_ttZSemimuonicCR_tightMuon_noLooseMuonIso"

# luminosity = 63670. # pb^-1
luminosity = 59830. # recommended lumi from https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2

legend_width = 0.20
legend_min_x = 0.40
legend_max_x = 0.89

legend_height = 0.05
legend_max_y = 0.89

n_default_backgrounds = 6

legends = {
  SampleType.signal: Legend(legend_max_x-3*legend_width, legend_max_y-2*legend_height, legend_max_x-2*legend_width, legend_max_y-legend_height, "l"),
  SampleType.background: Legend(legend_max_x-legend_width, legend_max_y-n_default_backgrounds*legend_height, legend_max_x, legend_max_y, "f"),
  SampleType.data: Legend(legend_max_x-3*(legend_width), legend_max_y-legend_height, legend_max_x-2*(legend_width), legend_max_y, "pl"),
}

canvas_size = (800, 600)
show_ratio_plots = True
ratio_limits = (0.0, 2.0)

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
  # Histogram("Event_nTightMuons"                   , "", True  , default_norm              , 1  , 0     , 10    , 1e1   , 1e9   , "Number of tight #mu"                            , "# events (2018)"   ),
  # Histogram("TightMuons_pt"                       , "", True  , default_norm              , 50 , 0     , 450   , 1e-2  , 1e4   , "tight #mu p_{T} [GeV]"                          , "# events (2018)"   ),
  # Histogram("TightMuons_leadingPt"                , "", True  , default_norm              , 50 , 0     , 1000  , 1e-5  , 1e4   , "leading tight #mu p_{T} [GeV]"                  , "# events (2018)"   ),
  # Histogram("TightMuons_subleadingPt"             , "", True  , default_norm              , 50 , 0     , 1000  , 1e-5  , 1e4   , "all subleading tight #mu p_{T} [GeV]"           , "# events (2018)"   ),
  # Histogram("TightMuons_eta"                      , "", True  , default_norm              , 10 , -3.0  , 5.0   , 1e0   , 2e3   , "tight #mu #eta"                                 , "# events (2018)"   ),
  # Histogram("TightMuons_dxy"                      , "", True  , default_norm              , 1  , -0.5  , 0.5   , 1e-2  , 1e6   , "tight #mu d_{xy} [cm]"                          , "# events (2018)"   ),
  # Histogram("TightMuons_dz"                       , "", True  , default_norm              , 1  , -1    , 1     , 1e-2  , 1e6   , "tight #mu d_{z} [cm]"                           , "# events (2018)"   ),
  
  # Histogram("Event_nLooseMuons"                   , "", True  , default_norm              , 1  , 0     , 10    , 1e1   , 1e9   , "Number of loose #mu"                            , "# events (2018)"   ),
  # Histogram("LooseMuons_pt"                       , "", True  , default_norm              , 20 , 0     , 500   , 1e-2  , 1e6   , "loose #mu p_{T} [GeV]"                          , "# events (2018)"   ),
  # Histogram("LooseMuons_leadingPt"                , "", True  , default_norm              , 20 , 0     , 500   , 1e-2  , 1e6   , "leading loose #mu p_{T} [GeV]"                  , "# events (2018)"   ),
  # Histogram("LooseMuons_subleadingPt"             , "", True  , default_norm              , 20 , 0     , 500   , 1e-2  , 1e6   , "all subleading loose #mu p_{T} [GeV]"           , "# events (2018)"   ),
  # Histogram("LooseMuons_eta"                      , "", True  , default_norm              , 5  , -3.5  , 3.5   , 1e0   , 1e6   , "loose #mu #eta"                                 , "# events (2018)"   ),
  # Histogram("LooseMuons_dxy"                      , "", True  , default_norm              , 2  , -10   , 10    , 1e-2  , 1e6   , "loose #mu d_{xy} [cm]"                          , "# events (2018)"   ),
  # Histogram("LooseMuons_dz"                       , "", True  , default_norm              , 2  , -10   , 10    , 1e-2  , 1e6   , "loose #mu d_{z} [cm]"                           , "# events (2018)"   ),
  
  # Histogram("Event_nLooseElectrons"               , "", True  , default_norm              , 1  , 0     , 10    , 1e1   , 1e9   , "Number of loose electrons"                      , "# events (2018)"   ),
  # # Histogram("LooseElectrons_pt"                   , "", True  , default_norm              , 10 , 0     , 500   , 1e-2  , 1e6   , "loose electron p_{T} [GeV]"                     , "# events (2018)"   ),
  # # Histogram("LooseElectrons_leadingPt"            , "", True  , default_norm              , 10 , 0     , 500   , 1e-2  , 1e6   , "leading loose electron p_{T} [GeV]"             , "# events (2018)"   ),
  # # Histogram("LooseElectrons_subleadingPt"         , "", True  , default_norm              , 10 , 0     , 500   , 1e-2  , 1e6   , "all subleading loose electron p_{T} [GeV]"      , "# events (2018)"   ),
  # # Histogram("LooseElectrons_eta"                  , "", True  , default_norm              , 5  , -3.5  , 3.5   , 1e-2  , 1e6   , "loose electron #eta"                            , "# events (2018)"   ),
  # # Histogram("LooseElectrons_dxy"                  , "", True  , default_norm              , 10 , -10   , 10    , 1e-2  , 1e6   , "loose electron d_{xy}"                          , "# events (2018)"   ),
  # # Histogram("LooseElectrons_dz"                   , "", True  , default_norm              , 10 , -10   , 10    , 1e-2  , 1e6   , "loose electron d_{z}"                           , "# events (2018)"   ),
  
  # Histogram("Event_nGoodJets"                     , "", True  , default_norm              , 1  , 2     , 16    , 1e-2  , 1e7   , "Number of good jets"                            , "# events (2018)"   ),
  # Histogram("GoodJets_pt"                         , "", True  , default_norm              , 50 , 0     , 1300  , 1e-3  , 1e4   , "good jet p_{T} [GeV]"                           , "# events (2018)"   ),
  # Histogram("GoodJets_eta"                        , "", True  , default_norm              , 10 , -3    , 5.0   , 1e1   , 1e4   , "good jet #eta"                                  , "# events (2018)"   ),
  # Histogram("GoodJets_btagDeepB"                  , "", True  , default_norm              , 10 , 0     , 1.5   , 2e0   , 1e5   , "good jet btagDeepB"                             , "# events (2018)"   ),
  
  # Histogram("Event_nGoodBtaggedJets"              , "", True  , default_norm              , 1  , 0     , 20    , 1e0   , 1e9   , "Number of good b-jets"                          , "# events (2018)"   ),
  # Histogram("GoodBtaggedJets_pt"                  , "", True  , default_norm              , 50 , 0     , 2000  , 1e-5  , 1e4   , "good b-jet p_{T} [GeV]"                         , "# events (2018)"   ),
  # Histogram("GoodBtaggedJets_eta"                 , "", True  , default_norm              , 5  , -3.5  , 3.5   , 1e0   , 1e10  , "good b-jet #eta"                                , "# events (2018)"   ),
  # Histogram("GoodBtaggedJets_btagDeepB"           , "", True  , default_norm              , 10 , -1    , 1     , 1e0   , 1e8   , "good b-jet btagDeepB"                           , "# events (2018)"   ),
  
  # Histogram("Event_nGoodNonBtaggedJets"           , "", True  , default_norm              , 1  , 0     , 20    , 1e0   , 1e9   , "Number of good non-b jets"                      , "# events (2018)"   ),
  # Histogram("GoodNonBtaggedJets_pt"               , "", True  , default_norm              , 50 , 0     , 2000  , 1e-5  , 1e4   , "good non-b jet p_{T} [GeV]"                     , "# events (2018)"   ),
  # Histogram("GoodNonBtaggedJets_eta"              , "", True  , default_norm              , 5  , -3.5  , 3.5   , 1e0   , 1e10  , "good non-b jet #eta"                            , "# events (2018)"   ),
  # Histogram("GoodNonBtaggedJets_btagDeepB"        , "", True  , default_norm              , 10 , -1    , 1     , 1e0   , 1e8   , "good non-b jet btagDeepB"                       , "# events (2018)"   ),
  
  # Histogram("Event_METpt"                         , "", True  , default_norm              , 40 , 0     , 640   , 1e-3  , 2e3   , "MET p_{T} [GeV]"                                , "# events (2018)"   ),
  
  # Histogram("LooseMuons_dimuonMinv"               , "", True  , default_norm              , 1  , 70    , 110   , 1e0   , 1e4   , "loose muons m_{#mu#mu} [GeV]"                   , "# events (2018)"   ),
  # Histogram("LooseMuons_dimuonMinvClosestToZ"     , "", True  , default_norm              , 1  , 70    , 110   , 1e0   , 1e4   , "loose muons closest to Z m_{#mu#mu} [GeV]"      , "# events (2018)"   ),
  # Histogram("LooseMuons_dimuonDeltaRclosestToZ"   , "", True  , default_norm              , 1  , -1    , 6     , 1e0   , 1e3   , "loose muons closest to Z #Delta R_{#mu#mu}"     , "# events (2018)"   ),
  # Histogram("LooseMuons_dimuonDeltaEtaclosestToZ" , "", True  , default_norm              , 1  , -1    , 6     , 1e0   , 1e3   , "loose muons closest to Z #Delta #eta_{#mu#mu}"  , "# events (2018)"   ),
  # Histogram("LooseMuons_dimuonDeltaPhiclosestToZ" , "", True  , default_norm              , 1  , -3.5  , 6     , 1e0   , 1e3   , "loose muons closest to Z #Delta #phi_{#mu#mu}"  , "# events (2018)"   ),
  
  # Histogram("TightMuons_deltaPhiMuonMET"          , "", True  , default_norm              , 20 , -4    , 4     , 1e0   , 1e7   , "tight muon #Delta #phi(MET, #mu)"               , "# events (2018)"   ),
  # Histogram("TightMuons_minvMuonMET"              , "", True  , default_norm              , 40 , 0     , 1000  , 1e-4  , 2e3   , "tight muon m_{MET, l} [GeV]"                    , "# events (2018)"   ),
  # Histogram("GoodJets_minvBjet2jets"              , "", True  , default_norm              , 30 , 0     , 1500  , 1e-1  , 1e5   , "good jets m_{bjj} [GeV]"                        , "# events (2018)"   ),
  
  Histogram("cutFlow"                             , "", True  , NormalizationType.to_lumi , 1  , 0     , 12    , 1e2   , 1e11  , "Selection"                                      , "Number of events"  ),
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
  Sample(
    name="ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8",
    file_path=f"{base_path}/backgrounds2018/ttZJets/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=41,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttZJets",
  ),
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
  
  Sample(
    name="ttHToMuMu_M125_TuneCP5_13TeV-powheg-pythia8",
    file_path=f"{base_path}/backgrounds2018/ttHToMuMu/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[3],
    fill_alpha=1.0,
    marker_size=0,
    legend_description="ttH (#mu#mu)",
  ),
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
    name="ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
    file_path=f"{base_path}/backgrounds2018/ST_t-channel_top/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[2],
    fill_alpha=0.7,
    marker_size=0,
    legend_description="Single top (t-channel)",
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
  #   name="WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8",
  #   file_path=f"{base_path}/backgrounds2018/WJetsToLNu/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kViolet+1,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="W+jets",
  # ),
  # Sample(
  #   name="DYJetsToMuMu_M-10to50_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
  #   file_path=f"{base_path}/backgrounds2018/DYJetsToMuMu_M-10to50/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=ROOT.kMagenta+1,
  #   fill_alpha=0.7,
  #   marker_size=0,
  #   legend_description="DY",
  #   custom_legend=Legend(legend_max_x-2*legend_width, legend_max_y-3*legend_height, legend_max_x-legend_width, legend_max_y-2*legend_height, "f")
  # ),
  Sample(
    name="DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
    file_path=f"{base_path}/backgrounds2018/DYJetsToMuMu_M-50/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=ROOT.kMagenta+1,
    fill_alpha=0.7,
    marker_size=0,
    legend_description=" ",
    custom_legend=Legend(0, 0, 0, 0, "")
  ),
    
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
  # Sample(
  #   name="QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
  #   file_path=f"{base_path}/backgrounds2018/QCD_Pt_50to80_MuEnriched/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=color_palette_wong[0],
  #   fill_alpha=1.0,
  #   marker_size=0,
  #   legend_description=" ",
  #   custom_legend=Legend(0, 0, 0, 0, "")
  # ),
  # Sample(
  #   name="QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
  #   file_path=f"{base_path}/backgrounds2018/QCD_Pt_80to120_MuEnriched/{skim}/{hist_path}/histograms.root",
  #   type=SampleType.background,
  #   cross_sections=cross_sections,
  #   line_alpha=0,
  #   fill_color=color_palette_wong[0],
  #   fill_alpha=1.0,
  #   marker_size=0,
  #   legend_description=" ",
  #   custom_legend=Legend(0, 0, 0, 0, "")
  # ),
  Sample(
    name="QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_120to170_MuEnriched/{skim}/{hist_path}/histograms.root",
    type=SampleType.background,
    cross_sections=cross_sections,
    line_alpha=0,
    fill_color=color_palette_wong[0],
    fill_alpha=1.0,
    marker_size=0,
    legend_description="QCD (#mu enriched)",
    custom_legend=Legend(legend_max_x-2*legend_width, legend_max_y-4*legend_height, legend_max_x-legend_width, legend_max_y-3*legend_height, "f")
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
    legend_description=" ",
    custom_legend=Legend(0, 0, 0, 0, "")
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
  
  "TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8",
  "TTZZ_TuneCP5_13TeV-madgraph-pythia8",
  "TTZH_TuneCP5_13TeV-madgraph-pythia8",
  
  "ttHToMuMu_M125_TuneCP5_13TeV-powheg-pythia8",
  "ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8",
  
  "ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8",
  
  
  "ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
  "ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
  
  "TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8",
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
  
  
  "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",
  
  "DYJetsToMuMu_M-10to50_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
  "DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
)