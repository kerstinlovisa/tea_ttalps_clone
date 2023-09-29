nEvents = -1
printEveryNevents = 100

inputFilePath = "../samples/signals/nanoAOD_example.root"
treeOutputFilePath = "../samples/signals/loose_skim/nanoAOD_example.root"

weightsBranchName = "genWeight"

triggerSelection = (
    "HLT_IsoMu24",
)

extraEventCollections = {
    "GoodLeptons": {
        "inputCollections": ("Muon", "Electron"),
        "pt": (30., 9999999.),
        "eta": (-2.4, 2.4),
    },
}

eventSelections = {
    "MET_pt": (30, 9999999),
    "nMuon": (1, 9999999),
    "nGoodLeptons": (1, 9999999),
}