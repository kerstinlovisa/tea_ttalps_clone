nEvents = -1
printEveryNevents = 1000

basePath = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds/"
# basePath = "/nfs/dust/cms/user/jniedzie/ttalps_cms/signals/"
# basePath = "/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data/"

# basePath = "/Users/jeremi/Documents/Physics/DESY/ttalps_cms.nosync/data/backgrounds/"
# basePath = "/Users/jeremi/Documents/Physics/DESY/ttalps_cms.nosync/data/signals/"
# basePath = "/Users/jeremi/Documents/Physics/DESY/ttalps_cms.nosync/data/collision_data/"

sampleName = "ttHToMuMu"
# skim = ""
skim = "skimmed_looseSemileptonic"
# skim = "skimmed_signalLike"
# skim = "skimmed_ttbarLike"

fileNames = {
    "TTbar_inclusive": "FCA55055-C8F3-C44B-8DCC-6DCBC0B8B992.root",
    "ST_tW_top": "776A38DC-FF27-6F4E-9B16-C55B696BAA92.root",
    "ST_tW_antitop": "09B1D3CA-5FCC-0A48-BFA6-E1759D5D7D02.root",
    "ttWJets": "5B123882-8484-1B47-9A07-57F8F526F6EF.root",
    "ttZJets": "EB2F627D-0570-7C4C-A561-C29B6E4F123A.root",
    "ttHToMuMu": "D41A5AFC-EC31-A64F-9E87-6F1C22ED6DCB.root",
    "QCD_Pt_30to50": "72E0DD65-5D9D-3E47-99A9-AAB4E4ACC724.root",
    "QCD_Pt_50to80": "CAB74055-4D6E-024F-9B89-465541A2B906.root",
    "QCD_Pt_80to120": "5D2183A8-8AC4-7841-9308-A1A221F27EBC.root",
    "QCD_Pt_120to170": "EFC4B90E-252D-5145-BE99-C880CAE3B061.root",
    "QCD_Pt_170to300": "5C540F1F-6B0C-1047-B020-539529AB3BB6.root",
    "QCD_Pt_300to470": "C5A7D337-F76C-B848-A17F-10BBBD72042B.root",
    "QCD_Pt_470to600": "452A92CA-5CED-A944-A44F-54CBD68D33CE.root",
    "QCD_Pt_600to800": "778F37B3-2E2D-024A-ADB2-66699F11783C.root",
    "QCD_Pt_800to1000": "191A7BDE-A93B-9440-9BC9-A6BEE36F43EE.root",
    "QCD_Pt_1000to1400": "C5C48DC6-E709-244D-B649-A6CC41B3F190.root",
    "QCD_Pt_1400to1800": "99B44156-580D-0249-9241-9E88DF59F04B.root",
    "QCD_Pt_1800to2400": "061D96A4-FE04-3348-9F8B-E7E9BA6E4327.root",
    "QCD_Pt_2400to3200": "A937F1B0-3D60-4E4D-B9EF-F7882A82450E.root",
    "QCD_Pt_3200toInf": "980542CA-9396-6344-88E3-EA9CCB639159.root",
    "tta_mAlp-0p35GeV": "tta_mAlp-0p35GeV_nEvents-100000.root",
    "SingleMuon2018": "36ED9511-D46A-0C4F-A485-C2DF1C874906.root"
}

fileName = fileNames[sampleName]
inputFilePath = f"{basePath}/{sampleName}/{skim}/{fileName}"
histsFileName = fileName.replace(".root", "_hists.root")
histogramsOutputFilePath = f"{basePath}/{sampleName}/{skim}/{histsFileName}"

defaultHistParams = {
# key              collection    variable      bins    xmin     xmax    outputdir  
  "n_muons"   :   ("Event",      "nMuon",      50,     0,       50,      ""  ),
  "muon_pt"   :   ("Muon",       "pt",         2000,    0,      1000,    ""  ),
  "muon_eta"  :   ("Muon",       "eta",        100,    -2.5,    2.5,     ""  ),
  "muon_dxy"  :   ("Muon",       "dxy",        400,    -20,     20,      ""  ),
  "muon_dz"   :   ("Muon",       "dz",         400,    -20,     20,      ""  ),
  "n_eles"    :   ("Event",      "nElectron",  50,     0,       50,      ""  ),
  "ele_pt"    :   ("Electron",   "pt",         2000,    0,      1000,    ""  ),
  "ele_eta"   :   ("Electron",   "eta",        100,    -2.5,    2.5,     ""  ),
  "ele_dxy"   :   ("Electron",   "dxy",        400,    -20,     20,      ""  ),
  "ele_dz"    :   ("Electron",   "dz",         400,    -20,     20,      ""  ),
  "n_jets"    :   ("Event",      "nJet",       50,     0,       50,      ""  ),
  "jet_pt"    :   ("Jet",        "pt",         2000,    0,      1000,    ""  ),
  "jet_eta"   :   ("Jet",        "eta",        100,    -2.5,    2.5,     ""  ),
  "jet_eta"   :   ("Jet",        "eta",        100,    -2.5,    2.5,     ""  ),
  "jet_btagDeepB":("Jet",        "btagDeepB",  200,    -1,      1,       ""  ),
}

ttalpsHistParams = {
  "muon_leading_pt"   :   ("Muon",       "leading_pt",         2000,    0,       1000,     ""  ),
  "muon_subleading_pt":   ("Muon",       "subleading_pt",      2000,    0,       1000,     ""  ),
  "ele_leading_pt"    :   ("Electron",   "leading_pt",         2000,    0,       1000,     ""  ),
  "ele_subleading_pt" :   ("Electron",   "subleading_pt",      2000,    0,       1000,     ""  ),
  "jet_leading_pt"    :   ("Jet",        "leading_pt",         2000,    0,       1000,     ""  ),
  "jet_subleading_pt" :   ("Jet",        "subleading_pt",      2000,    0,       1000,     ""  ),
}

defaultHistVariables = {key: (params[0],params[1]) for key, params in defaultHistParams.items()}
ttalpsHistVariables = {key: (params[0],params[1]) for key, params in ttalpsHistParams.items()}

histParams = {key : value for histParams in (defaultHistParams,ttalpsHistParams) for key,value in histParams.items()}

histTitles = {key: key for key, params in histParams.items()}
histNbins = {key: params[2] for key, params in histParams.items()}
histMin = {key: params[3] for key, params in histParams.items()}
histMax = {key: params[4] for key, params in histParams.items()}
histOutputDir = {key: params[5] for key, params in histParams.items()}