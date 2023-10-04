
# option 1: list input files and one output directory
# output files will have the same name as inputs, but be stored the output_dir
# input_file_list = (
#   "../samples/signals/nanoAOD_example.root",
#   "../samples/signals/nanoAOD_example.root"
# )
# output_dir = "../samples/signals/skim"


# option 2: list input files and output files
input_output_file_list = (
  ("/nfs/dust/cms/user/jniedzie/ttalps_cms/signals/tta_mAlp-0p35GeV/skimmed_looseSemileptonic/tta_mAlp-0p35GeV_nEvents-100000.root", 
   "/nfs/dust/cms/user/jniedzie/ttalps_cms/signals/tta_mAlp-0p35GeV/skimmed_ttbarLike/tta_mAlp-0p35GeV_nEvents-100000.root"),
)

# option 3: give DAS dataset name and output path: will run for all files in dataset (or up to max_files)
# dataset = "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
# output_dir = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ttZJets/skimmed_looseSemileptonic/"
# max_files = -1

# option 4: give DAS dataset name, output path and specify a particular file name you want to run on
# dataset = "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
# output_dir = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ttZJets/skimmed_looseSemileptonic/"
# file_name = "AC05C14C-B6AB-4A40-B647-D1F33544B0C0.root"
# file_name = "B3D1B575-8F73-F144-A493-199489FB2692.root"
# max_files = -1

# dataset = "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
# output_dir = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ttZJets/skimmed_looseSemileptonic/"
# file_name = "388501EC-9D5A-A742-B0FE-87D3174835A8.root"
# max_files = -1

# option 5: only specify local input and output directories
# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ttZJets/skimmed_looseSemileptonic"
# output_dir = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ttZJets/skimmed_ttbarLike/"
# max_files = -1

# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ttWJets/skimmed_looseSemileptonic"
# output_dir = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/ttWJets/skimmed_ttbarLike/"
# max_files = -1

# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/TTToSemiLeptonic/skimmed_looseSemileptonic"
# output_dir = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds2018/TTToSemiLeptonic/skimmed_ttbarLike/"
# max_files = -1

# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018A/skimmed_looseSemileptonic"
# output_dir = "/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018A/skimmed_ttbarLike/"
# max_files = -1

# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018B/skimmed_looseSemileptonic"
# output_dir = "/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018B/skimmed_ttbarLike/"
# max_files = -1

# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018C/skimmed_looseSemileptonic"
# output_dir = "/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018C/skimmed_ttbarLike/"
# max_files = -1

# input_directory = "/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018D/skimmed_looseSemileptonic"
# output_dir = "/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data2018/SingleMuon2018D/skimmed_ttbarLike/"
# max_files = -1
