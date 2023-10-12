nEvents = -1
printEveryNevents = 10000

runDefaultHistograms = True
runTriggerHistograms = False

weightsBranchName = "genWeight"

from ttalps_skimmer_looseSemileptonic_config import extraEventCollections

extraEventCollections["GoodMuons"] = {
  "inputCollections": ("Muon",),
  "pt": (30., 9999999.),
  "eta": (-2.4, 2.4),
}

extraEventCollections["AlmostGoodMuons"] = {
  "inputCollections": ("Muon",),
  "pt": (15., 9999999.),
  "eta": (-2.5, 2.5),
}

extraEventCollections["GoodElectrons"] = {
  "inputCollections": ("Electron",),
  "pt": (30., 9999999.),
  "eta": (-2.4, 2.4),
}

extraEventCollections["GoodNonBtaggedJets"] = {
  "inputCollections": ("Jet", ),
  "pt": (30., 9999999.),
  "eta": (-2.4, 2.4),
  "btagDeepB": (0, 0.5),
}

defaultHistParams = (
#  collection             variable                  bins    xmin     xmax     dir
  ("Event",               "nMuon",                  50,     0,       50,      ""  ),
  ("Muon",                "pt",                     2000,    0,      1000,    ""  ),
  ("Muon",                "eta",                    100,    -2.5,    2.5,     ""  ),
  ("Muon",                "dxy",                    400,    -20,     20,      ""  ),
  ("Muon",                "dz",                     400,    -20,     20,      ""  ),
  
  ("Event",               "nGoodMuons",             50,     0,       50,      ""  ),
  ("Event",               "nAlmostGoodMuons",       50,     0,       50,      ""  ),
  ("GoodMuons",           "pt",                     2000,    0,      1000,    ""  ),
  ("GoodMuons",           "eta",                    100,    -2.5,    2.5,     ""  ),
  ("GoodMuons",           "dxy",                    400,    -20,     20,      ""  ),
  ("GoodMuons",           "dz",                     400,    -20,     20,      ""  ),
  
  ("Event",               "nElectron",              50,     0,       50,      ""  ),
  ("Electron",            "pt",                     2000,    0,      1000,    ""  ),
  ("Electron",            "eta",                    100,    -2.5,    2.5,     ""  ),
  ("Electron",            "dxy",                    400,    -20,     20,      ""  ),
  ("Electron",            "dz",                     400,    -20,     20,      ""  ),
  
  ("Event",               "nGoodElectrons",         50,     0,       50,      ""  ),
  ("GoodElectrons",       "pt",                     2000,    0,      1000,    ""  ),
  ("GoodElectrons",       "eta",                    100,    -2.5,    2.5,     ""  ),
  ("GoodElectrons",       "dxy",                    400,    -20,     20,      ""  ),
  ("GoodElectrons",       "dz",                     400,    -20,     20,      ""  ),
  
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
#  collection             variable                  bins    xmin     xmax     dir
  ("Muon",                "leadingPt",              2000,   0,       1000,    ""  ),
  ("GoodMuons",           "leadingPt",              2000,   0,       1000,    ""  ),
  ("Electron",            "leadingPt",              2000,   0,       1000,    ""  ),
  ("GoodElectrons",       "leadingPt",              2000,   0,       1000,    ""  ),
  ("Jet",                 "leadingPt",              2000,   0,       1000,    ""  ),
  ("GoodJets",            "leadingPt",              2000,   0,       1000,    ""  ),
  
  ("Muon",                "subleadingPt",           2000,   0,       1000,    ""  ),
  ("GoodMuons",           "subleadingPt",           2000,   0,       1000,    ""  ),
  ("Electron",            "subleadingPt",           2000,   0,       1000,    ""  ),
  ("GoodElectrons",       "subleadingPt",           2000,   0,       1000,    ""  ),
  ("Jet",                 "subleadingPt",           2000,   0,       1000,    ""  ),
  ("GoodJets",            "subleadingPt",           2000,   0,       1000,    ""  ),
  
  ("AlmostGoodMuons",     "dimuonMinv",             200,    0,       200,     ""  ),
  ("AlmostGoodMuons",     "dimuonMinvClosestToZ",   200,    0,       200,     ""  ),
  ("AlmostGoodMuons",     "dimuonDeltaRclosestToZ", 200,   -10,        10,    ""  ),
  ("GoodJets",            "minvBjet2jets",          1000,   0,       1000,    ""  ),
  ("GoodLeptons",         "deltaPhiLeptonMET",      200,   -4,       4,       ""  ),
  ("GoodLeptons",         "minvLeptonMET",          1000,   0,       1000,    ""  ),
  
  ("Event",               "METpt",                  1000,   0,       1000,    ""  ),
  ("Event",               "normCheck",              1,      0,       1,       ""  ),
)
