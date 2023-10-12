#include "TTAlpsHistogramFiller.hpp"

#include "ConfigManager.hpp"
#include "TTAlpsSelections.hpp"
#include "ExtensionsHelpers.hpp"

using namespace std;

TTAlpsHistogramFiller::TTAlpsHistogramFiller(shared_ptr<HistogramsHandler> histogramsHandler_)
    : histogramsHandler(histogramsHandler_) {
  eventProcessor = make_unique<EventProcessor>();
  auto &config = ConfigManager::GetInstance();

  try {
    config.GetMap("triggerSets", triggerSets);
    for (auto it = triggerSets.begin(); it != triggerSets.end(); ++it) triggerNames.push_back(it->first);
  }
  catch (const Exception& e){
    warn() << "Couldn't read triggerSets from config file ";
    warn() << "(which may be fine if you're not trying to apply trigger selection)" << endl;
  }

  try {
    config.GetHistogramsParams(defaultHistVariables, "defaultHistParams");
  }
  catch (const Exception& e){
    warn() << "Couldn't read defaultHistParams from config file - no default histograms will be included" << endl;
  }
  try {
    config.GetHistogramsParams(ttalpsHistVariables, "histParams");
  }
  catch (const Exception& e){
    warn() << "Couldn't read histParams from config file - no custom ttalps histograms will be included" << endl;
  }

  try {
    config.GetValue("weightsBranchName", weightsBranchName);
  } catch (const Exception& e) {
    warn() << "Weights branch not specified -- will assume weight is 1 for all events" << endl;
  }
}

TTAlpsHistogramFiller::~TTAlpsHistogramFiller() {}

bool TTAlpsHistogramFiller::EndsWithTriggerName(string name) {
  string lastPart = name.substr(name.rfind("_") + 1);
  return find(triggerNames.begin(), triggerNames.end(), lastPart) != triggerNames.end();
}

void TTAlpsHistogramFiller::FillTriggerEfficiencies() {
  TH1D *hist_tmp;

  for (auto &[name, hist] : histogramsHandler->GetHistograms1D()) {
    if (!EndsWithTriggerName(name)) continue;
    string nameWithoutTrigger = name.substr(0, name.rfind("_"));
    string newName = name + "_eff";
    hist_tmp = (TH1D *)histogramsHandler->GetHistogram1D(name)->Clone(newName.c_str());
    hist_tmp->Divide(hist_tmp, histogramsHandler->GetHistogram1D(nameWithoutTrigger), 1, 1, "B");
    histogramsHandler->SetHistogram1D(newName, hist_tmp);
  }
}

void TTAlpsHistogramFiller::FillTriggerVariables(const std::shared_ptr<Event> event, std::string prefix, std::string suffix) {
  if (prefix != "") prefix = prefix + "_";
  if (suffix != "") suffix = "_" + suffix;

  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  histogramsHandler->Fill(prefix + "muonMaxPt" + suffix, eventProcessor->GetMaxPt(event, "Muon"), weight);
  histogramsHandler->Fill(prefix + "eleMaxPt" + suffix, eventProcessor->GetMaxPt(event, "Electron"), weight);
  histogramsHandler->Fill(prefix + "jetMaxPt" + suffix, eventProcessor->GetMaxPt(event, "Jet"), weight);
  histogramsHandler->Fill(prefix + "jetHt" + suffix, eventProcessor->GetHt(event, "Jet"), weight);
}

void TTAlpsHistogramFiller::FillTriggerVariablesPerTriggerSet(const std::shared_ptr<Event> event, std::string ttbarCategory) {
  auto ttAlpsSelections = make_unique<TTAlpsSelections>();

  bool passesSingleLepton = ttAlpsSelections->PassesSingleLeptonSelections(event);
  bool passesDilepton = ttAlpsSelections->PassesDileptonSelections(event);
  bool passesHadron = ttAlpsSelections->PassesHadronSelections(event);

  for (auto &[triggerSetName, triggerSet] : triggerSets) {
    bool passesTrigger = false;

    for (auto &triggerName : triggerSet) {
      passesTrigger = event->Get(triggerName);
      if (passesTrigger) break;
    }
    if (!passesTrigger) continue;

    FillTriggerVariables(event, ttbarCategory, triggerSetName);
    if (passesSingleLepton) FillTriggerVariables(event, ttbarCategory, triggerSetName + "_singleLepton");
    if (passesDilepton) FillTriggerVariables(event, ttbarCategory, triggerSetName + "_dilepton");
    if (passesHadron) FillTriggerVariables(event, ttbarCategory, triggerSetName + "_hadron");
  }
}

void TTAlpsHistogramFiller::FillNormCheck(const std::shared_ptr<Event> event) {
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }
  
  histogramsHandler->Fill("Event_normCheck", 0.5, weight);
}

void TTAlpsHistogramFiller::FillLeadingPt(const std::shared_ptr<Event> event, std::string histName, const HistogramParams &params) {
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }
  float maxPt = eventProcessor->GetMaxPt(event, params.collection);
  if(maxPt < 0) return;
  histogramsHandler->Fill(histName, maxPt, weight);
}

void TTAlpsHistogramFiller::FillAllSubLeadingPt(const std::shared_ptr<Event> event, std::string histName, const HistogramParams &params) {
  
  float maxPt = eventProcessor->GetMaxPt(event, params.collection);
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  auto collection = event->GetCollection(params.collection);
    for(auto object : *collection){
      float pt = object->Get("pt");
      if(pt == maxPt) continue;
      histogramsHandler->Fill(histName, pt, weight);
    }
}

void TTAlpsHistogramFiller::FillCustomTTAlpsVariables(const std::shared_ptr<Event> event) {

  for(auto &[histName, params] : ttalpsHistVariables) {
    if(params.variable == "subleadingPt") FillAllSubLeadingPt(event, histName, params);
    else if(params.variable == "leadingPt") FillLeadingPt(event, histName, params);
  }

  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  auto almostGoodMuons = event->GetCollection("AlmostGoodMuons");

  double zMass = 91.1876; // GeV
  double smallestDifferenceToZmass = 999999;
  double massClosestToZ = -1;
  double deltaRclosestToZ = -1;

  for(int iMuon1=0; iMuon1 < almostGoodMuons->size(); iMuon1++){
    auto muon1 = asMuon(almostGoodMuons->at(iMuon1));
    auto muon1fourVector = TLorentzVector();
    muon1fourVector.SetPtEtaPhiM(muon1->GetPt(), muon1->GetEta(), muon1->GetPhi(), 0.105);
    
    for(int iMuon2=iMuon1+1; iMuon2 < almostGoodMuons->size(); iMuon2++){
      auto muon2 = asMuon(almostGoodMuons->at(iMuon2));
      auto muon2fourVector = TLorentzVector();
      muon2fourVector.SetPtEtaPhiM(muon2->GetPt(), muon2->GetEta(), muon2->GetPhi(), 0.105);
      double diMuonMass = (muon1fourVector + muon2fourVector).M();

      if(fabs(diMuonMass-zMass) < smallestDifferenceToZmass){
        smallestDifferenceToZmass = fabs(diMuonMass-zMass);
        massClosestToZ = diMuonMass;
        deltaRclosestToZ = muon1fourVector.DeltaR(muon2fourVector);
      }

      histogramsHandler->Fill("AlmostGoodMuons_dimuonMinv", diMuonMass, weight);    
    }
  }

  histogramsHandler->Fill("AlmostGoodMuons_dimuonMinvClosestToZ", massClosestToZ, weight);
  histogramsHandler->Fill("AlmostGoodMuons_dimuonDeltaRclosestToZ", deltaRclosestToZ, weight);

  float metPhi = event->Get("MET_phi");
  float metPt = event->Get("MET_pt");

  histogramsHandler->Fill("Event_METpt", metPt, weight);

  float leadingLeptonPhi = -1;
  float leadingLeptonPt = -1;
  float leadingLeptonEta = -1;
  float leadingLeptonMass = -1;

  for(auto lepton : *event->GetCollection("GoodLeptons")){
    float leptonPt = lepton->Get("pt");
    if(leptonPt > leadingLeptonPt){
      leadingLeptonPt = leptonPt;
      leadingLeptonPhi = lepton->Get("phi");
      leadingLeptonEta = lepton->Get("eta");
      leadingLeptonMass = lepton->GetOriginalCollection()=="Muon" ? 0.105 : 0.000511;
    }
  }

  

  TLorentzVector leadingLepton, metVector, leptonPlusMet;
  leadingLepton.SetPtEtaPhiM(leadingLeptonPt, leadingLeptonEta, leadingLeptonPhi, leadingLeptonMass);
  metVector.SetPtEtaPhiM(metPt, 0, metPhi, 0);
  leptonPlusMet = leadingLepton + metVector;

  histogramsHandler->Fill("GoodLeptons_deltaPhiLeptonMET", metVector.DeltaPhi(leadingLepton), weight);
  histogramsHandler->Fill("GoodLeptons_minvLeptonMET", leptonPlusMet.M(), weight);

  auto bJets = event->GetCollection("GoodBtaggedJets");
  auto jets = event->GetCollection("GoodNonBtaggedJets");

  for(auto bJet : *bJets){
    TLorentzVector bJetVector;
    bJetVector.SetPtEtaPhiM(bJet->Get("pt"), bJet->Get("eta"), bJet->Get("phi"), bJet->Get("mass"));

    for(int iJet=0; iJet<jets->size(); iJet++){
      TLorentzVector jet1vector;
      auto jet1 = jets->at(iJet);
      jet1vector.SetPtEtaPhiM(jet1->Get("pt"), jet1->Get("eta"), jet1->Get("phi"), jet1->Get("mass"));

      for(int jJet=iJet+1; jJet<jets->size(); jJet++){
        TLorentzVector jet2vector, sum;
        auto jet2 = jets->at(jJet);
        jet2vector.SetPtEtaPhiM(jet2->Get("pt"), jet2->Get("eta"), jet2->Get("phi"), jet2->Get("mass"));
        sum = bJetVector + jet1vector + jet2vector;

        histogramsHandler->Fill("GoodJets_minvBjet2jets", sum.M(), weight);

      } 
    }

  }

}
