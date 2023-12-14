from scale_factors_config import *

nEvents = -1
printEveryNevents = 1000

inputFilePath = "../samples/background_dy.root"
histogramsOutputFilePath = "../samples/histograms/background_dy.root"

extraEventCollections = {
    "GoodLeptons": {
        "inputCollections": ("Muon", "Electron"),
        "pt": (30., 9999999.),
        "eta": (-2.4, 2.4),
    },
}

defaultHistParams = (
#  collection      variable          bins    xmin     xmax     dir
  ("Event"       , "nMuon"         , 50,     0,       50,      ""  ),
  ("Muon"        , "pt"            , 400,    0,       200,     ""  ),
  ("Muon"        , "eta"           , 100,    -2.5,    2.5,     ""  ),
  ("Event"       , "nGoodLeptons"  , 50,     0,       50,      ""  ),
  ("GoodLeptons" , "pt"            , 400,    0,       200,     ""  ),
  ("GoodLeptons" , "eta"           , 100,    -2.5,    2.5,     ""  ),
)

histParams = (
  ("Muon", "scaledPt", 400, 0, 200, ""),
)

weightsBranchName = "genWeight"

pileupScaleFactorsPath = "../data/pileup/pileup_scale_factors.root"
pileupScaleFactorsHistName = "pileup_scale_factors"

applyScaleFactors = {
  "muon": False,
  "muonTrigger": False,
  "pileup": True,
}
