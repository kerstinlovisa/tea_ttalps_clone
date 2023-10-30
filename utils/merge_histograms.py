import os

def main():
  
  base_path = "/nfs/dust/cms/user/jniedzie/ttalps_cms"
  
  # skim="ttbarLike"
  #skim="ttZLike"
  skim="skimmed_ttbarSemimuonicCR_tightMuon"
  
  output_paths = (
    f"collision_data2018/SingleMuon2018_{skim}_histograms.root",
    f"backgrounds2018/ttZJets/{skim}/histograms/histograms.root",
    f"backgrounds2018/ttWJets/{skim}/histograms/histograms.root",
    f"backgrounds2018/TTToSemiLeptonic/{skim}/histograms/histograms.root",
    f"backgrounds2018/ST_tW_top/{skim}/histograms/histograms.root",
    f"backgrounds2018/ST_tW_antitop/{skim}/histograms/histograms.root",
    f"backgrounds2018/ttHToMuMu/{skim}/histograms/histograms.root",
    f"backgrounds2018/ttHTobb/{skim}/histograms/histograms.root",
    f"backgrounds2018/DYJetsToMuMu_M-50/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_15to30/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_30to50/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_50to80/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_80to120/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_120to170/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_170to300/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_300to470/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_470to600/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_600to800/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_800to1000/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_1000to1400/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_1400to1800/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_1800to2400/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_2400to3200/{skim}/histograms/histograms.root",
    f"backgrounds2018/QCD_Pt_3200toInf/{skim}/histograms/histograms.root",
    f"backgrounds2018/ST_t-channel_antitop/{skim}/histograms/histograms.root",
    f"backgrounds2018/ST_t-channel_top/{skim}/histograms/histograms.root",
    f"backgrounds2018/TTZToLLNuNu/{skim}/histograms/histograms.root",
    f"backgrounds2018/TTWJetsToLNu/{skim}/histograms/histograms.root",
    f"backgrounds2018/WJetsToLNu/{skim}/histograms/histograms.root",
  )
  
  input_hists_patterns = (
    f"collision_data2018/SingleMuon2018*/{skim}/histograms/*root",
    f"backgrounds2018/ttZJets/{skim}/histograms/*.root",
    f"backgrounds2018/ttWJets/{skim}/histograms/*.root",
    f"backgrounds2018/TTToSemiLeptonic/{skim}/histograms/*.root",
    f"backgrounds2018/ST_tW_top/{skim}/histograms/*.root",
    f"backgrounds2018/ST_tW_antitop/{skim}/histograms/*.root",
    f"backgrounds2018/ttHToMuMu/{skim}/histograms/*.root",
    f"backgrounds2018/ttHTobb/{skim}/histograms/*.root",
    f"backgrounds2018/ttHTobb/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_15to30/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_30to50/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_50to80/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_80to120/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_120to170/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_170to300/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_300to470/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_470to600/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_600to800/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_800to1000/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_1000to1400/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_1400to1800/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_1800to2400/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_2400to3200/{skim}/histograms/*.root",
    f"backgrounds2018/QCD_Pt_3200toInf/{skim}/histograms/*.root",
    f"backgrounds2018/ST_t-channel_antitop/{skim}/histograms/*.root",
    f"backgrounds2018/ST_t-channel_top/{skim}/histograms/*.root",
    f"backgrounds2018/TTZToLLNuNu/{skim}/histograms/*.root",
    f"backgrounds2018/TTWJetsToLNu/{skim}/histograms/*.root",
    f"backgrounds2018/WJetsToLNu/{skim}/histograms/*.root",
  )
  
  for output_path, input_hists_pattern in zip(output_paths, input_hists_patterns):
    os.system(f"rm {base_path}/{output_path}")
    os.system(f"hadd -f -j -k {base_path}/{output_path} {base_path}/{input_hists_pattern}")

if __name__ == "__main__":
  main()
