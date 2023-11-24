from scale_factors_config import *
from ttalps_extra_collections import extraEventCollections

nEvents = -1
printEveryNevents = 10000

runDefaultHistograms = True
runTriggerHistograms = False
runPileupHistograms = False

weightsBranchName = "genWeight"

pileupScaleFactorsPath = "/nfs/dust/cms/user/jniedzie/ttalps_cms/pileup_scale_factors.root"
pileupScaleFactorsHistName = "pileup_scale_factors"

applyScaleFactors = {
  "muon": False,
  "muonTrigger": False,
  "pileup": True,
}

defaultHistParams = (
#  collection             variable               bins    xmin    xmax    dir
  ("Event"             , "PV_npvs"              , 300   , 0     , 300   , ""  ),
  ("Event"             , "PV_npvsGood"          , 300   , 0     , 300   , ""  ),
  
  ("Event"              , "nMuon"               , 50    , 0     , 50    , ""  ),
  ("Muon"               , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("Muon"               , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("Muon"               , "dxy"                 , 1600  , -20   , 20    , ""  ),
  ("Muon"               , "dz"                  , 1600  , -20   , 20    , ""  ),
  
  ("Event"              , "nTightMuons"         , 50    , 0     , 50    , ""  ),
  ("TightMuons"         , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("TightMuons"         , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("TightMuons"         , "dxy"                 , 1600  , -20   , 20    , ""  ),
  ("TightMuons"         , "dz"                  , 1600  , -20   , 20    , ""  ),
  ("TightMuons"         , "pfRelIso04_all"      , 2000  , -10   , 10    , ""  ),
  ("TightMuons"         , "pfRelIso03_chg"      , 2000  , -10   , 10    , ""  ),
  ("TightMuons"         , "pfRelIso03_all"      , 2000  , -10   , 10    , ""  ),
  ("TightMuons"         , "tkRelIso"            , 2000  , -10   , 10    , ""  ),
  ("TightMuons"         , "miniPFRelIso_chg"    , 2000  , -10   , 10    , ""  ),
  ("TightMuons"         , "miniPFRelIso_all"    , 2000  , -10   , 10    , ""  ),
  ("TightMuons"         , "jetRelIso"           , 2000  , -10   , 10    , ""  ),

  
  ("Event"              , "nLooseMuons"         , 50    , 0     , 50    , ""  ),
  ("LooseMuons"         , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("LooseMuons"         , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("LooseMuons"         , "dxy"                 , 1600  , -20   , 20    , ""  ),
  ("LooseMuons"         , "dz"                  , 1600  , -20   , 20    , ""  ),
  ("LooseMuons"         , "pfRelIso04_all"      , 2000  , -10   , 10    , ""  ),
  ("LooseMuons"         , "pfRelIso03_chg"      , 2000  , -10   , 10    , ""  ),
  ("LooseMuons"         , "pfRelIso03_all"      , 2000  , -10   , 10    , ""  ),
  ("LooseMuons"         , "tkRelIso"            , 2000  , -10   , 10    , ""  ),
  ("LooseMuons"         , "miniPFRelIso_chg"    , 2000  , -10   , 10    , ""  ),
  ("LooseMuons"         , "miniPFRelIso_all"    , 2000  , -10   , 10    , ""  ),
  ("LooseMuons"         , "jetRelIso"           , 2000  , -10   , 10    , ""  ),
  
  # ("Event"              , "nLooseDSAMuons"      , 50    , 0     , 50    , ""  ),
  # ("LooseDSAMuons"      , "pt"                  , 2000  , 0     , 1000  , ""  ),
  # ("LooseDSAMuons"      , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  # ("LooseDSAMuons"      , "dxy"                 , 1600  , -20   , 20    , ""  ),
  # ("LooseDSAMuons"      , "dz"                  , 1600  , -20   , 20    , ""  ),
  
  ("Event"              , "nElectron"           , 50    , 0     , 50    , ""  ),
  ("Electron"           , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("Electron"           , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("Electron"           , "dxy"                 , 1600  , -20   , 20    , ""  ),
  ("Electron"           , "dz"                  , 1600  , -20   , 20    , ""  ),
  
  ("Event"              , "nLooseElectrons"     , 50    , 0     , 50    , ""  ),
  ("LooseElectrons"     , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("LooseElectrons"     , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("LooseElectrons"     , "dxy"                 , 1600  , -20   , 20    , ""  ),
  ("LooseElectrons"     , "dz"                  , 1600  , -20   , 20    , ""  ),
  
  ("Event"              , "nJet"                , 50    , 0     , 50    , ""  ),
  ("Jet"                , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("Jet"                , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("Jet"                , "phi"                 , 100   , -2.5  , 2.5   , ""  ),
  ("Jet"                , "btagDeepB"           , 200   , -1    , 1     , ""  ),
  
  ("Event"              , "nGoodJets"           , 50    , 0     , 50    , ""  ),
  ("GoodJets"           , "pt"                  , 2000  , 0     , 2000  , ""  ),
  ("GoodJets"           , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("GoodJets"           , "phi"                 , 100   , -2.5  , 2.5   , ""  ),
  ("GoodJets"           , "btagDeepB"           , 200   , -1    , 1     , ""  ),
  ("GoodJets"           , "btagDeepFlavB"       , 200   , -1    , 1     , ""  ),
  
  ("Event"                    , "nGoodMediumBtaggedJets"    , 50    , 0     , 50    , ""  ),
  ("GoodMediumBtaggedJets"    , "pt"                  , 2000  , 0     , 2000  , ""  ),
  ("GoodMediumBtaggedJets"    , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("GoodMediumBtaggedJets"    , "phi"                 , 100   , -2.5  , 2.5   , ""  ),
  ("GoodMediumBtaggedJets"    , "btagDeepB"           , 200   , -1    , 1     , ""  ),
  ("GoodMediumBtaggedJets"    , "btagDeepFlavB"       , 200   , -1    , 1     , ""  ),
  
  ("Event"                    , "nGoodNonTightBtaggedJets" , 50    , 0     , 50    , ""  ),
  ("GoodNonTightBtaggedJets"  , "pt"                  , 2000  , 0     , 2000  , ""  ),
  ("GoodNonTightBtaggedJets"  , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("GoodNonTightBtaggedJets"  , "phi"                 , 100   , -2.5  , 2.5   , ""  ),
  ("GoodNonTightBtaggedJets"  , "btagDeepB"           , 200   , -1    , 1     , ""  ),
  ("GoodNonTightBtaggedJets"  , "btagDeepFlavB"       , 200   , -1    , 1     , ""  ),
)

histParams = (
#  collection         variable                      bins   xmin   xmax    dir
  ("Muon"           , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  ("TightMuons"     , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  ("LooseMuons"     , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  ("Electron"       , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  ("LooseElectrons" , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  ("Jet"            , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  ("GoodJets"       , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  
  ("Muon"           , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  ("TightMuons"     , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  ("LooseMuons"     , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  ("Electron"       , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  ("LooseElectrons" , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  ("Jet"            , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  ("GoodJets"       , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  
  ("LooseMuons"     , "dimuonMinv"                , 200   , 0   , 200   , ""  ),
  ("LooseMuons"     , "dimuonMinvClosestToZ"      , 200   , 0   , 200   , ""  ),
  ("LooseMuons"     , "dimuonDeltaRclosestToZ"    , 200   , -10 , 10    , ""  ),
  ("LooseMuons"     , "dimuonDeltaEtaclosestToZ"  , 200   , -10 , 10    , ""  ),
  ("LooseMuons"     , "dimuonDeltaPhiclosestToZ"  , 200   , -10 , 10    , ""  ),
  ("GoodJets"       , "minvBjet2jets"             , 2000  , 0   , 2000  , ""  ),
  ("TightMuons"     , "deltaPhiMuonMET"           , 200   , -4  , 4     , ""  ),
  ("TightMuons"     , "minvMuonMET"               , 1000  , 0   , 1000  , ""  ),
  
  ("Event"          , "METpt"                     , 1000  , 0   , 1000  , ""  ),
  ("Event"          , "normCheck"                 , 1     , 0   , 1     , ""  ),
)
