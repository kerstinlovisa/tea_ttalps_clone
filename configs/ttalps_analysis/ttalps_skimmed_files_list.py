max_files = -1

# input_skim = "skimmed_looseSemileptonic"
input_skim = "skimmed_looseSemimuonic_tightMuon"

# output_skim = "skimmed_ttbarLike"
# output_skim = "skimmed_ttbarSemimuonicCR_tightMuon"
output_skim = "skimmed_ttZSemimuonicCR_tightMuon_noLooseMuonIso"

file_name = "C55A6FA8-6732-0046-B89B-2FCB6E264FB2.root"

# input_file_list = ("./skimmed_loose/test_TTToSemileptonic.root",)
# output_dir = f"./skimmed_ttbar/"

base_path = "/nfs/dust/cms/user/jniedzie/ttalps_cms"

samples = (
  # Backgrounds
  # "backgrounds2018/ttZJets",
  # "backgrounds2018/TTZToLLNuNu",
  
  # "backgrounds2018/ttWJets",
  # "backgrounds2018/TTWJetsToLNu",
  # "backgrounds2018/WJetsToLNu",

  # "backgrounds2018/TTToSemiLeptonic",

  # "backgrounds2018/ST_tW_antitop",
  # "backgrounds2018/ST_tW_top",
  # "backgrounds2018/ST_t-channel_antitop",
  # "backgrounds2018/ST_t-channel_top",

  # "backgrounds2018/ttHToMuMu",
  # "backgrounds2018/ttHTobb",

  # "backgrounds2018/DYJetsToMuMu_M-50",
  # "backgrounds2018/DYJetsToMuMu_M-10to50",

  # # QCD
  # "backgrounds2018/QCD_Pt_15to30",
  # "backgrounds2018/QCD_Pt_30to50",
  # "backgrounds2018/QCD_Pt_50to80",
  # "backgrounds2018/QCD_Pt_80to120",
  # "backgrounds2018/QCD_Pt_120to170",
  # "backgrounds2018/QCD_Pt_170to300",
  # "backgrounds2018/QCD_Pt_300to470",
  # "backgrounds2018/QCD_Pt_470to600",
  # "backgrounds2018/QCD_Pt_600to800",
  # "backgrounds2018/QCD_Pt_800to1000",
  # "backgrounds2018/QCD_Pt_1000to1400",
  # "backgrounds2018/QCD_Pt_1400to1800",
  # "backgrounds2018/QCD_Pt_1800to2400",
  # "backgrounds2018/QCD_Pt_2400to3200",
  # "backgrounds2018/QCD_Pt_3200toInf",

  # # QCD mu enhanced
  # "backgrounds2018/QCD_Pt_15to20_MuEnriched",
  # "backgrounds2018/QCD_Pt_20to30_MuEnriched",
  # "backgrounds2018/QCD_Pt_30to50_MuEnriched",
  # "backgrounds2018/QCD_Pt_50to80_MuEnriched",
  # "backgrounds2018/QCD_Pt_80to120_MuEnriched",
  # "backgrounds2018/QCD_Pt_120to170_MuEnriched",
  # "backgrounds2018/QCD_Pt_170to300_MuEnriched",
  # "backgrounds2018/QCD_Pt_300to470_MuEnriched",
  # "backgrounds2018/QCD_Pt_470to600_MuEnriched",
  # "backgrounds2018/QCD_Pt_600to800_MuEnriched",
  # "backgrounds2018/QCD_Pt_800to1000_MuEnriched",
  # "backgrounds2018/QCD_Pt_1000_MuEnriched",


  # # Data
  # "collision_data2018/SingleMuon2018A",
  "collision_data2018/SingleMuon2018B",
  # "collision_data2018/SingleMuon2018C",
  # "collision_data2018/SingleMuon2018D",
)

# this has to be here, otherwise the script will not work:
sample_path = ""

input_directory = f"{base_path}/{sample_path}/{input_skim}"
output_dir = f"{base_path}/{sample_path}/{output_skim}/"