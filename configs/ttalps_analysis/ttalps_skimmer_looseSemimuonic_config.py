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

extraEventCollections = {
    "TightMuons": {
        "inputCollections": ("Muon",),
        "pt": (30., 9999999.),
        "eta": (-2.4, 2.4),
        "tightId": True,
        "pfIsoId": (4, 6), # 1=PFIsoVeryLoose, 2=PFIsoLoose, 3=PFIsoMedium, 4=PFIsoTight, 5=PFIsoVeryTight, 6=PFIsoVeryVeryTight
    },
    "LooseMuons": {
        "inputCollections": ("Muon",),
        "pt": (15., 9999999.),
        "eta": (-2.5, 2.5),
        "looseId": True,
        "pfIsoId": (1, 6), # 1=PFIsoVeryLoose, 2=PFIsoLoose, 3=PFIsoMedium, 4=PFIsoTight, 5=PFIsoVeryTight, 6=PFIsoVeryVeryTight
    },
    "GoodJets": {
        "inputCollections": ("Jet", ),
        "pt": (30., 9999999.),
        "eta": (-2.4, 2.4),
        "jetId": 6, #  bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto*
    },
    "GoodBtaggedJets": {
        "inputCollections": ("Jet", ),
        "pt": (30., 9999999.),
        "eta": (-2.4, 2.4),
        # "btagDeepFlavB": (0.7100, 9999999.), # tight Working Point
        "btagDeepFlavB": (0.0490, 9999999.), # loose Working Point
        "jetId": 6, #  bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto*
    },
}

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