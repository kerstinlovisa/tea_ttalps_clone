import ttalps_extra_collections as collections

extraEventCollections = collections.extraEventCollections

nEvents = -1
printEveryNevents = 1000

applyLooseSkimming = False
applyTTbarLikeSkimming = False
applyTTZLikeSkimming = False
applySignalLikeSkimming = True

weightsBranchName = "genWeight"

eventSelections = {
    "MET_pt": (50, 9999999),
    "nTightMuons": (1, 9999999),
    "nLooseMuons": (2, 9999999),
    "nLooseElectrons": (0, 0),
    "nGoodBtaggedJets": (1, 9999999),
}