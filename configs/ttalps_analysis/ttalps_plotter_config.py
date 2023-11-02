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
# skim = "skimmed_ttbarLike"
# skim = "skimmed_ttZLike"
skim = "skimmed_ttbarSemimuonicCR_tightMuon"

# luminosity = 63670. # pb^-1
luminosity = 59830. # recommended lumi from https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2

legends = {
  SampleType.signal: Legend(0.35, 0.85, 0.5, 0.89, "l"),
  SampleType.background: Legend(0.7, 0.35, 0.85, 0.89, "f"),
  SampleType.data: Legend(0.30, 0.8, 0.5, 0.85, "pl"),
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

histograms = (
#           name                                title logy    norm_type                 rebin xmin  xmax    ymin    ymax,   xlabel                                        ylabel
  Histogram("Event_nTightMuons"                 , "", True  , NormalizationType.to_lumi, 1  , 0     , 10    , 1e1   , 1e9   , "Number of loose #mu"                       , "# events (2018)"   ),
  Histogram("TightMuons_pt"                     , "", True  , NormalizationType.to_lumi, 50 , 0     , 1000  , 1e-5  , 1e4   , "tight #mu p_{T} [GeV]"                     , "# events (2018)"   ),
  Histogram("TightMuons_leadingPt"              , "", True  , NormalizationType.to_lumi, 50 , 0     , 1000  , 1e-5  , 1e4   , "leading tight #mu p_{T} [GeV]"             , "# events (2018)"   ),
  Histogram("TightMuons_subleadingPt"           , "", True  , NormalizationType.to_lumi, 50 , 0     , 1000  , 1e-5  , 1e4   , "all subleading tight #mu p_{T} [GeV]"      , "# events (2018)"   ),
  Histogram("TightMuons_eta"                    , "", True  , NormalizationType.to_lumi, 5  , -3.5  , 3.5   , 1e0   , 1e6   , "tight #mu #eta"                            , "# events (2018)"   ),
  Histogram("TightMuons_dxy"                    , "", True  , NormalizationType.to_lumi, 1  , -0.5  , 0.5   , 1e-2  , 1e6   , "tight #mu d_{xy} [cm]"                     , "# events (2018)"   ),
  Histogram("TightMuons_dz"                     , "", True  , NormalizationType.to_lumi, 1  , -1    , 1     , 1e-2  , 1e6   , "tight #mu d_{z} [cm]"                      , "# events (2018)"   ),
  
  Histogram("Event_nLooseMuons"                 , "", True  , NormalizationType.to_lumi, 1  , 0     , 10    , 1e1   , 1e9   , "Number of loose #mu"                       , "# events (2018)"   ),
  Histogram("LooseMuons_pt"                     , "", True  , NormalizationType.to_lumi, 20 , 0     , 500   , 1e-2  , 1e6   , "loose #mu p_{T} [GeV]"                     , "# events (2018)"   ),
  Histogram("LooseMuons_leadingPt"              , "", True  , NormalizationType.to_lumi, 20 , 0     , 500   , 1e-2  , 1e6   , "leading loose #mu p_{T} [GeV]"             , "# events (2018)"   ),
  Histogram("LooseMuons_subleadingPt"           , "", True  , NormalizationType.to_lumi, 20 , 0     , 500   , 1e-2  , 1e6   , "all subleading loose #mu p_{T} [GeV]"      , "# events (2018)"   ),
  Histogram("LooseMuons_eta"                    , "", True  , NormalizationType.to_lumi, 5  , -3.5  , 3.5   , 1e0   , 1e6   , "loose #mu #eta"                            , "# events (2018)"   ),
  Histogram("LooseMuons_dxy"                    , "", True  , NormalizationType.to_lumi, 2  , -10   , 10    , 1e-2  , 1e6   , "loose #mu d_{xy} [cm]"                     , "# events (2018)"   ),
  Histogram("LooseMuons_dz"                     , "", True  , NormalizationType.to_lumi, 2  , -10   , 10    , 1e-2  , 1e6   , "loose #mu d_{z} [cm]"                      , "# events (2018)"   ),
  
  Histogram("Event_nLooseElectrons"             , "", True  , NormalizationType.to_lumi, 1  , 0     , 10    , 1e1   , 1e9   , "Number of loose electrons"                 , "# events (2018)"   ),
  Histogram("LooseElectrons_pt"                 , "", True  , NormalizationType.to_lumi, 10 , 0     , 500   , 1e-2  , 1e6   , "loose electron p_{T} [GeV]"                , "# events (2018)"   ),
  Histogram("LooseElectrons_leadingPt"          , "", True  , NormalizationType.to_lumi, 10 , 0     , 500   , 1e-2  , 1e6   , "leading loose electron p_{T} [GeV]"        , "# events (2018)"   ),
  Histogram("LooseElectrons_subleadingPt"       , "", True  , NormalizationType.to_lumi, 10 , 0     , 500   , 1e-2  , 1e6   , "all subleading loose electron p_{T} [GeV]" , "# events (2018)"   ),
  Histogram("LooseElectrons_eta"                , "", True  , NormalizationType.to_lumi, 5  , -3.5  , 3.5   , 1e-2  , 1e6   , "loose electron #eta"                       , "# events (2018)"   ),
  Histogram("LooseElectrons_dxy"                , "", True  , NormalizationType.to_lumi, 10 , -10   , 10    , 1e-2  , 1e6   , "loose electron d_{xy}"                     , "# events (2018)"   ),
  Histogram("LooseElectrons_dz"                 , "", True  , NormalizationType.to_lumi, 10 , -10   , 10    , 1e-2  , 1e6   , "loose electron d_{z}"                      , "# events (2018)"   ),
  
  Histogram("Event_nGoodJets"                   , "", True  , NormalizationType.to_lumi, 1  , 0     , 20    , 1e0   , 1e9   , "Number of good jets"                       , "# events (2018)"   ),
  Histogram("GoodJets_pt"                       , "", True  , NormalizationType.to_lumi, 50 , 0     , 2000  , 1e-5  , 1e4   , "good jet p_{T} [GeV]"                      , "# events (2018)"   ),
  Histogram("GoodJets_eta"                      , "", True  , NormalizationType.to_lumi, 5  , -3.5  , 3.5   , 1e0   , 1e10  , "good jet #eta"                             , "# events (2018)"   ),
  Histogram("GoodJets_btagDeepB"                , "", True  , NormalizationType.to_lumi, 10 , -1    , 1     , 1e0   , 1e8   , "good jet btagDeepB"                        , "# events (2018)"   ),
  
  Histogram("Event_nGoodBtaggedJets"            , "", True  , NormalizationType.to_lumi, 1  , 0     , 20    , 1e0   , 1e9   , "Number of good b-jets"                     , "# events (2018)"   ),
  Histogram("GoodBtaggedJets_pt"                , "", True  , NormalizationType.to_lumi, 50 , 0     , 2000  , 1e-5  , 1e4   , "good b-jet p_{T} [GeV]"                    , "# events (2018)"   ),
  Histogram("GoodBtaggedJets_eta"               , "", True  , NormalizationType.to_lumi, 5  , -3.5  , 3.5   , 1e0   , 1e10  , "good b-jet #eta"                           , "# events (2018)"   ),
  Histogram("GoodBtaggedJets_btagDeepB"         , "", True  , NormalizationType.to_lumi, 10 , -1    , 1     , 1e0   , 1e8   , "good b-jet btagDeepB"                      , "# events (2018)"   ),
  
  Histogram("Event_nGoodNonBtaggedJets"         , "", True  , NormalizationType.to_lumi, 1  , 0     , 20    , 1e0   , 1e9   , "Number of good non-b jets"                 , "# events (2018)"   ),
  Histogram("GoodNonBtaggedJets_pt"             , "", True  , NormalizationType.to_lumi, 50 , 0     , 2000  , 1e-5  , 1e4   , "good non-b jet p_{T} [GeV]"                , "# events (2018)"   ),
  Histogram("GoodNonBtaggedJets_eta"            , "", True  , NormalizationType.to_lumi, 5  , -3.5  , 3.5   , 1e0   , 1e10  , "good non-b jet #eta"                       , "# events (2018)"   ),
  Histogram("GoodNonBtaggedJets_btagDeepB"      , "", True  , NormalizationType.to_lumi, 10 , -1    , 1     , 1e0   , 1e8   , "good non-b jet btagDeepB"                  , "# events (2018)"   ),
  
  Histogram("Event_METpt"                       , "", True  , NormalizationType.to_lumi, 40 , 0     , 1000  , 1e-3  , 2e3   , "MET p_{T} [GeV]"                           , "# events (2018)"   ),
  Histogram("LooseMuons_dimuonMinv"             , "", True  , NormalizationType.to_lumi, 1  , 70    , 110   , 1e0   , 1e6   , "loose muons m_{#mu#mu} [GeV]"              , "# events (2018)"   ),
  Histogram("LooseMuons_dimuonMinvClosestToZ"   , "", True  , NormalizationType.to_lumi, 1  , 70    , 110   , 1e0   , 1e6   , "loose muons closest to Z m_{#mu#mu} [GeV]" , "# events (2018)"   ),
  Histogram("LooseMuons_dimuonDeltaRclosestToZ" , "", True  , NormalizationType.to_lumi, 1  , -1    , 6     , 1e0   , 1e5   , "loose muons closest to Z #Delta R_{#mu#mu}", "# events (2018)"   ),
  Histogram("TightMuons_deltaPhiMuonMET"        , "", True  , NormalizationType.to_lumi, 20 , -4    , 4     , 1e0   , 1e7   , "tight muon #Delta #phi(MET, #mu)"          , "# events (2018)"   ),
  Histogram("TightMuons_minvMuonMET"            , "", True  , NormalizationType.to_lumi, 40 , 0     , 2000  , 1e-4  , 2e3   , "tight muon m_{MET, l} [GeV]"               , "# events (2018)"   ),
  Histogram("GoodJets_minvBjet2jets"            , "", True  , NormalizationType.to_lumi, 30 , 0     , 1500  , 1e-1  , 1e5   , "good jets m_{bjj} [GeV]"                   , "# events (2018)"   ),
  
  Histogram("cutFlow"                           , "", True  , NormalizationType.to_lumi, 1  , 0     , 12    , 1e2   , 1e11  , "Selection"                                 , "Number of events"  ),
  Histogram("Event_normCheck"                   , "", True  , NormalizationType.to_lumi, 1  , 0     , 1     , 1e-2  , 1e7   , "norm check"                                , "# events (2018)"   ),
)

weightsBranchName = "genWeight"

samples = (
  Sample(
    name="SingleMuon2018",
    file_path=f"{base_path}/collision_data2018/SingleMuon2018_{skim}_histograms.root",
    type=SampleType.data,
    cross_section=1,
    line_alpha=1,
    fill_alpha=0,
    marker_size=0.7,
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
    fill_color=ROOT.kMagenta,
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
    fill_color=ROOT.kPink - 4,
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
    fill_color=ROOT.kOrange,
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
    fill_color=ROOT.kBlue,
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
    fill_color=ROOT.kAzure - 3,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ST_tW_antitop",
  ),
  Sample(
    name="TTToSemiLeptonic",
    file_path=f"{base_path}/backgrounds2018/TTToSemiLeptonic/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=365.34,
    line_alpha=0,
    fill_color=ROOT.kRed-2,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="TTToSemiLeptonic",
  ),
  Sample(
    name="qcd_120to170",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_120to170/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=406800.0,
    line_alpha=0,
    fill_color=ROOT.kGreen-4,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="QCD pt = 120to170 GeV",
  ),
  Sample(
    name="qcd_170to300",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_170to300/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=103300.0,
    line_alpha=0,
    fill_color=ROOT.kGreen-3,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="QCD pt = 170to300 GeV",
  ),
  Sample(
    name="qcd_300to470",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_300to470/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=6826.0,
    line_alpha=0,
    fill_color=ROOT.kGreen-2,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="QCD pt = 300to470 GeV",
  ),
  Sample(
    name="qcd_470to600",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_470to600/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=552.6,
    line_alpha=0,
    fill_color=ROOT.kGreen,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="QCD pt = 470to600 GeV",
  ),
  Sample(
    name="qcd_600to800",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_600to800/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=156.6,
    line_alpha=0,
    fill_color=ROOT.kGreen+2,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="QCD pt = 600to800 GeV",
  ),
  Sample(
    name="qcd_800to1000",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_800to1000/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=26.32,
    line_alpha=0,
    fill_color=ROOT.kGreen+3,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="QCD pt = 800to1000 GeV",
  ),
  Sample(
    name="qcd_1000to1400",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_1000to1400/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=7.5,
    line_alpha=0,
    fill_color=ROOT.kGreen+4,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="QCD pt = 1000to1400 GeV",
  ),
  Sample(
    name="qcd_1400to1800",
    file_path=f"{base_path}/backgrounds2018/QCD_Pt_1400to1800/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=0.6479,
    line_alpha=0,
    fill_color=ROOT.kGreen+4,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="QCD pt = 1400to1800 GeV",
  ),
  Sample(
    name="top_t_channel",
    file_path=f"{base_path}/backgrounds2018/ST_t-channel_top/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=115.3,
    line_alpha=0,
    fill_color=ROOT.kAzure - 4,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="t-channel top",
  ),
  Sample(
    name="antitop_t_channel",
    file_path=f"{base_path}/backgrounds2018/ST_t-channel_antitop/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=69.09,
    line_alpha=0,
    fill_color=ROOT.kAzure + 3,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="t-channel antitop",
  ),
  Sample(
    name="ttz_llnunu",
    file_path=f"{base_path}/backgrounds2018/TTZToLLNuNu/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=0.2439,
    line_alpha=0,
    fill_color=ROOT.kYellow,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttZ, ll#nu#nu",
  ),
  Sample(
    name="ttw_jets_lnu",
    file_path=f"{base_path}/backgrounds2018/TTWJetsToLNu/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=0.2163,
    line_alpha=0,
    fill_color=ROOT.kBlue-2,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="ttW+jets, l#nu",
  ),
  Sample(
    name="w_jets_l_nu",
    file_path=f"{base_path}/backgrounds2018/WJetsToLNu/{skim}/histograms/histograms.root",
    type=SampleType.background,
    cross_section=52850.0,
    line_alpha=0,
    fill_color=ROOT.kTeal,
    fill_alpha=0.7,
    marker_size=0,
    legend_description="W+jets, l#nu",
  ),
)