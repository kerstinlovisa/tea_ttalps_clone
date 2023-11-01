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
  TH2D *hist = nullptr;

  if (pt < 10) {
    hist = muonSFvalues["muonLowPtRecoSFs"];
  } else if (pt > 10 && pt < 200) {
    hist = muonSFvalues["muonMidPtRecoSFs"];
  } else {
    hist = muonSFvalues["muonHighPtRecoSFs"];
  }

  BringEtaPtToHistRange(hist, eta, pt);

  int etaBin = hist->GetXaxis()->FindBin(eta);
  int ptBin = hist->GetYaxis()->FindBin(pt);

  return hist->GetBinContent(etaBin, ptBin);
}

float ScaleFactorsManager::GetMuonIDScaleFactor(float eta, float pt, MuonID id) {
  if(!id.PassesAnyId()) return 1.0;
  
  string name = "muon";

  if (pt < 15) {
    name += "LowPt";
  } else if (pt > 15) {
    name += "MidPt";
  }

  if (id.soft)
    name += "Soft";
  else if (id.highPt)
    name += "HighPt";
  else if (id.trkHighPt)
    name += "TrkHighPt";
  else if (id.tight)
    name += "Tight";
  else if (id.mediumPrompt)
    name += "MediumPrompt";
  else if (id.medium)
    name += "Medium";
  else if (id.loose)
    name += "Loose";
  else {
    warn() << "Muon ID is not defined: ";
    id.Print();
    return 1;
  }

  name += "IDSFs";

  if (!muonSFvalues.count(name)) {
    warn() << "Muon SFs for " << name << " are not defined" << endl;
    return 1;
  }

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