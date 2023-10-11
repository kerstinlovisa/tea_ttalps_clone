import os
import glob

# dataset = "/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD"
# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018A/skimmed_looseSemileptonic/"

# dataset = "/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"
# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018D/skimmed_ttbarLike/"

# dataset = "/DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/DYJetsToMuMu_M-50/skimmed_ttZLike/"
# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/DYJetsToMuMu_M-50/skimmed_ttbarLike/"

# dataset = "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ST_tW_antitop/skimmed_ttbarLike/"

# dataset = "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ttWJets/skimmed_ttZLike/histograms/"

dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/TTToSemiLeptonic/skimmed_ttZLike/histograms/"

def main():
  print(f"Searching in {input_directory}")
  input_files = glob.glob(input_directory + "/*.root")
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