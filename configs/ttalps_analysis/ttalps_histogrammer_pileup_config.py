from scale_factors_config import *

nEvents = -1
printEveryNevents = 10000

runDefaultHistograms = False
runTriggerHistograms = False
runPileupHistograms = True

weightsBranchName = "genWeight"

pileupScaleFactorsPath = "../data/pileup/pileup_scale_factors.root"
pileupScaleFactorsHistName = "pileup_scale_factors"

applyScaleFactors = {
  "muon": False,
  "muonTrigger": False,
  "pileup": False,
}

defaultHistParams = (
#  collection             variable               bins    xmin    xmax    dir
  ("Event"             , "PV_npvs"              , 300   , 0     , 300   , ""  ),
  ("Event"             , "PV_npvsGood"          , 300   , 0     , 300   , ""  ),
)
