from ttalps_extra_collections import extraEventCollections

nEvents = -1
printEveryNevents = 10000

applyLooseSkimming = False
applyTTbarLikeSkimming = True
applyTTZLikeSkimming = False
applySignalLikeSkimming = False

weightsBranchName = "genWeight"

eventSelections = {
    "MET_pt": (50, 9999999),
    # "nTightMuons": (1, 1), # This is already handled in PassesSingleLeptonSelections
    "nLooseElectrons": (0, 0),
    # "nGoodTightBtaggedJets": (2, 9999999),
    "nGoodMediumBtaggedJets": (1, 9999999),
}
