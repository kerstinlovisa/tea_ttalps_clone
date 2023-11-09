//  ScaleFactorsManager.cpp
//
//  Created by Jeremi Niedziela on 01/11/2023.

#include "ScaleFactorsManager.hpp"

#include "ConfigManager.hpp"

using namespace std;

ScaleFactorsManager::ScaleFactorsManager() {
  auto &config = ConfigManager::GetInstance();
  map<string, ScaleFactorsMap> muonSFs;
  config.GetScaleFactors("muonSFs", muonSFs);

  for (auto &[name, values] : muonSFs) {
    string path = "../data/" + name + ".root";
    if (!FileExists(path)) {
      ScaleFactorsMap muonSFs;
      CreateMuonSFsHistogram(values, path, name);
    }
    muonSFvalues[name] = (TH2D *)TFile::Open(path.c_str())->Get(name.c_str());
  }

  config.GetValue("applyMuonScaleFactors", applyMuonScaleFactors);
  config.GetValue("applyMuonTriggerScaleFactors", applyMuonTriggerScaleFactors);
}

void ScaleFactorsManager::CreateMuonSFsHistogram(const ScaleFactorsMap &muonSFs, string outputPath, string histName) {
  set<float> etaBinsSet, ptBinsSet;

  for (auto &[etaRange, valuesForEta] : muonSFs) {
    etaBinsSet.insert(get<0>(etaRange));
    etaBinsSet.insert(get<1>(etaRange));

    for (auto &[ptRange, values] : valuesForEta) {
      ptBinsSet.insert(get<0>(ptRange));
      ptBinsSet.insert(get<1>(ptRange));
    }
  }

  vector<float> etaBins(etaBinsSet.begin(), etaBinsSet.end());
  vector<float> ptBins(ptBinsSet.begin(), ptBinsSet.end());

  auto hist = new TH2D(histName.c_str(), histName.c_str(), etaBins.size() - 1, etaBins.data(), ptBins.size() - 1, ptBins.data());

  for (auto &[etaRange, valuesForEta] : muonSFs) {
    float eta = (get<1>(etaRange) + get<0>(etaRange)) / 2.;
    for (auto &[ptRange, values] : valuesForEta) {
      float pt = (get<1>(ptRange) + get<0>(ptRange)) / 2.;
      hist->Fill(eta, pt, values.at("value"));
    }
  }
  makeParentDirectories(outputPath);
  hist->SaveAs(outputPath.c_str());
}

float ScaleFactorsManager::GetMuonRecoScaleFactor(float eta, float pt) {
  if (!applyMuonScaleFactors) return 1.0;

  string name = "";

  if (pt < 10) {
    name = "NUM_TrackerMuons_DEN_genTracks";
  } else if (pt >= 10 && pt < 200) {
    name = "NUM_TrackerMuons_DEN_genTracks";
  } else {
    name = "NUM_GlobalMuons_DEN_TrackerMuons";
  }
  return GetScaleFactor(name, eta, pt);
}

float ScaleFactorsManager::GetMuonIDScaleFactor(float eta, float pt, MuonID id) {
  if (!applyMuonScaleFactors) return 1.0;
  if (!id.PassesAnyId()) return 1.0;

  string name = "";

  if (pt < 15) {
    if (id.soft)
      name = "NUM_SoftID_DEN_TrackerMuons";
    else if (id.tight)
      name = "NUM_TightID_DEN_TrackerMuons";
    else if (id.medium)
      name = "NUM_MediumID_DEN_TrackerMuons";
    else if (id.loose)
      name = "NUM_LooseID_DEN_TrackerMuons";
  } else if (pt >= 15) {
    if (id.soft)
      name = "NUM_SoftID_DEN_TrackerMuons";
    else if (id.highPt)
      name = "NUM_HighPtID_DEN_TrackerMuons";
    else if (id.trkHighPt)
      name = "NUM_TrkHighPtID_DEN_TrackerMuons";
    else if (id.tight)
      name = "NUM_TightID_DEN_TrackerMuons";
    else if (id.mediumPrompt)
      name = "NUM_MediumPromptID_DEN_TrackerMuons";
    else if (id.medium)
      name = "NUM_MediumID_DEN_TrackerMuons";
    else if (id.loose)
      name = "NUM_LooseID_DEN_TrackerMuons";
  }

  if (!muonSFvalues.count(name)) {
    warn() << "Muon ID SFs not defined for combination of pt and ID: " << (pt < 15 ? "low pt -- " : "mid-high pt -- ") << id.ToString()
           << endl;
    return 1;
  }
  return GetScaleFactor(name, eta, pt);
}

float ScaleFactorsManager::GetMuonIsoScaleFactor(float eta, float pt, MuonID id, MuonIso iso) {
  if (!applyMuonScaleFactors) return 1.0;
  if (pt < 15) return 1;                // no SFs for low pt muons
  if (!id.PassesAnyId()) return 1.0;    // not considered an actual muon
  if (!iso.PassesAnyIso()) return 1.0;  // it's not isolated at all
  if (iso.pFIsoVeryLoose) return 1.0;   // no SFs for very loosely isolated muons

  vector<tuple<string, int, int>> names;  // name, id tightness, iso tightness

  if (id.trkHighPt) {
    if (iso.tkIsoTight) {
      names.push_back({"NUM_TightRelTkIso_DEN_TrkHighPtIDandIPCut", 6, 2});
    }
    if (iso.tkIsoLoose) {
      names.push_back({"NUM_LooseRelTkIso_DEN_TrkHighPtIDandIPCut", 6, 1});
    }
  }
  if (id.highPt) {
    if (iso.tkIsoTight) {
      names.push_back({"NUM_TightRelTkIso_DEN_HighPtIDandIPCut", 5, 2});
    }
    if (iso.tkIsoLoose) {
      names.push_back({"NUM_LooseRelTkIso_DEN_HighPtIDandIPCut", 5, 1});
    }
  }
  if (id.tight) {
    if (iso.pFIsoTight || iso.pFIsoVeryTight || iso.pFIsoVeryVeryTight) {
      names.push_back({"NUM_TightRelIso_DEN_TightIDandIPCut", 4, 2});
    }
    if (iso.pFIsoLoose || iso.pFIsoMedium) {
      names.push_back({"NUM_LooseRelIso_DEN_TightIDandIPCut", 4, 1});
    }
  }
  if (id.mediumPrompt) {
    if (iso.pFIsoTight || iso.pFIsoVeryTight || iso.pFIsoVeryVeryTight) {
      names.push_back({"NUM_TightRelIso_DEN_MediumPromptID", 3, 2});
    }
    if (iso.pFIsoLoose || iso.pFIsoMedium) {
      names.push_back({"NUM_LooseRelIso_DEN_MediumPromptID", 3, 1});
    }
  }
  if (id.medium || id.tight) {
    if (iso.pFIsoTight || iso.pFIsoVeryTight || iso.pFIsoVeryVeryTight) {
      names.push_back({"NUM_TightRelIso_DEN_MediumID", 2, 2});
    }
    if (iso.pFIsoLoose || iso.pFIsoMedium) {
      names.push_back({"NUM_LooseRelIso_DEN_MediumID", 2, 1});
    }
  }
  if (id.loose || id.medium || id.tight) {
    if (iso.pFIsoLoose || iso.pFIsoMedium || iso.pFIsoTight || iso.pFIsoVeryTight || iso.pFIsoVeryVeryTight) {
      names.push_back({"NUM_LooseRelIso_DEN_LooseID", 1, 1});
    }
  }

  // order names first by id tightness, then by iso tightness
  sort(names.begin(), names.end(), [](const tuple<string, int, int> &a, const tuple<string, int, int> &b) {
    if (get<1>(a) == get<1>(b)) {
      return get<2>(a) < get<2>(b);
    }
    return get<1>(a) < get<1>(b);
  });

  // get the element from names with the highest id tightness and iso tightness
  string name = "";
  if (names.size() != 0) {
    name = get<0>(names.back());
  }

  if (!muonSFvalues.count(name)) {
    warn() << "Muon Iso SFs not defined for combination of ID & Iso: " << id.ToString() << " -- " << iso.ToString() << endl;
    return 1;
  }
  return GetScaleFactor(name, eta, pt);
}

float ScaleFactorsManager::GetMuonTriggerScaleFactor(float eta, float pt, MuonID id, MuonIso iso, bool IsoMu24included,
                                                     bool IsoMu50included) {
  if (!applyMuonTriggerScaleFactors) return 1.0;
  if (pt < 15) return 1;                                 // no SFs for low pt muons
  if (!id.PassesAnyId()) return 1.0;                     // not considered an actual muon
  if (!iso.PassesAnyIso()) return 1.0;                   // it's not isolated at all
  if (iso.pFIsoVeryLoose) return 1.0;                    // no SFs for very loosely isolated muons
  if (!IsoMu24included && !IsoMu50included) return 1.0;  // no SFs if none of the muon triggers were present

  vector<tuple<string, int, int>> names;  // name, id tightness, iso tightness

  if (IsoMu24included && !IsoMu50included) {
    if (id.tight) {
      if (iso.pFIsoTight || iso.pFIsoVeryTight || iso.pFIsoVeryVeryTight) {
        names.push_back({"NUM_IsoMu24_DEN_CutBasedIdTight_and_PFIsoTight", 2, 2});
      }
    }
    if (id.medium) {
      if (iso.pFIsoMedium || iso.pFIsoTight || iso.pFIsoVeryTight || iso.pFIsoVeryVeryTight) {
        names.push_back({"NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium", 1, 1});
      }
    }
  } else if (IsoMu24included && IsoMu50included) {
    if (id.tight) {
      if (iso.pFIsoTight || iso.pFIsoVeryTight || iso.pFIsoVeryVeryTight) {
        names.push_back({"NUM_IsoMu24_or_Mu50_DEN_CutBasedIdTight_and_PFIsoTight", 2, 2});
      }
    }
    if (id.medium) {
      if (iso.pFIsoMedium || iso.pFIsoTight || iso.pFIsoVeryTight || iso.pFIsoVeryVeryTight) {
        names.push_back({"NUM_IsoMu24_or_Mu50_DEN_CutBasedIdMedium_and_PFIsoMedium", 1, 1});
      }
    }
  } else if (!IsoMu24included && IsoMu50included) {
    if (id.highPt) {
      if (iso.tkIsoLoose || iso.tkIsoTight) {
        names.push_back({"NUM_Mu50_or_OldMu100_or_TkMu100_DEN_CutBasedIdGlobalHighPt_and_TkIsoLoose", 1, 1});
      }
    }
  }

  // order names first by id tightness, then by iso tightness
  sort(names.begin(), names.end(), [](const tuple<string, int, int> &a, const tuple<string, int, int> &b) {
    if (get<1>(a) == get<1>(b)) {
      return get<2>(a) < get<2>(b);
    }
    return get<1>(a) < get<1>(b);
  });

  // get the element from names with the highest id tightness and iso tightness
  string name = "";
  if (names.size() != 0) {
    name = get<0>(names.back());
  }

  if (!muonSFvalues.count(name)) {
    warn() << "Muon Trigger SFs not defined for combination of ID & Iso: " << id.ToString() << " -- " << iso.ToString()
           << " with Iso24: " << IsoMu24included << ", Iso50: " << IsoMu50included << endl;
    return 1;
  }
  return GetScaleFactor(name, eta, pt);
}

float ScaleFactorsManager::GetScaleFactor(string name, float eta, float pt) {
  TH2D *hist = muonSFvalues[name];

  BringEtaPtToHistRange(hist, eta, pt);

  int etaBin = hist->GetXaxis()->FindBin(eta);
  int ptBin = hist->GetYaxis()->FindBin(pt);

  return hist->GetBinContent(etaBin, ptBin);
}

void ScaleFactorsManager::BringEtaPtToHistRange(TH2D *hist, float &eta, float &pt) {
  if (eta < hist->GetXaxis()->GetBinLowEdge(1)) {
    eta = hist->GetXaxis()->GetBinLowEdge(1) + 0.01;
  }
  if (eta > hist->GetXaxis()->GetBinUpEdge(hist->GetNbinsX())) {
    eta = hist->GetXaxis()->GetBinUpEdge(hist->GetNbinsX()) - 0.01;
  }

  if (pt < hist->GetYaxis()->GetBinLowEdge(1)) {
    pt = hist->GetYaxis()->GetBinLowEdge(1) + 0.01;
  }

  if (pt > hist->GetYaxis()->GetBinUpEdge(hist->GetNbinsY())) {
    pt = hist->GetYaxis()->GetBinUpEdge(hist->GetNbinsY()) - 0.01;
  }
}
