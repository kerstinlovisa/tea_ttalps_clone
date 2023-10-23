nEvents = -1
printEveryNevents = 1000

runDefaultHistograms = True
runLLPNanoHistograms = True

# weightsBranchName = "genWeight"

basePath = "/nfs/dust/cms/user/lrygaard/ttalps_cms/"

# inputFile = "signal/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-100000.root"
# outputFile = "signal/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-100000_hist.root"

# inputFile = "signal/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-100000.root"
# outputFile = "signal/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-100000_hist.root"

inputFile = "signal/tta_mAlp-0p35GeV_ctau-1e7mm_nEvents-100000.root"
outputFile = "signal/tta_mAlp-0p35GeV_ctau-1e7mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e7mm_nEvents-100000_hist.root"

inputFilePath = f"{basePath}/{inputFile}"
histogramsOutputFilePath = f"{basePath}/{outputFile}"


defaultHistParams = (
#  collection             variable                  bins    xmin     xmax     dir
  ("Event",               "nMuon",                  50,     0,       50,      ""  ),
  ("Muon",                "pt",                     2000,   0,       1000,    ""  ),
  ("Muon",                "eta",                    100,    -2.5,    2.5,     ""  ),
  ("Muon",                "dxy",                    400,    -20,     20,      ""  ),
  ("Muon",                "dz",                     400,    -20,     20,      ""  ),
  ("Muon",                "ip3d",                   400,    0,       20,      ""  ),
  ("Muon",                "sip3d",                  400,    0,       20,      ""  ),

  ("Event",               "nMuonExtended",          50,     0,       50,      ""  ),
  ("MuonExtended",        "dxyPV",                  400,    -20,     20,      ""  ),
#   ("MuonExtended",        "dxyPVErr",               400,    -20,     20,      ""  ),
  ("MuonExtended",        "dzPV",                   400,    -20,     20,      ""  ),
#   ("MuonExtended",        "dzPVErr",                400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyPVTraj",              400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyPVTrajErr",           400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyPVAbs",               400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyPVAbsErr",            400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyPVSigned",            400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyPVSignedErr",         400,    -20,     20,      ""  ),
#   ("MuonExtended",        "ip3DPVAbs",              400,    -20,     20,      ""  ),
#   ("MuonExtended",        "ip3DPVAbsErr",           400,    -20,     20,      ""  ),
  ("MuonExtended",        "ip3DPVSigned",           400,    -20,     20,      ""  ),
  ("MuonExtended",        "ip3DPVSignedErr",        400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyBS",                  400,    -20,     20,      ""  ),
#   ("MuonExtended",        "dxyBSErr",               400,    -20,     20,      ""  ),
  ("MuonExtended",        "dzBS",                   400,    -20,     20,      ""  ),
#   ("MuonExtended",        "dzBSErr",                400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyBSTraj",              400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyBSTrajErr",           400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyBSAbs",               400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyBSAbsErr",            400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyBSSigned",            400,    -20,     20,      ""  ),
  ("MuonExtended",        "dxyBSSignedErr",         400,    -20,     20,      ""  ),
#   ("MuonExtended",        "ip3DBSAbs",              400,    -20,     20,      ""  ),
#   ("MuonExtended",        "ip3DBSAbsErr",           400,    -20,     20,      ""  ),
  ("MuonExtended",        "ip3DBSSigned",           400,    -20,     20,      ""  ),
  ("MuonExtended",        "ip3DBSSignedErr",        400,    -20,     20,      ""  ),

  ("Event",               "nDSAMuon",               50,     0,       50,      ""  ),
  ("DSAMuon",             "pt",                     2000,    0,      1000,    ""  ),
  ("DSAMuon",             "eta",                    100,    -2.5,    2.5,     ""  ),
  ("DSAMuon",             "dxyPV",                  400,    -20,     20,      ""  ),
#   ("DSAMuon",             "dxyPVErr",               400,    -20,     20,      ""  ),
  ("DSAMuon",             "dzPV",                   400,    -20,     20,      ""  ),
#   ("DSAMuon",             "dzPVErr",                400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyPVTraj",              400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyPVTrajErr",           400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyPVAbs",               400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyPVAbsErr",            400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyPVSigned",            400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyPVSignedErr",         400,    -20,     20,      ""  ),
#   ("DSAMuon",             "ip3DPVAbs",              400,    -20,     20,      ""  ),
#   ("DSAMuon",             "ip3DPVAbsErr",           400,    -20,     20,      ""  ),
  ("DSAMuon",             "ip3DPVSigned",           400,    -20,     20,      ""  ),
  ("DSAMuon",             "ip3DPVSignedErr",        400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyBS",                  400,    -20,     20,      ""  ),
#   ("DSAMuon",             "dxyBSErr",               400,    -20,     20,      ""  ),
  ("DSAMuon",             "dzBS",                   400,    -20,     20,      ""  ),
#   ("DSAMuon",             "dzBSErr",                400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyBSTraj",              400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyBSTrajErr",           400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyBSAbs",               400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyBSAbsErr",            400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyBSSigned",            400,    -20,     20,      ""  ),
  ("DSAMuon",             "dxyBSSignedErr",         400,    -20,     20,      ""  ),
#   ("DSAMuon",             "ip3DBSAbs",              400,    -20,     20,      ""  ),
#   ("DSAMuon",             "ip3DBSAbsErr",           400,    -20,     20,      ""  ),
  ("DSAMuon",             "ip3DBSSigned",           400,    -20,     20,      ""  ),
  ("DSAMuon",             "ip3DBSSignedErr",        400,    -20,     20,      ""  ),
  
  ("Event",               "nElectron",              50,     0,       50,      ""  ),
  ("Electron",            "pt",                     2000,    0,      1000,    ""  ),
  ("Electron",            "eta",                    100,    -2.5,    2.5,     ""  ),
  ("Electron",            "dxy",                    400,    -20,     20,      ""  ),
  ("Electron",            "dz",                     400,    -20,     20,      ""  ),
  ("Electron",            "ip3d",                   400,    0,       20,      ""  ),
  ("Electron",            "sip3d",                  400,    0,       20,      ""  ),
  
  ("Event",               "nElectronExtended",      50,     0,       50,      ""  ),
  ("ElectronExtended",    "dxyPV",                  400,    -20,     20,      ""  ),
#   ("ElectronExtended",    "dxyPVErr",               400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dzPV",                   400,    -20,     20,      ""  ),
#   ("ElectronExtended",    "dzPVErr",                400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyPVTraj",              400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyPVTrajErr",           400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyPVAbs",               400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyPVAbsErr",            400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyPVSigned",            400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyPVSignedErr",         400,    -20,     20,      ""  ),
#   ("ElectronExtended",    "ip3DPVAbs",              400,    -20,     20,      ""  ),
#   ("ElectronExtended",    "ip3DPVAbsErr",           400,    -20,     20,      ""  ),
  ("ElectronExtended",    "ip3DPVSigned",           400,    -20,     20,      ""  ),
  ("ElectronExtended",    "ip3DPVSignedErr",        400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyBS",                  400,    -20,     20,      ""  ),
#   ("ElectronExtended",    "dxyBSErr",               400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dzBS",                   400,    -20,     20,      ""  ),
#   ("ElectronExtended",    "dzBSErr",                400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyBSTraj",              400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyBSTrajErr",           400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyBSAbs",               400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyBSAbsErr",            400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyBSSigned",            400,    -20,     20,      ""  ),
  ("ElectronExtended",    "dxyBSSignedErr",         400,    -20,     20,      ""  ),
#   ("ElectronExtended",    "ip3DBSAbs",              400,    -20,     20,      ""  ),
#   ("ElectronExtended",    "ip3DBSAbsErr",           400,    -20,     20,      ""  ),
  ("ElectronExtended",    "ip3DBSSigned",           400,    -20,     20,      ""  ),
  ("ElectronExtended",    "ip3DBSSignedErr",        400,    -20,     20,      ""  ),

  ("Event",               "nSV",                    50,     0,       50,      ""  ),
  ("SV",                  "x",                      400,    -20,     20,      ""  ),
  ("SV",                  "y",                      400,    -20,     20,      ""  ),
  ("SV",                  "z",                      400,    -20,     20,      ""  ),
  ("SV",                  "chi2",                   400,    -20,     20,      ""  ),
  ("SV",                  "ndof",                   50,     0,       50,      ""  ),

#   ("Event",               "nPV",                    50,     0,       50,      ""  ),
#   ("PV",                  "x",                      400,    -20,     20,      ""  ),
#   ("PV",                  "y",                      400,    -20,     20,      ""  ),
#   ("PV",                  "z",                      400,    -20,     20,      ""  ),
#   ("PV",                  "chi2",                   400,    -20,     20,      ""  ),
#   ("PV",                  "ndof",                   50,     0,       50,      ""  ),

  ("Event",               "nBS",                    50,     0,       50,      ""  ),
  ("BS",                  "x",                      400,    -20,     20,      ""  ),
  ("BS",                  "y",                      400,    -20,     20,      ""  ),
  ("BS",                  "z",                      400,    -20,     20,      ""  ),
  ("BS",                  "chi2",                   400,    -20,     20,      ""  ),
  ("BS",                  "ndof",                   50,     0,       50,      ""  ),
  
)

histParams = (
#  collection             variable                  bins    xmin     xmax     dir
  # ("Muon",                "leadingPt",              2000,   0,       1000,    ""  ),
)
