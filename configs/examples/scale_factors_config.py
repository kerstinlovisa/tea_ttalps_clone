from ScaleFactorsReader import ScaleFactorsReader
scaleFactorsReader = ScaleFactorsReader()

muonSFs = {
  # Reco SFs
  **scaleFactorsReader.getMuonScaleFactors("../data/muon_highPt_recoID.json"),
  **scaleFactorsReader.getMuonScaleFactors("../data/NUM_TrackerMuons_DEN_genTracks_Z_abseta_pt.json"),
  **scaleFactorsReader.getMuonScaleFactors("../data/Efficiency_muon_generalTracks_Run2018_UL_trackerMuon.json"),
  
  # ID SFs
  **scaleFactorsReader.getMuonScaleFactors("../data/Efficiency_muon_trackerMuon_Run2018_UL_ID.json"),
  **scaleFactorsReader.getMuonScaleFactors("../data/Efficiencies_muon_generalTracks_Z_Run2018_UL_ID.json"),
  
  # Iso SFs
  **scaleFactorsReader.getMuonScaleFactors("../data/Efficiencies_muon_generalTracks_Z_Run2018_UL_ISO.json"),
}

print("Loaded SFs:")
for name in muonSFs.keys():
  print(name)
