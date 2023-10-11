nEvents = -1
printEveryNevents = 10000

applyLooseSkimming = False
applyTTbarLikeSkimming = False
applyTTZLikeSkimming = True
applySignalLikeSkimming = False

weightsBranchName = "genWeight"

triggerSelection = (
    "HLT_Ele28_eta2p1_WPTight_Gsf_HT150",
    "HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned",
    "HLT_Ele32_WPTight_Gsf",
    "HLT_IsoMu24",
)

extraEventCollections = {
    "GoodLeptons": {
        "inputCollections": ("Muon", "Electron"),
        "pt": (30., 9999999.),
        "eta": (-2.4, 2.4),
    },
    "GoodJets": {
        "inputCollections": ("Jet", ),
        "pt": (30., 9999999.),
        "eta": (-2.4, 2.4),
    },
    "GoodBtaggedJets": {
        "inputCollections": ("Jet", ),
        "pt": (30., 9999999.),
        "eta": (-2.4, 2.4),
        "btagDeepB": (0.5, 9999999.),
    },
    
    "AlmostGoodMuons": {
        "inputCollections": ("Muon",),
        "pt": (15., 9999999.),
        "eta": (-2.5, 2.5),
    },
    "AlmostGoodLeptons": {
        "inputCollections": ("Muon", "Electron"),
        "pt": (15., 9999999.),
        "eta": (-2.5, 2.5),
    },
}

eventSelections = {
    "MET_pt": (30, 9999999),
    "nGoodLeptons": (1, 9999999),
    "nAlmostGoodMuons": (2, 9999999),
    "nGoodJets": (4, 9999999),
    "nGoodBtaggedJets": (2, 9999999),
}