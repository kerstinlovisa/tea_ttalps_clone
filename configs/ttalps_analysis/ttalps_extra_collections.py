extraEventCollections = {
  "TightMuons": {
    "inputCollections": ("Muon",),
    "pt": (30., 9999999.),
    "eta": (-2.4, 2.4),
    "tightId": True,
    # 1=PFIsoVeryLoose, 2=PFIsoLoose, 3=PFIsoMedium, 4=PFIsoTight, 5=PFIsoVeryTight, 6=PFIsoVeryVeryTight
    "pfIsoId": (4, 6),
  },
  "LooseMuons": {
    "inputCollections": ("Muon",),
    "pt": (15., 9999999.),
    "eta": (-2.5, 2.5),
    "looseId": True,
    # 1=PFIsoVeryLoose, 2=PFIsoLoose, 3=PFIsoMedium, 4=PFIsoTight, 5=PFIsoVeryTight, 6=PFIsoVeryVeryTight
    "pfIsoId": (1, 6),
  },

  "LooseElectrons": {
    "inputCollections": ("Electron",),
    "pt": (15., 9999999.),
    "eta": (-2.5, 2.5),
    "mvaFall17V2Iso_WPL": True,
  },
  
  "GoodJets": {
    "inputCollections": ("Jet", ),
    "pt": (30., 9999999.),
    "eta": (-2.4, 2.4),
    # bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto*
    "jetId": 6,
  },
  "GoodBtaggedJets": {
    "inputCollections": ("Jet", ),
    "pt": (30., 9999999.),
    "eta": (-2.4, 2.4),
    "btagDeepFlavB": (0.7100, 9999999.),
    # bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto*
    "jetId": 6,
  },
  "GoodNonBtaggedJets": {
    "inputCollections": ("Jet", ),
    "pt": (30., 9999999.),
    "eta": (-2.4, 2.4),
    "btagDeepFlavB": (0.0, 0.7100),
    # bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto*
    "jetId": 6,
  },
}
