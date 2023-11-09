import os

def main():
  
  base_path = "/nfs/dust/cms/user/jniedzie/ttalps_cms"
  
  # skim="ttbarLike"
  #skim="ttZLike"
  # skim="skimmed_ttbarSemimuonicCR_tightMuon"
  skim="skimmed_ttZSemimuonicCR_tightMuon_noLooseMuonIso"
  
  # hist_path = "histograms"
  # hist_path = "histograms_noSFs"
  hist_path = "histograms_noTriggerSFs"
  
  sample_paths = (
    "backgrounds2018/ttZJets",
    "backgrounds2018/TTZToLLNuNu",
    
    "backgrounds2018/ttWJets",
    "backgrounds2018/TTWJetsToLNu",
    "backgrounds2018/WJetsToLNu",
    
    "backgrounds2018/TTToSemiLeptonic",
    
    "backgrounds2018/ST_tW_top",
    "backgrounds2018/ST_tW_antitop",
    "backgrounds2018/ST_t-channel_antitop",
    "backgrounds2018/ST_t-channel_top",
    
    "backgrounds2018/ttHToMuMu",
    "backgrounds2018/ttHTobb",
    
    "backgrounds2018/DYJetsToMuMu_M-50",
    "backgrounds2018/DYJetsToMuMu_M-10to50",
    
    "backgrounds2018/QCD_Pt_15to30",
    "backgrounds2018/QCD_Pt_30to50",
    "backgrounds2018/QCD_Pt_50to80",
    "backgrounds2018/QCD_Pt_80to120",
    "backgrounds2018/QCD_Pt_120to170",
    "backgrounds2018/QCD_Pt_170to300",
    "backgrounds2018/QCD_Pt_300to470",
    "backgrounds2018/QCD_Pt_470to600",
    "backgrounds2018/QCD_Pt_600to800",
    "backgrounds2018/QCD_Pt_800to1000",
    "backgrounds2018/QCD_Pt_1000to1400",
    "backgrounds2018/QCD_Pt_1400to1800",
    "backgrounds2018/QCD_Pt_1800to2400",
    "backgrounds2018/QCD_Pt_2400to3200",
    "backgrounds2018/QCD_Pt_3200toInf",
    
    "backgrounds2018/QCD_Pt_15to20_MuEnriched",
    "backgrounds2018/QCD_Pt_20to30_MuEnriched",
    "backgrounds2018/QCD_Pt_30to50_MuEnriched",
    "backgrounds2018/QCD_Pt_50to80_MuEnriched",
    "backgrounds2018/QCD_Pt_80to120_MuEnriched",
    "backgrounds2018/QCD_Pt_120to170_MuEnriched",
    "backgrounds2018/QCD_Pt_170to300_MuEnriched",
    "backgrounds2018/QCD_Pt_300to470_MuEnriched",
    "backgrounds2018/QCD_Pt_470to600_MuEnriched",
    "backgrounds2018/QCD_Pt_600to800_MuEnriched",
    "backgrounds2018/QCD_Pt_800to1000_MuEnriched",
    "backgrounds2018/QCD_Pt_1000_MuEnriched",
    
    "collision_data2018/SingleMuon2018*",
  )
  
  for sample_path in sample_paths:
    print(f"{sample_path=}")
    
    input_path = f"{sample_path}/{skim}/{hist_path}/*.root"
    
    if "collision_data" in input_path:
      output_path = f"collision_data2018/SingleMuon2018_{skim}_{hist_path}.root"
    else:
      output_path = input_path.replace("*.root", "histograms.root")
    
    print(f"{output_path=}")
    
    os.system(f"rm {base_path}/{output_path}")
    os.system(f"hadd -f -j -k {base_path}/{output_path} {base_path}/{input_path}")

if __name__ == "__main__":
  main()
