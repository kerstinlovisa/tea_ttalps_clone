import os

def main():
  
  base_path = "/nfs/dust/cms/user/jniedzie/ttalps_cms"
  
  # skim="ttbarLike"
  #skim="ttZLike"
  skim="skimmed_ttbarSemimuonicCR_tightMuon"
  
  hist_path = "histograms"
  # hist_path = "histograms_noSFs"
  
  input_hists_patterns = (
    f"collision_data2018/SingleMuon2018*/{skim}/{hist_path}/*root",
    f"backgrounds2018/ttZJets/{skim}/{hist_path}/*.root",
    f"backgrounds2018/ttWJets/{skim}/{hist_path}/*.root",
    f"backgrounds2018/TTToSemiLeptonic/{skim}/{hist_path}/*.root",
    f"backgrounds2018/ST_tW_top/{skim}/{hist_path}/*.root",
    f"backgrounds2018/ST_tW_antitop/{skim}/{hist_path}/*.root",
    f"backgrounds2018/ttHToMuMu/{skim}/{hist_path}/*.root",
    f"backgrounds2018/ttHTobb/{skim}/{hist_path}/*.root",
    f"backgrounds2018/ttHTobb/{skim}/{hist_path}/*.root",
    f"backgrounds2018/DYJetsToMuMu_M-50/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_15to30/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_30to50/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_50to80/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_80to120/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_120to170/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_170to300/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_300to470/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_470to600/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_600to800/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_800to1000/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_1000to1400/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_1400to1800/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_1800to2400/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_2400to3200/{skim}/{hist_path}/*.root",
    f"backgrounds2018/QCD_Pt_3200toInf/{skim}/{hist_path}/*.root",
    f"backgrounds2018/ST_t-channel_antitop/{skim}/{hist_path}/*.root",
    f"backgrounds2018/ST_t-channel_top/{skim}/{hist_path}/*.root",
    f"backgrounds2018/TTZToLLNuNu/{skim}/{hist_path}/*.root",
    f"backgrounds2018/TTWJetsToLNu/{skim}/{hist_path}/*.root",
    f"backgrounds2018/WJetsToLNu/{skim}/{hist_path}/*.root",
  )
  
  for input_hists_pattern in input_hists_patterns:
    print(f"{input_hists_pattern=}")
    
    if "collision_data" in input_hists_pattern:
      output_path = f"collision_data2018/SingleMuon2018_{skim}_{hist_path}.root"
    else:
      output_path = input_hists_pattern.replace("*.root", "histograms.root")
    
    print(f"{output_path=}")
    
    os.system(f"rm {base_path}/{output_path}")
    os.system(f"hadd -f -j -k {base_path}/{output_path} {base_path}/{input_hists_pattern}")

if __name__ == "__main__":
  main()
