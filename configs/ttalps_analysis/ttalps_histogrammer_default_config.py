nEvents = -1
printEveryNevents = 10000

runDefaultHistograms = True
runTriggerHistograms = False

weightsBranchName = "genWeight"

from ttalps_skimmer_ttbarLike_semimuonic_config import extraEventCollections

extraEventCollections["GoodNonBtaggedJets"] = {
  "inputCollections": ("Jet", ),
  "pt": (30., 9999999.),
  "eta": (-2.4, 2.4),
  "btagDeepB": (0, 0.5),
  "jetId": 6, #  bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto*
}

defaultHistParams = (
#  collection             variable                  bins    xmin     xmax     dir
  ("Event",               "nMuon",                  50,     0,       50,      ""  ),
  ("Muon",                "pt",                     2000,    0,      1000,    ""  ),
  ("Muon",                "eta",                    100,    -2.5,    2.5,     ""  ),
  ("Muon",                "dxy",                    400,    -20,     20,      ""  ),
  ("Muon",                "dz",                     400,    -20,     20,      ""  ),
  
  ("Event",               "nTightMuons",             50,     0,       50,      ""  ),
  ("TightMuons",           "pt",                     2000,    0,      1000,    ""  ),
  ("TightMuons",           "eta",                    100,    -2.5,    2.5,     ""  ),
  ("TightMuons",           "dxy",                    400,    -20,     20,      ""  ),
  ("TightMuons",           "dz",                     400,    -20,     20,      ""  ),
  
  ("Event",               "nLooseMuons",       50,     0,       50,      ""  ),
  ("LooseMuons",           "pt",                     2000,    0,      1000,    ""  ),
  ("LooseMuons",           "eta",                    100,    -2.5,    2.5,     ""  ),
  ("LooseMuons",           "dxy",                    400,    -20,     20,      ""  ),
  ("LooseMuons",           "dz",                     400,    -20,     20,      ""  ),
  
  ("Event",               "nElectron",              50,     0,       50,      ""  ),
  ("Electron",            "pt",                     2000,    0,      1000,    ""  ),
  ("Electron",            "eta",                    100,    -2.5,    2.5,     ""  ),
  ("Electron",            "dxy",                    400,    -20,     20,      ""  ),
  ("Electron",            "dz",                     400,    -20,     20,      ""  ),
  
  ("Event",               "nLooseElectrons",         50,     0,       50,      ""  ),
  ("LooseElectrons",       "pt",                     2000,    0,      1000,    ""  ),
  ("LooseElectrons",       "eta",                    100,    -2.5,    2.5,     ""  ),
  ("LooseElectrons",       "dxy",                    400,    -20,     20,      ""  ),
  ("LooseElectrons",       "dz",                     400,    -20,     20,      ""  ),
  
  ("Event",               "nJet",                   50,     0,       50,      ""  ),
  ("Jet",                 "pt",                     2000,    0,      1000,    ""  ),
  ("Jet",                 "eta",                    100,    -2.5,    2.5,     ""  ),
  ("Jet",                 "phi",                    100,    -2.5,    2.5,     ""  ),
  ("Jet",                 "btagDeepB",              200,    -1,      1,       ""  ),
  
  ("Event",               "nGoodJets",              50,     0,       50,      ""  ),
  ("GoodJets",            "pt",                     2000,    0,      1000,    ""  ),
  ("GoodJets",            "eta",                    100,    -2.5,    2.5,     ""  ),
  ("GoodJets",            "phi",                    100,    -2.5,    2.5,     ""  ),
  ("GoodJets",            "btagDeepB",              200,    -1,      1,       ""  ),
  
  ("Event",               "nGoodBtaggedJets",       50,     0,       50,      ""  ),
  ("GoodBtaggedJets",     "pt",                     2000,    0,      1000,    ""  ),
  ("GoodBtaggedJets",     "eta",                    100,    -2.5,    2.5,     ""  ),
  ("GoodBtaggedJets",     "phi",                    100,    -2.5,    2.5,     ""  ),
  ("GoodBtaggedJets",     "btagDeepB",              200,    -1,      1,       ""  ),
  
  ("Event",               "nGoodNonBtaggedJets",    50,     0,       50,      ""  ),
  ("GoodNonBtaggedJets",  "pt",                     2000,    0,      1000,    ""  ),
  ("GoodNonBtaggedJets",  "eta",                    100,    -2.5,    2.5,     ""  ),
  ("GoodNonBtaggedJets",  "phi",                    100,    -2.5,    2.5,     ""  ),
  ("GoodNonBtaggedJets",  "btagDeepB",              200,    -1,      1,       ""  ),
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
  ("GoodJets"       , "minvBjet2jets"             , 1000  , 0   , 1000  , ""  ),
  ("TightMuons"     , "deltaPhiMuonMET"           , 200   , -4  , 4     , ""  ),
  ("TightMuons"     , "minvMuonMET"               , 1000  , 0   , 1000  , ""  ),
  
  ("Event"          , "METpt"                     , 1000  , 0   , 1000  , ""  ),
  ("Event"          , "normCheck"                 , 1     , 0   , 1     , ""  ),
)
