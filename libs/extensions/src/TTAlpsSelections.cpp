//  TTAlpsSelections.cpp
//
//  Created by Jeremi Niedziela on 16/08/2023.

#include "TTAlpsSelections.hpp"

#include "ExtensionsHelpers.hpp"

using namespace std;

bool TTAlpsSelections::PassesTriggerSelections(const shared_ptr<Event> event) {
  for (auto &triggerName : triggerNames) {
    bool passes = false;
    try {
      passes = event->Get(triggerName);
    } catch (Exception &) {
      if (find(triggerWarningsPrinted.begin(), triggerWarningsPrinted.end(), triggerName) == triggerWarningsPrinted.end()) {
        warn() << "Trigger not present: " << triggerName << "\n";
        triggerWarningsPrinted.push_back(triggerName);
      }
    }
    if (passes) return true;
  }
  return false;
}

bool TTAlpsSelections::PassesLooseSemileptonicSelections(const shared_ptr<Event> event, shared_ptr<CutFlowManager> cutFlowManager) {
  float metPt = event->Get("MET_pt");
  if (!inRange(metPt, eventSelections["MET_pt"])) return false;
  cutFlowManager->UpdateCutFlow("MetPt");

  AddExtraCollections(event);

  if (!inRange(event->GetCollectionSize("GoodLeptons"), eventSelections["nGoodLeptons"])) return false;
  cutFlowManager->UpdateCutFlow("nGoodLeptons");

  if (!inRange(event->GetCollectionSize("GoodBtaggedJets"), eventSelections["nGoodBtaggedJets"])) return false;
  cutFlowManager->UpdateCutFlow("nGoodBtaggedJets");

  if (!inRange(event->GetCollectionSize("GoodJets"), eventSelections["nGoodJets"])) return false;
  cutFlowManager->UpdateCutFlow("nGoodJets");

  return true;
}

bool TTAlpsSelections::PassesSignalLikeSelections(const shared_ptr<Event> event, shared_ptr<CutFlowManager> cutFlowManager) {
  float metPt = event->Get("MET_pt");
  if (!inRange(metPt, eventSelections["MET_pt"])) return false;

  AddExtraCollections(event);

  if (!inRange(event->GetCollectionSize("GoodLeptons"), eventSelections["nGoodLeptons"])) return false;
  if (!inRange(event->GetCollectionSize("GoodBtaggedJets"), eventSelections["nGoodBtaggedJets"])) return false;
  if (!inRange(event->GetCollectionSize("GoodJets"), eventSelections["nGoodJets"])) return false;

  auto goodLeptons = event->GetCollection("GoodLeptons");
  int requiredGoodMuons = 3;
  for (auto lepton : *goodLeptons) {
    if (lepton->GetOriginalCollection() != "Electron") continue;
    requiredGoodMuons = 2;
    break;
  }
  if (event->GetCollectionSize("GoodMuons") < requiredGoodMuons) return false;
  cutFlowManager->UpdateCutFlow("twoAdditionalMuons");

  return true;
}

bool TTAlpsSelections::PassesSingleLeptonSelections(const shared_ptr<Event> event, shared_ptr<CutFlowManager> cutFlowManager) {
  float metPt = event->Get("MET_pt");
  if (!inRange(metPt, eventSelections["MET_pt"])) return false;

  AddExtraCollections(event);

  if (!inRange(event->GetCollectionSize("GoodLeptons"), eventSelections["nGoodLeptons"])) return false;
  if (!inRange(event->GetCollectionSize("GoodBtaggedJets"), eventSelections["nGoodBtaggedJets"])) return false;
  if (!inRange(event->GetCollectionSize("GoodJets"), eventSelections["nGoodJets"])) return false;

  int almostGoodLeptons = event->GetCollectionSize("AlmostGoodLeptons");
  if (almostGoodLeptons > 1) return false;
  if (almostGoodLeptons == 1) {
    auto leadingLepton = event->GetCollection("GoodLeptons")->at(0);
    auto survivingLepton = event->GetCollection("AlmostGoodLeptons")->at(0);
    if (survivingLepton != leadingLepton) return false;
  }
  if(cutFlowManager) cutFlowManager->UpdateCutFlow("noAdditionalMuons");

  return true;
}

bool TTAlpsSelections::PassesDileptonSelections(const shared_ptr<Event> event) {
  int muonsPt30 = 0;
  int electronsPt30;
  int jetsBtagged = 0;

  uint nMuons = event->Get("nMuon");
  auto muons = event->GetCollection("Muon");
  for (int i = 0; i < nMuons; i++) {
    float muonPt = muons->at(i)->Get("pt");
    float muonEta = muons->at(i)->Get("eta");
    if (muonPt > 30 && abs(muonEta) < 2.4) muonsPt30++;
  }
  uint nElectrons = event->Get("nElectron");
  auto electrons = event->GetCollection("Electron");
  for (int i = 0; i < nElectrons; i++) {
    float electronPt = electrons->at(i)->Get("pt");
    float electronEta = electrons->at(i)->Get("eta");
    if (electronPt > 30 && abs(electronEta) < 2.4) electronsPt30++;
  }
  uint nJets = event->Get("nJet");
  auto jets = event->GetCollection("Jet");
  for (int i = 0; i < nJets; i++) {
    float jetPt = jets->at(i)->Get("pt");
    float jet_eta = jets->at(i)->Get("eta");
    float jet_btagDeepB = jets->at(i)->Get("btagDeepB");
    if (jetPt > 30 && abs(jet_eta) < 2.4 && jet_btagDeepB > 0.5) jetsBtagged++;
  }

  if ((muonsPt30 + electronsPt30) < 2) return false;
  float metPt = event->Get("MET_pt");
  if (metPt <= 30) return false;
  if (jetsBtagged < 2) return false;
  return true;
}

bool TTAlpsSelections::PassesHadronSelections(const shared_ptr<Event> event) {
  int jetsBtagged = 0;
  int jetsPt30;

  uint nJets = event->Get("nJet");
  auto jets = event->GetCollection("Jet");
  for (int i = 0; i < nJets; i++) {
    float jetPt = jets->at(i)->Get("pt");
    float jetEta = jets->at(i)->Get("eta");
    float jetBtagDeepB = jets->at(i)->Get("btagDeepB");
    if (jetPt > 30 && abs(jetEta) < 2.4) {
      jetsPt30++;
      if (jetBtagDeepB > 0.5) jetsBtagged++;
    }
  }

  if (jetsBtagged < 2) return false;
  if (jetsPt30 < 6) return false;
  return true;
}