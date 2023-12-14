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
    # "nLooseMuons": (3, 9999999),
    # "nLooseDSAMuons": (3, 9999999),
    # "nLooseMuonsAndDSAMuons": (3, 9999999),
    "nLooseElectrons": (0, 0),
    # "nGoodBtaggedJets": (2, 9999999),
    "nGoodMediumBtaggedJets": (1, 9999999),
}