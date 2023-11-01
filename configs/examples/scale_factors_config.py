from ScaleFactorsReader import ScaleFactorsReader
scaleFactorsReader = ScaleFactorsReader()

muonSFs = {
  "muonHighPtRecoSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/muon_highPt_recoID.json",
    "NUM_GlobalMuons_DEN_TrackerMuons"
  ),
  
  "muonMidPtRecoSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/NUM_TrackerMuons_DEN_genTracks_Z_abseta_pt.json",
    "NUM_TrackerMuons_DEN_genTracks"
  ),

  "muonLowPtRecoSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/Efficiency_muon_generalTracks_Run2018_UL_trackerMuon.json",
    "NUM_TrackerMuons_DEN_genTracks"
  ),

  "muonLowPtMediumIDSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/Efficiency_muon_trackerMuon_Run2018_UL_ID.json",
    "NUM_MediumID_DEN_TrackerMuons"
  ),

  "muonLowPtSoftIDSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/Efficiency_muon_trackerMuon_Run2018_UL_ID.json",
    "NUM_SoftID_DEN_TrackerMuons"
  ),

  "muonLowPtTightIDSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/Efficiency_muon_trackerMuon_Run2018_UL_ID.json",
    "NUM_TightID_DEN_TrackerMuons"
  ),

  "muonLowPtLooseIDSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/Efficiency_muon_trackerMuon_Run2018_UL_ID.json",
    "NUM_LooseID_DEN_TrackerMuons"
  ),

  "muonMidPtHighPtIDSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/Efficiencies_muon_generalTracks_Z_Run2018_UL_ID.json",
    "NUM_HighPtID_DEN_TrackerMuons"
  ),

  "muonMidPtLooseIDSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/Efficiencies_muon_generalTracks_Z_Run2018_UL_ID.json",
    "NUM_LooseID_DEN_TrackerMuons"
  ),

  "muonMidPtMediumIDSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/Efficiencies_muon_generalTracks_Z_Run2018_UL_ID.json",
    "NUM_MediumID_DEN_TrackerMuons"
  ),

  "muonMidPtMediumPromptIDSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/Efficiencies_muon_generalTracks_Z_Run2018_UL_ID.json",
    "NUM_MediumPromptID_DEN_TrackerMuons"
  ),

  "muonMidPtSoftIDSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/Efficiencies_muon_generalTracks_Z_Run2018_UL_ID.json",
    "NUM_SoftID_DEN_TrackerMuons"
  ),

  "muonMidPtTightIDSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/Efficiencies_muon_generalTracks_Z_Run2018_UL_ID.json",
    "NUM_TightID_DEN_TrackerMuons"
  ),

  "muonMidPtTrkHighPtIDSFs": scaleFactorsReader.getMuonScaleFactors(
    "../data/Efficiencies_muon_generalTracks_Z_Run2018_UL_ID.json",
    "NUM_TrkHighPtID_DEN_TrackerMuons"
  ),
}
