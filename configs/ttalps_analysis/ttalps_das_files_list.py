max_files = -1

lovisa_base_path = "/nfs/dust/cms/user/lrygaard/ttalps_cms"
base_path = "/nfs/dust/cms/user/jniedzie/ttalps_cms"

# skim = "skimmed_looseSemileptonic"
# skim = "skimmed_looseSemimuonic_tightMuon"
# skim = "skimmed_looseSemimuonic"
skim = "skimmed_looseSemimuonic_looseMuon_looseBjet"

# skim = "histograms_pileup"

# file_name = "02D6A1FE-C8EB-1A48-8B31-149FDFB64893.root"

input_output_dirs = (
  # tt̄
  # (f"{lovisa_base_path}/backgrounds18/TTToSemiLeptonic/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/TTToSemiLeptonic_LLPnanoAOD/{skim}/"),
  
  # QCD mu enriched
  # (f"{lovisa_base_path}/backgrounds18/QCDPt15To20/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/QCDPt15To20_LLPnanoAOD/{skim}/"),
  # (f"{lovisa_base_path}/backgrounds18/QCDPt20To30/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/QCDPt20To30_LLPnanoAOD/{skim}/"),
  # (f"{lovisa_base_path}/backgrounds18/QCDPt30To50/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/QCDPt30To50_LLPnanoAOD/{skim}/"),
  # (f"{lovisa_base_path}/backgrounds18/QCDPt50To80/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/QCDPt50To80_LLPnanoAOD/{skim}/"),
  # (f"{lovisa_base_path}/backgrounds18/QCDPt80To120/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/QCDPt80To120_LLPnanoAOD/{skim}/"),
  # (f"{lovisa_base_path}/backgrounds18/QCDPt120To170/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/QCDPt120To170_LLPnanoAOD/{skim}/"),
  # (f"{lovisa_base_path}/backgrounds18/QCDPt170To300/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/QCDPt170To300_LLPnanoAOD/{skim}/"),
  # (f"{lovisa_base_path}/backgrounds18/QCDPt300To470/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/QCDPt300To470_LLPnanoAOD/{skim}/"),
  # (f"{lovisa_base_path}/backgrounds18/QCDPt470To600/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/QCDPt470To600_LLPnanoAOD/{skim}/"),
  # (f"{lovisa_base_path}/backgrounds18/QCDPt600To800/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/QCDPt600To800_LLPnanoAOD/{skim}/"),
  # (f"{lovisa_base_path}/backgrounds18/QCDPt800To1000/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/QCDPt800To1000_LLPnanoAOD/{skim}/"),
  # (f"{lovisa_base_path}/backgrounds18/QCDPt1000/LLPNanoAOD/",
  #  f"{base_path}/backgrounds2018/QCDPt1000_LLPnanoAOD/{skim}/"),
  
  # Signals
  # (f"{lovisa_base_path}/signal/tta_mAlp-0p35GeV_ctau-1e0mm_nEvents-100/LLPNanoAOD/",
  #  f"{base_path}/signals/tta_mAlp-0p35GeV_ctau-1e0mm/{skim}/"),
  # (f"{lovisa_base_path}/signal/tta_mAlp-0p35GeV_ctau-1e1mm_nEvents-100/LLPNanoAOD/",
  #  f"{base_path}/signals/tta_mAlp-0p35GeV_ctau-1e1mm/{skim}/"),
  # (f"{lovisa_base_path}/signal/tta_mAlp-0p35GeV_ctau-1e2mm_nEvents-100/LLPNanoAOD/",
  #  f"{base_path}/signals/tta_mAlp-0p35GeV_ctau-1e2mm/{skim}/"),
  # (f"{lovisa_base_path}/signal/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-100/LLPNanoAOD/",
  #  f"{base_path}/signals/tta_mAlp-0p35GeV_ctau-1e3mm/{skim}/"),
  # (f"{lovisa_base_path}/signal/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-1000/LLPNanoAOD/",
  #  f"{base_path}/signals/tta_mAlp-0p35GeV_ctau-1e5mm/{skim}/"),
)

# datasets_and_output_dirs = (
# # # tt̄
#   ("/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/TTToSemiLeptonic/{skim}/"),
  
#   ("/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/TTToHadronic/{skim}/"),
  
#   ("/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/TTTo2L2Nu/{skim}/"),

# # Single top
#   ("/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/ST_tW_antitop/{skim}/"),
#   ("/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/ST_tW_top/{skim}/"),
#   ("/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/ST_t-channel_antitop/{skim}/"),
#   ("/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/ST_t-channel_top/{skim}/"),

# # DY
#   ("/DYJetsToMuMu_M-10to50_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/DYJetsToMuMu_M-10to50/{skim}/"),
#   ("/DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/DYJetsToMuMu_M-50/{skim}/"),

# # W+jets
#   ("/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/WJetsToLNu/{skim}/"),

# # ttV
#   ("/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/TTZToLLNuNu/{skim}/"),
#   ("/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/TTZToLLNuNu_M-1to10/{skim}/"),
#   # ("/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#   #  f"{base_path}/backgrounds2018/ttZJets/{skim}/"),

#   ("/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/TTWJetsToLNu/{skim}/"),
#   # ("/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#   #  f"{base_path}/backgrounds2018/ttWJets/{skim}/"),

# # ttH
#   ("/ttHToMuMu_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/ttHToMuMu/{skim}/"),
#   ("/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/ttHTobb/{skim}/"),
#   ("/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/ttHToNonbb/{skim}/"),
  
# # TTZZ, TTZH, TTTT
#   ("/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
#    f"{base_path}/backgrounds2018/TTZZ/{skim}/"),
#   ("/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/TTZH/{skim}/"),
#   ("/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/TTTT/{skim}/"),


# # # QCD
# #   # ("/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_15to30/{skim}/"),
# #   # ("/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_30to50/{skim}/"),
# #   # ("/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_50to80/{skim}/"),
# #   # ("/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_80to120/{skim}/"),
# #   # ("/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_120to170/{skim}/"),
# #   # ("/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_170to300/{skim}/"),
# #   # ("/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_300to470/{skim}/"),
# #   # ("/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_470to600/{skim}/"),
# #   # ("/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_600to800/{skim}/"),
# #   # ("/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_800to1000/{skim}/"),
# #   # ("/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_1000to1400/{skim}/"),
# #   # ("/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_1400to1800/{skim}/"),
# #   # ("/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_1800to2400/{skim}/"),
# #   # ("/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_2400to3200/{skim}/"),
# #   # ("/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
# #   # f"{base_path}/backgrounds2018/QCD_Pt_3200toInf/{skim}/"),

# # QCD mu enriched
#   ("/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/QCD_Pt_15to20_MuEnriched/{skim}/"),
#   ("/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/QCD_Pt_20to30_MuEnriched/{skim}/"),
#   ("/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/QCD_Pt_30to50_MuEnriched/{skim}/"),
#   ("/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/QCD_Pt_50to80_MuEnriched/{skim}/"),
#   ("/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/QCD_Pt_80to120_MuEnriched/{skim}/"),
#   ("/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/QCD_Pt_120to170_MuEnriched/{skim}/"),
#   ("/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/QCD_Pt_170to300_MuEnriched/{skim}/"),
#   ("/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/QCD_Pt_300to470_MuEnriched/{skim}/"),
#   ("/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/QCD_Pt_470to600_MuEnriched/{skim}/"),
#   ("/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/QCD_Pt_600to800_MuEnriched/{skim}/"),
#   ("/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/QCD_Pt_800to1000_MuEnriched/{skim}/"),
#   ("/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",
#    f"{base_path}/backgrounds2018/QCD_Pt_1000_MuEnriched/{skim}/"),

# # Data
#   ("/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD",
#    f"{base_path}/collision_data2018/SingleMuon2018A/{skim}/"),
#   ("/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD",
#    f"{base_path}/collision_data2018/SingleMuon2018B/{skim}/"),
#   ("/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD",
#    f"{base_path}/collision_data2018/SingleMuon2018C/{skim}/"),
#   ("/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD",
#    f"{base_path}/collision_data2018/SingleMuon2018D/{skim}/"),
# )

# # this has to be here, otherwise the script will not work:
dataset = ""
output_dir = ""
input_directory = ""




# jniedzie ID: 18340173  11/27 14:21	_      _    501    501 18340173.0-500
# jniedzie ID: 18340174  11/27 14:21	_      _     91     91 18340174.0-90
# jniedzie ID: 18340175  11/27 14:21	_      _    175    175 18340175.0-174
# jniedzie ID: 18340176  11/27 14:21	_      _    363    363 18340176.0-362
# jniedzie ID: 18340177  11/27 14:21	_      _    251    251 18340177.0-250
# jniedzie ID: 18340178  11/27 14:21      _      _    289    289 18340178.0-288
# jniedzie ID: 18340179  11/27 14:21	_      _    222    222 18340179.0-221
# jniedzie ID: 18340180  11/27 14:21	_      _    433    433 18340180.0-432
# jniedzie ID: 18340181  11/27 14:21	_      _    319    319 18340181.0-318
# jniedzie ID: 18340182  11/27 14:21	_      _    228    228 18340182.0-227
# jniedzie ID: 18340183  11/27 14:21	_      _    316    316 18340183.0-315
# jniedzie ID: 18340184  11/27 14:22	_      _    479    479 18340184.0-478
# jniedzie ID: 18340185  11/27 14:22	_      _    253    253 18340185.0-252
# jniedzie ID: 18340186  11/27 14:22	_      _     45     45 18340186.0-44
# jniedzie ID: 18340187  11/27 14:22      _      _     50     50 18340187.0-49
# jniedzie ID: 18340188  11/27 14:22	_      _     39     39 18340188.0-38
# jniedzie ID: 18340189  11/27 14:22      _      _     45     45 18340189.0-44
# jniedzie ID: 18340190  11/27 14:22	_      _    100    100 18340190.0-99

# ls -1 QCDPt15To20_LLPnanoAOD/skimmed_looseSemimuonic_looseMuon_looseBjet/*root | wc -l
# ls -1 QCDPt20To30_LLPnanoAOD/skimmed_looseSemimuonic_looseMuon_looseBjet/*root | wc -l
# ls -1 QCDPt30To50_LLPnanoAOD/skimmed_looseSemimuonic_looseMuon_looseBjet/*root | wc -l
# ls -1 QCDPt50To80_LLPnanoAOD/skimmed_looseSemimuonic_looseMuon_looseBjet/*root | wc -l
# ls -1 QCDPt80To120_LLPnanoAOD/skimmed_looseSemimuonic_looseMuon_looseBjet/*root | wc -
# ls -1 QCDPt120To170_LLPnanoAOD/skimmed_looseSemimuonic_looseMuon_looseBjet/*root | wc -l
# ls -1 QCDPt170To300_LLPnanoAOD/skimmed_looseSemimuonic_looseMuon_looseBjet/*root | wc -l
# ls -1 QCDPt300To470_LLPnanoAOD/skimmed_looseSemimuonic_looseMuon_looseBjet/*root | wc -l
# ls -1 QCDPt470To600_LLPnanoAOD/skimmed_looseSemimuonic_looseMuon_looseBjet/*root | wc -l
# ls -1 QCDPt600To800_LLPnanoAOD/skimmed_looseSemimuonic_looseMuon_looseBjet/*root | wc -l
# ls -1 QCDPt800To1000_LLPnanoAOD/skimmed_looseSemimuonic_looseMuon_looseBjet/*root | wc -l
# ls -1 QCDPt1000_LLPnanoAOD/skimmed_looseSemimuonic_looseMuon_looseBjet/*root | wc -l

