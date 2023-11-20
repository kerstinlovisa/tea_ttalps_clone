from ttalps_extra_collections import extraEventCollections

nEvents = -1
printEveryNevents = 1000

applyLooseSkimming = False
applyTTbarLikeSkimming = True
applyTTZLikeSkimming = False
applySignalLikeSkimming = False

weightsBranchName = "genWeight"

eventSelections = {
    "MET_pt": (50, 9999999),
    "nTightMuons": (1, 1),
    "nLooseElectrons": (0, 0),
    "nGoodBtaggedJets": (2, 9999999),
}
