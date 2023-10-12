nEvents = -1
printEveryNevents = 1000

runDefaultHistograms = False
runTriggerHistograms = True

ttbarCategories = ["inclusive", "hh", "he", "hmu", "htau", "ee", "mumu", "tautau", "emu", "etau", "mutau", "other"]
variableNames = ["muonMaxPt", "eleMaxPt", "jetMaxPt", "jetHt"]
selectionNames = ["singleLepton", "dilepton", "hadron"]

weightsBranchName = "genWeight"

triggerSets = {
    "hadBoth": ("HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59", "HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94"),
    "hadSinglebtag": ("HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59", ),
    "hadDoublebtag": ("HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94", ),
    # "had_Doublebtag_5jet100": ("HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5"),
    # "had_Doublebtag_5jet120": ("HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepCSV_4p5"),

    "heBoth": ("HLT_Ele28_eta2p1_WPTight_Gsf_HT150", "HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned"),
    "heEle28": ("HLT_Ele28_eta2p1_WPTight_Gsf_HT150", ),
    "heEle30_Jet35": ("HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned", ),

    "ele28": ("HLT_Ele28_WPTight_Gsf", ),
    "ele30": ("HLT_Ele30_WPTight_Gsf", ),
    "ele32": ("HLT_Ele32_WPTight_Gsf", ),
    "ele35": ("HLT_Ele35_WPTight_Gsf", ),
    "ele38": ("HLT_Ele38_WPTight_Gsf", ),
    "ele23Ele12": ("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL", ),

    "isomu24": ("HLT_IsoMu24", ),
    "mu17Mu8": ("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ", ),

    "emuMu12-8_ele23": ("HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL"),
    "emuMu23_ele12": ("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", ),
}


def GetHistogramsParameters():
    histParams = ()

    for ttbar_category in ttbarCategories:
        for variable in variableNames:
            outputDir = f"{ttbar_category}/{variable}"
            name = f"{ttbar_category}_{variable}"
            histParams.append((name, 1000, 0, 1000, outputDir))

            for set_name in triggerSets.keys():
                name = f"{ttbar_category}_{variable}_{set_name}"
                histParams.append((name, 1000, 0, 1000, outputDir))
                name += "_eff"
                histParams.append((name, 1000, 0, 1000, outputDir))

                for selection in selectionNames:
                    name = f"{ttbar_category}_{variable}_{set_name}_{selection}"
                    histParams.append((name, 1000, 0, 1000, outputDir))

    return histParams


histParams = GetHistogramsParameters()
