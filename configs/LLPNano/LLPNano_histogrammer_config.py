nEvents = -1
printEveryNevents = 1000

runDefaultHistograms = True
runLLPNanoAODHistograms = True

# weightsBranchName = "genWeight"

basePath = "/nfs/dust/cms/user/lrygaard/ttalps_cms/"

# inputFile = "signal/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-100000.root"
# outputFile = "signal/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-100000_hist.root"

# inputFile = "signal/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-100000.root"
# outputFile = "signal/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-100000_hist.root"

# inputFile = "signal/tta_mAlp-0p35GeV_ctau-1e7mm_nEvents-100000.root"
# outputFile = "signal/tta_mAlp-0p35GeV_ctau-1e7mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e7mm_nEvents-100000_hist.root"

# inputFile = "signal/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-1000/LLPNanoAOD/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-1000_part-0.root"
# outputFile = "signal/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-1000_part-0_hist.root"

# inputFile = "signal/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-1000/LLPNanoAOD/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-1000_part-0.root"
# outputFile = "signal/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-1000_part-0_hist.root"

inputFile = "signal/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-1000/LLPNanoAOD/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-100000.root"
outputFile = "signal/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-100000_hist.root"



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
  ("Muon",                "trkNumPlanes",           400,    0,       20,      ""  ),
  ("Muon",                "trkNumHits",             400,    0,       20,      ""  ),
  ("Muon",                "trkNumDTHits",           400,    0,       20,      ""  ),
  ("Muon",                "trkNumCSCHits",          400,    0,       20,      ""  ),
  ("Muon",                "normChi2",               400,    -20,     20,      ""  ),

  ("Event",               "nMuonExtended",          50,     0,       50,      ""  ),
  ("MuonExtended",        "dxyPV",                  2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyPVErr",               2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dzPV",                   2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dzPVErr",                2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyPVTraj",              2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyPVTrajErr",           2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyPVAbs",               2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyPVAbsErr",            2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyPVSigned",            2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyPVSignedErr",         2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "ip3DPVAbs",              2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "ip3DPVAbsErr",           2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "ip3DPVSigned",           2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "ip3DPVSignedErr",        2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyBS",                  2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyBSErr",               2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dzBS",                   2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dzBSErr",                2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyBSTraj",              2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyBSTrajErr",           2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyBSAbs",               2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyBSAbsErr",            2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyBSSigned",            2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "dxyBSSignedErr",         2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "ip3DBSAbs",              2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "ip3DBSAbsErr",           2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "ip3DBSSigned",           2000,   -1000,   1000,    ""  ),
  ("MuonExtended",        "ip3DBSSignedErr",        2000,   -1000,   1000,    ""  ),

  ("Event",               "nDSAMuon",               50,     0,       50,      ""  ),
  ("DSAMuon",             "pt",                     2000,    0,      1000,    ""  ),
  ("DSAMuon",             "eta",                    100,    -2.5,    2.5,     ""  ),
  ("DSAMuon",             "dxyPV",                  2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyPVErr",               2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dzPV",                   2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dzPVErr",                2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyPVTraj",              2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyPVTrajErr",           2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyPVAbs",               2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyPVAbsErr",            2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyPVSigned",            2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyPVSignedErr",         2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "ip3DPVAbs",              2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "ip3DPVAbsErr",           2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "ip3DPVSigned",           2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "ip3DPVSignedErr",        2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyBS",                  2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyBSErr",               2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dzBS",                   2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dzBSErr",                2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyBSTraj",              2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyBSTrajErr",           2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyBSAbs",               2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyBSAbsErr",            2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyBSSigned",            2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "dxyBSSignedErr",         2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "ip3DBSAbs",              2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "ip3DBSAbsErr",           2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "ip3DBSSigned",           2000,    -1000,   1000,   ""  ),
  ("DSAMuon",             "ip3DBSSignedErr",        2000,    -1000,   1000,   ""  ),
  
  ("Event",               "nElectron",              50,     0,       50,      ""  ),
  ("Electron",            "pt",                     2000,    0,      1000,    ""  ),
  ("Electron",            "eta",                    100,    -2.5,    2.5,     ""  ),
  ("Electron",            "dxy",                    400,    -20,     20,      ""  ),
  ("Electron",            "dz",                     400,    -20,     20,      ""  ),
  ("Electron",            "ip3d",                   400,    0,       20,      ""  ),
  ("Electron",            "sip3d",                  400,    0,       20,      ""  ),
  ("Electron",            "normChi2",               400,    -20,     20,      ""  ),
  
  ("Event",               "nElectronExtended",      50,     0,       50,      ""  ),
  ("ElectronExtended",    "dxyPV",                  2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyPVErr",               2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dzPV",                   2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dzPVErr",                2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyPVTraj",              2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyPVTrajErr",           2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyPVAbs",               2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyPVAbsErr",            2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyPVSigned",            2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyPVSignedErr",         2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "ip3DPVAbs",              2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "ip3DPVAbsErr",           2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "ip3DPVSigned",           2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "ip3DPVSignedErr",        2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyBS",                  2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyBSErr",               2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dzBS",                   2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dzBSErr",                2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyBSTraj",              2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyBSTrajErr",           2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyBSAbs",               2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyBSAbsErr",            2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyBSSigned",            2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "dxyBSSignedErr",         2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "ip3DBSAbs",              2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "ip3DBSAbsErr",           2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "ip3DBSSigned",           2000,   -1000,   1000,    ""  ),
  ("ElectronExtended",    "ip3DBSSignedErr",        2000,   -1000,   1000,    ""  ),

  ("Event",               "nLowPtElectron",         50,     0,       50,      ""  ),
  ("LowPtElectron",       "pt",                     2000,    0,      1000,    ""  ),
  ("LowPtElectron",       "eta",                    100,    -2.5,    2.5,     ""  ),
  ("LowPtElectron",       "dxy",                    400,    -20,     20,      ""  ),
  ("LowPtElectron",       "dz",                     400,    -20,     20,      ""  ),
  ("LowPtElectron",       "ip3d",                   400,    0,       20,      ""  ),
  ("LowPtElectron",       "sip3d",                  400,    0,       20,      ""  ),
  ("LowPtElectron",       "normChi2",               400,    -20,     20,      ""  ),

  ("Event",               "nLowPtElectronExtended",  50,     0,       50,      ""  ),
  ("LowPtElectronExtended","dxyPV",                  2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyPVErr",               2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dzPV",                   2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dzPVErr",                2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyPVTraj",              2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyPVTrajErr",           2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyPVAbs",               2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyPVAbsErr",            2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyPVSigned",            2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyPVSignedErr",         2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","ip3DPVAbs",              2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","ip3DPVAbsErr",           2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","ip3DPVSigned",           2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","ip3DPVSignedErr",        2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyBS",                  2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyBSErr",               2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dzBS",                   2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dzBSErr",                2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyBSTraj",              2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyBSTrajErr",           2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyBSAbs",               2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyBSAbsErr",            2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyBSSigned",            2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","dxyBSSignedErr",         2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","ip3DBSAbs",              2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","ip3DBSAbsErr",           2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","ip3DBSSigned",           2000,   -1000,   1000,    ""  ),
  ("LowPtElectronExtended","ip3DBSSignedErr",        2000,   -1000,   1000,    ""  ),

  ("Event",               "nSV",                    50,     0,       50,      ""  ),
  ("SV",                  "x",                      400,    -20,     20,      ""  ),
  ("SV",                  "y",                      400,    -20,     20,      ""  ),
  ("SV",                  "z",                      400,    -20,     20,      ""  ),
  ("SV",                  "chi2",                   400,    -20,     20,      ""  ),
  ("SV",                  "ndof",                   50,     0,       50,      ""  ),

  ("Event",               "nBS",                    50,     0,       50,      ""  ),
  ("BS",                  "x",                      400,    -20,     20,      ""  ),
  ("BS",                  "y",                      400,    -20,     20,      ""  ),
  ("BS",                  "z",                      400,    -20,     20,      ""  ),
  ("BS",                  "chi2",                   400,    -20,     20,      ""  ),
  ("BS",                  "ndof",                   50,     0,       50,      ""  ),
  ("BS",                  "ntracks",                50,     0,       50,      ""  ),

  ("Event",               "nGenPart",               50,     0,       50,      ""  ),
  ("GenPart",             "pt",                     2000,   0,       1000,    ""  ),
  ("GenPart",             "pdgId",                  500,    0,       500,     ""  ),
  ("GenPart",             "mass",                   2000,   0,       200,     ""  ),
  ("GenPart",             "vx",                     2000,   -1e6,    1e6,     ""  ),
  ("GenPart",             "vy",                     2000,   -1e6,    1e6,     ""  ),
  ("GenPart",             "vz",                     2000,   -1e6,    1e6,     ""  ),
  ("GenPart",             "Rho",                    2000,   -1e6,    1e6,     ""  ),
  ("GenPart",             "R",                      2000,   -1e6,    1e6,     ""  ),

  ("Event",               "nMuonVertex",            50,     0,       50,      ""  ),
  ("MuonVertex",          "vxy",                    2000,   -1e6,    1e6,     ""  ),
  ("MuonVertex",          "vxySigma",               2000,   -1e6,    1e6,     ""  ),
  ("MuonVertex",          "vz",                     2000,   -1e6,    1e6,     ""  ),
  ("MuonVertex",          "chi2",                   400,    -20,     20,      ""  ),
  ("MuonVertex",          "dR",                     400,    -20,     20,      ""  ),

  ("Event",               "nMuonCombVertex",        50,     0,       50,      ""  ),
  ("MuonCombVertex",      "vxy",                    2000,   -1e6,    1e6,     ""  ),
  ("MuonCombVertex",      "vxySigma",               2000,   -1e6,    1e6,     ""  ),
  ("MuonCombVertex",      "vz",                     2000,   -1e6,    1e6,     ""  ),
  ("MuonCombVertex",      "chi2",                   400,    -20,     20,      ""  ),
  ("MuonCombVertex",      "dR",                     400,    -20,     20,      ""  ),

  ("Event",               "nDSAMuonVertex",         50,     0,       50,      ""  ),
  ("DSAMuonVertex",       "vxy",                    2000,   -1e6,    1e6,     ""  ),
  ("DSAMuonVertex",       "vxySigma",               2000,   -1e6,    1e6,     ""  ),
  ("DSAMuonVertex",       "vz",                     2000,   -1e6,    1e6,     ""  ),
  ("DSAMuonVertex",       "chi2",                   400,    -20,     20,      ""  ),
  ("DSAMuonVertex",       "dR",                     400,    -20,     20,      ""  ),

  # ("Event",               "nPV",                    50,     0,       50,      ""  ),
  # ("PV",                  "x",                      400,    -20,     20,      ""  ),
  # ("PV",                  "y",                      400,    -20,     20,      ""  ),
  # ("PV",                  "z",                      400,    -20,     20,      ""  ),
  # ("PV",                  "chi2",                   400,    -20,     20,      ""  ),
  # ("PV",                  "ndof",                   50,     0,       50,      ""  ),
  # ("PV",                  "ntracks",                50,     0,       50,      ""  ),
  
)

histParams = (
#  histName               bins    xmin     xmax     dir
 ("GenALP_pdgId",         500,    0,       500,     ""  ),
 ("GenALP_mass",          2000,   0,       100,     ""  ),
 ("GenALP_vx",            2000,   -1e6,    1e6,     ""  ),
 ("GenALP_vy",            2000,   -1e6,    1e6,     ""  ),
 ("GenALP_vz",            2000,   -1e6,    1e6,     ""  ),
#  ("GenALP_boost",         2000,   0,       1000,    ""  ),
 ("GenALP_vxyz",          2000,   0,       1000,    ""  ),
#  ("GenALP_proper_vxyz",   2000,   0,       1000,    ""  ),
 ("GenMuon_pdgId",        500,    0,       500,     ""  ),
 ("GenMuon_mass",         2000,   0,       100,     ""  ),
 ("GenMuon_vx",           2000,   -1e6,    1e6,     ""  ),
 ("GenMuon_vy",           2000,   -1e6,    1e6,     ""  ),
 ("GenMuon_vz",           2000,   -1e6,    1e6,     ""  ),
#  ("GenMuon_boost",        2000,   0,       1000,    ""  ),
 ("GenMuon_vxyz",         2000,   0,       1000,    ""  ),
#  ("GenMuon_proper_vxyz",  2000,   0,       1000,    ""  ),
 ("GenMuonFromALP_vx",           2000,   -1e8,    1e8,     ""  ),
 ("GenMuonFromALP_vy",           2000,   -1e8,    1e8,     ""  ),
 ("GenMuonFromALP_vz",           2000,   -1e8,    1e8,     ""  ),
#  ("GenMuonFromALP_boost",        2000,   0,       1000,    ""  ),
 ("GenMuonFromALP_vxyz",         2000,   0,       1000,    ""  ),
#  ("GenMuonFromALP_proper_vxyz",  2000,   0,       1000,    ""  ),
)
