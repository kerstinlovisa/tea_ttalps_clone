
# option 1: list input files and one output directory
# output files will have the same name as inputs, but be stored the output_dir
# input_file_list = (
#   "../samples/signals/nanoAOD_example.root",
#   "../samples/signals/nanoAOD_example.root"
# )
# output_dir = "../samples/signals/skim"


# option 2: list input files and output files
input_output_file_list = (
  ("../samples/signals/nanoAOD_example.root", "../samples/signals/skim/nanoAOD_example.root"),
  ("../samples/backgrounds/nanoAOD_example.root", "../samples/backgrounds/skim/nanoAOD_example.root"),
)

# option 3: give DAS dataset name and output path: will run for all files in dataset (or up to max_files)
# dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"
# output_dir = "../samples/backgrounds/skim"
# max_files = 10

