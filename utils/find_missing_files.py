import os
import glob

# skim = "skimmed_looseSemileptonic"
# skim = "skimmed_looseSemimuonic_tightMuon"
skim = "skimmed_looseSemimuonic_tightMuon_newBtag"
# skim = "skimmed_ttZSemimuonicCR_tightMuon_noLooseMuonIso"

samples = (
  # ("/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ttZJets/{skim}/"),
  # ("/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ttWJets/{skim}/"),
  # ("/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/TTToSemiLeptonic/{skim}/"),
  # ("/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ST_tW_antitop/{skim}/"),
  # ("/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ST_tW_top/{skim}/"),
  # ("/ttHToMuMu_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ttHToMuMu/{skim}/"),
  # ("/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ttHTobb/{skim}/"),
  # ("/DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/DYJetsToMuMu_M-50/{skim}/"),
  # ("/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_15to30/{skim}/"),
  # ("/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_30to50/{skim}/"),
  # ("/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_50to80/{skim}/"),
  # ("/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_80to120/{skim}/"),
  # ("/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_120to170/{skim}/"),
  # ("/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_170to300/{skim}/"),
  # ("/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_300to470/{skim}/"),
  # ("/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_470to600/{skim}/"),
  # ("/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_600to800/{skim}/"),
  # ("/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_800to1000/{skim}/"),
  # ("/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_1000to1400/{skim}/"),
  # ("/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_1400to1800/{skim}/"),
  # ("/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_1800to2400/{skim}/"),
  # ("/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_2400to3200/{skim}/"),
  # ("/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/QCD_Pt_3200toInf/{skim}/"),
  ("/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD",
   f"/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018A/{skim}/"),
  ("/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD",
   f"/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018B/{skim}/"),
  # ("/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018C/{skim}/"),
  # ("/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD",
  #  f"/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018D/{skim}/"),
)

def main():
  
  for dataset, output_dir in samples:
    print(f"\n\nSearching in {output_dir}")
    input_files = glob.glob(output_dir + "/*.root")
    input_files = [file.split("/")[-1] for file in input_files]

    das_files = os.popen(f"dasgoclient -query='file dataset={dataset}'").read().split("\n")
    
    print(f"DAS path: {'/'.join(das_files[0].split('/')[0:-1])}")
    
    das_files = [file.split("/")[-1] for file in das_files]
    
    for file in das_files:
      if file not in input_files:
        print(file)
  

if __name__ == '__main__':
  main()
  
  
# ./ttalps_skimmer ttalps_skimmer_ttbarLike_config.py /nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/DYJetsToMuMu_M-50/skimmed_looseSemileptonic/2D47004A-E7E8-4A49-9EA2-374FAB2437BA.root /nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/DYJetsToMuMu_M-50/skimmed_ttbarLike/2D47004A-E7E8-4A49-9EA2-374FAB2437BA.root

# ./ttalps_skimmer ttalps_skimmer_ttbarLike_config.py /nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ST_tW_antitop/skimmed_looseSemileptonic/EEA943A9-2FA6-634D-AAAA-66055F00E547.root /nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ST_tW_antitop/skimmed_ttbarLike/EEA943A9-2FA6-634D-AAAA-66055F00E547.root

# ./ttalps_histogrammer ttalps_histogrammer_default_config.py /nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/TTToSemiLeptonic/skimmed_ttZLike/10AE0CA0-AD1E-5A47-8437-B0D867A62B80.root /nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/TTToSemiLeptonic/skimmed_ttZLike/histograms/10AE0CA0-AD1E-5A47-8437-B0D867A62B80.root