nEvents = -1
printEveryNevents = 1000

basePath = "/nfs/dust/cms/user/jniedzie/ttalps_cms/backgrounds/"
# basePath = "/nfs/dust/cms/user/jniedzie/ttalps_cms/signals/"
# basePath = "/nfs/dust/cms/user/jniedzie/ttalps_cms/collision_data/"

# basePath = "/Users/jeremi/Documents/Physics/DESY/ttalps_cms.nosync/data/backgrounds/"
# basePath = "/Users/jeremi/Documents/Physics/DESY/ttalps_cms.nosync/data/signals/"
# basePath = "/Users/jeremi/Documents/Physics/DESY/ttalps_cms.nosync/data/collision_data/"

sampleName = "QCD_Pt_470to600"

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
inputFilePath = f"{basePath}/{sampleName}/skimmed_looseSemileptonic/{fileName}"
treeOutputFilePath = f"{basePath}/{sampleName}/skimmed_ttbarLike/{fileName}"

triggerSelection = (
    "HLT_Ele28_eta2p1_WPTight_Gsf_HT150",
    "HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned",
    "HLT_Ele28_WPTight_Gsf",
    "HLT_Ele30_WPTight_Gsf",
    "HLT_Ele32_WPTight_Gsf",
    "HLT_IsoMu24",
)

extraEventCollections = {
    "GoodLeptons": {
        "inputCollections": ("Muon", "Electron"),
        "pt": (30., 9999999.),
        "eta": (-2.4, 2.4),
    },
    "AlmostGoodLeptons": {
        "inputCollections": ("Muon", "Electron"),
        "pt": (15., 9999999.),
        "eta": (-2.5, 2.5),
    },
    "GoodJets": {
        "inputCollections": ("Jet", ),
        "pt": (30., 9999999.),
        "eta": (-2.4, 2.4),
    },
    "GoodBtaggedJets": {
        "inputCollections": ("Jet", ),
        "pt": (30., 9999999.),
        "eta": (-2.4, 2.4),
        "btagDeepB": (0.5, 9999999.),
    },
}

eventSelections = {
    "MET_pt": (30, 9999999),
    "nGoodLeptons": (1, 1),
    "nGoodJets": (4, 9999999),
    "nGoodBtaggedJets": (2, 9999999),
}