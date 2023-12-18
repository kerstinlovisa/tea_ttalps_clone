max_files = -1

# Loose skims
# input_skim = "skimmed_looseSemileptonic"
# input_skim = "skimmed_looseSemimuonic_tightMuon"
# input_skim = "skimmed_looseSemimuonic_tightMuon_newBtag"
input_skim = "skimmed_looseSemimuonic"
# input_skim = "skimmed_looseSemimuonic_looseMuon_looseBjet"

# CRs & SRs
# output_skim = "skimmed_ttbarLike"
# output_skim = "skimmed_ttbarSemimuonicCR_tightMuon"
# output_skim = "skimmed_ttbarSemimuonicCR_tightMuon_newBtag"
# output_skim = "skimmed_ttbarSemimuonicCR"
# output_skim = "skimmed_ttbarSemimuonicCR_Met30GeV"
# output_skim = "skimmed_ttbarSemimuonicCR_Met50GeV_2mediumBjets"
# output_skim = "skimmed_ttbarSemimuonicCR_Met50GeV_2tightBjets"
# output_skim = "skimmed_ttbarSemimuonicCR_Met50GeV_1mediumBjets_muonIdIso"

# output_skim = "skimmed_ttZSemimuonicCR_tightMuon_noLooseMuonIso"
# output_skim = "skimmed_ttZSemimuonicCR_Met50GeV"

# output_skim = "skimmed_SR_Met50GeV"
output_skim = "skimmed_SemimuonicSR_Met50GeV"
# output_skim = "skimmed_SemimuonicSR_Met50GeV_0LooseEle"

# file_name = "6476B810-7ED2-704C-B80D-6F956C63EEBD.root"

# input_file_list = ("./skimmed_loose/test_TTToSemileptonic.root",)
# output_dir = f"./skimmed_ttbar/"

base_path = "/nfs/dust/cms/user/jniedzie/ttalps_cms"
# base_path = "/nfs/dust/cms/user/lrygaard/ttalps_cms"

samples = (
  # Backgrounds
  "backgrounds2018/TTToSemiLeptonic",
  "backgrounds2018/TTToHadronic",
  "backgrounds2018/TTTo2L2Nu",
  
  "backgrounds2018/ST_tW_antitop",
  "backgrounds2018/ST_tW_top",
  "backgrounds2018/ST_t-channel_antitop",
  "backgrounds2018/ST_t-channel_top",
  
  "backgrounds2018/DYJetsToMuMu_M-50",
  "backgrounds2018/DYJetsToMuMu_M-10to50",
  
  "backgrounds2018/WJetsToLNu",
  
  "backgrounds2018/TTZToLLNuNu",
  "backgrounds2018/TTZToLLNuNu_M-1to10",
  
  "backgrounds2018/TTWJetsToLNu",
  
  "backgrounds2018/ttHTobb",
  "backgrounds2018/ttHToNonbb",
  "backgrounds2018/ttHToMuMu",
  
  "backgrounds2018/TTZZ",
  "backgrounds2018/TTZH",
  "backgrounds2018/TTTT"
  
  # # # QCD
  # # "backgrounds2018/QCD_Pt_15to30",
  # # "backgrounds2018/QCD_Pt_30to50",
  # # "backgrounds2018/QCD_Pt_50to80",
  # # "backgrounds2018/QCD_Pt_80to120",
  # # "backgrounds2018/QCD_Pt_120to170",
  # # "backgrounds2018/QCD_Pt_170to300",
  # # "backgrounds2018/QCD_Pt_300to470",
  # # "backgrounds2018/QCD_Pt_470to600",
  # # "backgrounds2018/QCD_Pt_600to800",
  # # "backgrounds2018/QCD_Pt_800to1000",
  # # "backgrounds2018/QCD_Pt_1000to1400",
  # # "backgrounds2018/QCD_Pt_1400to1800",
  # # "backgrounds2018/QCD_Pt_1800to2400",
  # # "backgrounds2018/QCD_Pt_2400to3200",
  # # "backgrounds2018/QCD_Pt_3200toInf",

  QCD mu enhanced
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

  # Data
  "collision_data2018/SingleMuon2018A",
  "collision_data2018/SingleMuon2018B",
  "collision_data2018/SingleMuon2018C",
  "collision_data2018/SingleMuon2018D",
  
  # LLPnanoAOD
  # tt̄
  # "/backgrounds2018/TTToSemiLeptonic_LLPnanoAOD",
  
  # # QCD mu enriched
  #  "/backgrounds2018/QCDPt15To20_LLPnanoAOD",
  #  "/backgrounds2018/QCDPt20To30_LLPnanoAOD",
  #  "/backgrounds2018/QCDPt30To50_LLPnanoAOD",
  #  "/backgrounds2018/QCDPt50To80_LLPnanoAOD",
  #  "/backgrounds2018/QCDPt80To120_LLPnanoAOD",
  #  "/backgrounds2018/QCDPt120To170_LLPnanoAOD",
  #  "/backgrounds2018/QCDPt170To300_LLPnanoAOD",
  #  "/backgrounds2018/QCDPt300To470_LLPnanoAOD",
  #  "/backgrounds2018/QCDPt470To600_LLPnanoAOD",
  #  "/backgrounds2018/QCDPt600To800_LLPnanoAOD",
  #  "/backgrounds2018/QCDPt800To1000_LLPnanoAOD",
  #  "/backgrounds2018/QCDPt1000_LLPnanoAOD",
  
  # Signals
  #  "/signals/tta_mAlp-0p35GeV_ctau-1e0mm_nEvents-100",
  #  "/signals/tta_mAlp-0p35GeV_ctau-1e1mm_nEvents-100",
  #  "/signals/tta_mAlp-0p35GeV_ctau-1e2mm_nEvents-100",
  #  "/signals/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-100",
  #  "/signals/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-1000",
  #  "/signals/tta_mAlp-0p35GeV_ctau-1e7mm_nEvents-1000",
  #  "/signals/tta_mAlp-0p35GeV_ctau-1e0mm",
  #  "/signals/tta_mAlp-0p35GeV_ctau-1e1mm",
  #  "/signals/tta_mAlp-0p35GeV_ctau-1e2mm",
  #  "/signals/tta_mAlp-0p35GeV_ctau-1e3mm",
  #  "/signals/tta_mAlp-0p35GeV_ctau-1e5mm",
)

# this has to be here, otherwise the script will not work:
sample_path = ""

input_directory = f"{base_path}/{sample_path}/{input_skim}"
output_dir = f"{base_path}/{sample_path}/{output_skim}/"