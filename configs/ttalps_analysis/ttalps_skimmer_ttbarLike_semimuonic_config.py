nEvents = -1
printEveryNevents = 1000

applyLooseSkimming = False
applyTTbarLikeSkimming = True
applyTTZLikeSkimming = False
applySignalLikeSkimming = False

weightsBranchName = "genWeight"

triggerSelection = (
    "HLT_Ele28_eta2p1_WPTight_Gsf_HT150",
    "HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned",
    "HLT_Ele32_WPTight_Gsf",
    "HLT_IsoMu24",
)

extraEventCollections = {
    "TightMuons": {
        "inputCollections": ("Muon",),
        "pt": (30., 9999999.),
        "eta": (-2.4, 2.4),
        "tightId": True,
        "pfIsoId": 4, # 1=PFIsoVeryLoose, 2=PFIsoLoose, 3=PFIsoMedium, 4=PFIsoTight, 5=PFIsoVeryTight, 6=PFIsoVeryVeryTight
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
        "btagDeepB": (0.5, 9999999.),
        "jetId": 6, #  bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto*
    },
    "LooseMuons": {
        "inputCollections": ("Muon",),
        "pt": (15., 9999999.),
        "eta": (-2.5, 2.5),
        "looseId": True,
        "pfIsoId": 1, # 1=PFIsoVeryLoose, 2=PFIsoLoose, 3=PFIsoMedium, 4=PFIsoTight, 5=PFIsoVeryTight, 6=PFIsoVeryVeryTight
    },
    "LooseElectrons": {
        "inputCollections": ("Electron",),
        "pt": (15., 9999999.),
        "eta": (-2.5, 2.5),
    },
}

eventSelections = {
    "nTightMuons": (1, 1),
    "nLooseElectrons": (0, 0),
    "nGoodBtaggedJets": (2, 9999999),
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
