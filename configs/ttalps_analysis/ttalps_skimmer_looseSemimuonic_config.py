from ttalps_extra_collections import extraEventCollections

nEvents = -1
printEveryNevents = 10000

applyLooseSkimming = True
applyTTbarLikeSkimming = False
applyTTZLikeSkimming = False
applySignalLikeSkimming = False

weightsBranchName = "genWeight"

triggerSelection = (
    "HLT_IsoMu24",
)

eventSelections = {
    "MET_pt": (30, 9999999),
    "nLooseMuons": (1, 9999999),
    "nGoodJets": (4, 9999999),
    "nGoodBtaggedJets": (1, 9999999),
}

requiredFlags = (
    "Flag_goodVertices",
    "Flag_globalSuperTightHalo2016Filter",
    "Flag_HBHENoiseFilter",
    "Flag_HBHENoiseIsoFilter",
    "Flag_EcalDeadCellTriggerPrimitiveFilter",
    "Flag_BadPFMuonFilter",
    "Flag_BadPFMuonDzFilter",
    "Flag_hfNoisyHitsFilter",
    "Flag_eeBadScFilter",
    "Flag_ecalBadCalibFilter",
)