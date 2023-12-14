#include "TTAlpsHistogramFiller.hpp"

#include "ConfigManager.hpp"
#include "ExtensionsHelpers.hpp"
#include "TTAlpsSelections.hpp"
#include "UserExtensionsHelpers.hpp"

using namespace std;

TTAlpsHistogramFiller::TTAlpsHistogramFiller(shared_ptr<HistogramsHandler> histogramsHandler_) : histogramsHandler(histogramsHandler_) {
  eventProcessor = make_unique<EventProcessor>();
  nanoEventProcessor = make_unique<NanoEventProcessor>();
  auto &config = ConfigManager::GetInstance();

  try {
    config.GetMap("triggerSets", triggerSets);
    for (auto it = triggerSets.begin(); it != triggerSets.end(); ++it) triggerNames.push_back(it->first);
  } catch (const Exception &e) {
    warn() << "Couldn't read triggerSets from config file ";
    warn() << "(which may be fine if you're not trying to apply trigger selection)" << endl;
  }

  try {
    config.GetHistogramsParams(defaultHistVariables, "defaultHistParams");
  } catch (const Exception &e) {
    warn() << "Couldn't read defaultHistParams from config file - no default histograms will be included" << endl;
  }
  try {
    config.GetHistogramsParams(ttalpsHistVariables, "histParams");
  } catch (const Exception &e) {
    warn() << "Couldn't read histParams from config file - no custom ttalps histograms will be included" << endl;
  }
}

TTAlpsHistogramFiller::~TTAlpsHistogramFiller() {}

float TTAlpsHistogramFiller::GetEventWeight(const shared_ptr<Event> event) {
  float genWeight = nanoEventProcessor->GetGenWeight(event);
  float pileupSF = nanoEventProcessor->GetPileupScaleFactor(event);
  float muonTriggerSF = nanoEventProcessor->GetMuonTriggerScaleFactor(event);

  return genWeight * pileupSF * muonTriggerSF;
}

bool TTAlpsHistogramFiller::EndsWithTriggerName(string name) {
  string lastPart = name.substr(name.rfind("_") + 1);
  return find(triggerNames.begin(), triggerNames.end(), lastPart) != triggerNames.end();
}

void TTAlpsHistogramFiller::FillDefaultVariables(const shared_ptr<Event> event) {
  for (auto &[title, params] : defaultHistVariables) {
    string collectionName = params.collection;
    string branchName = params.variable;

    float value;
    float weight = GetEventWeight(event);

    if (collectionName == "Event") {
      if (branchName[0] == 'n') {
        value = event->GetCollectionSize(branchName.substr(1));
      } else {
        value = event->GetAsFloat(branchName);
      }
      histogramsHandler->Fill(title, value, weight);
    } else {
      auto collection = event->GetCollection(collectionName);
      for (auto object : *collection) {
        value = object->GetAsFloat(branchName);
        if (collectionName == "Muon" || object->GetOriginalCollection() == "Muon") {
          weight *= asMuon(object)->GetScaleFactor();
        }
        histogramsHandler->Fill(title, value, weight);
      }
    }
  }
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

void TTAlpsHistogramFiller::FillTriggerVariables(const shared_ptr<Event> event, string prefix, string suffix) {
  if (prefix != "") prefix = prefix + "_";
  if (suffix != "") suffix = "_" + suffix;

  float weight = nanoEventProcessor->GetGenWeight(event);

  histogramsHandler->Fill(prefix + "muonMaxPt" + suffix, eventProcessor->GetMaxPt(event, "Muon"), weight);
  histogramsHandler->Fill(prefix + "eleMaxPt" + suffix, eventProcessor->GetMaxPt(event, "Electron"), weight);
  histogramsHandler->Fill(prefix + "jetMaxPt" + suffix, eventProcessor->GetMaxPt(event, "Jet"), weight);
  histogramsHandler->Fill(prefix + "jetHt" + suffix, eventProcessor->GetHt(event, "Jet"), weight);
}

void TTAlpsHistogramFiller::FillTriggerVariablesPerTriggerSet(const shared_ptr<Event> event, string ttbarCategory) {
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

void TTAlpsHistogramFiller::FillNormCheck(const shared_ptr<Event> event) {
  float weight = nanoEventProcessor->GetGenWeight(event);
  histogramsHandler->Fill("Event_normCheck", 0.5, weight);
}

void TTAlpsHistogramFiller::FillLeadingPt(const shared_ptr<Event> event, string histName, const HistogramParams &params) {
  auto maxPtObject = eventProcessor->GetMaxPtObject(event, params.collection);
  if (!maxPtObject) return;

  float weight = GetEventWeight(event);

  if (params.collection == "Muon" || maxPtObject->GetOriginalCollection() == "Muon") {
    weight *= asMuon(maxPtObject)->GetScaleFactor();
  }
  histogramsHandler->Fill(histName, maxPtObject->Get("pt"), weight);
}

void TTAlpsHistogramFiller::FillAllSubLeadingPt(const shared_ptr<Event> event, string histName, const HistogramParams &params) {
  float maxPt = eventProcessor->GetMaxPt(event, params.collection);

  auto collection = event->GetCollection(params.collection);

  for (auto object : *collection) {
    float pt = object->Get("pt");
    if (pt == maxPt) continue;
    float weight = GetEventWeight(event);

    if (params.collection == "Muon" || object->GetOriginalCollection() == "Muon") {
      weight *= asMuon(object)->GetScaleFactor();
    }
    histogramsHandler->Fill(histName, pt, weight);
  }
}

void TTAlpsHistogramFiller::FillDimuonHistograms(const shared_ptr<Event> event) {
  float weight = GetEventWeight(event);

  auto looseMuons = event->GetCollection("LooseMuons");
  for (int iMuon1 = 0; iMuon1 < looseMuons->size(); iMuon1++) {
    auto muon1 = asMuon(looseMuons->at(iMuon1));
    float muon1SF = muon1->GetScaleFactor();
    TLorentzVector muon1vector = muon1->GetFourVector();

    for (int iMuon2 = iMuon1 + 1; iMuon2 < looseMuons->size(); iMuon2++) {
      auto muon2 = asMuon(looseMuons->at(iMuon2));
      float muon2SF = muon2->GetScaleFactor();
      TLorentzVector muon2vector = muon2->GetFourVector();
      histogramsHandler->Fill("LooseMuons_dimuonMinv", (muon1vector + muon2vector).M(), weight * muon1SF * muon2SF);
    }
  }
}

void TTAlpsHistogramFiller::FillDiumonClosestToZhistgrams(const shared_ptr<Event> event) {
  if (event->GetCollectionSize("LooseMuons") < 2) {
    warn() << "Not enough muons in event to fill dimuon histograms" << endl;
    return;
  }

  float weight = GetEventWeight(event);
  auto [muon1, muon2] = nanoEventProcessor->GetMuonPairClosestToZ(event, "LooseMuons");

  TLorentzVector muon1fourVector = muon1->GetFourVector();
  TLorentzVector muon2fourVector = muon2->GetFourVector();

  float massClosestToZ = (muon1fourVector + muon2fourVector).M();
  float deltaRclosestToZ = muon1fourVector.DeltaR(muon2fourVector);
  float deltaEtaclosestToZ = fabs(muon1fourVector.Eta() - muon2fourVector.Eta());
  float deltaPhiclosestToZ = muon1fourVector.DeltaPhi(muon2fourVector);
  float muon1SF = muon1->GetScaleFactor();
  float muon2SF = muon2->GetScaleFactor();

  histogramsHandler->Fill("LooseMuons_dimuonMinvClosestToZ", massClosestToZ, weight * muon1SF * muon2SF);
  histogramsHandler->Fill("LooseMuons_dimuonDeltaRclosestToZ", deltaRclosestToZ, weight * muon1SF * muon2SF);
  histogramsHandler->Fill("LooseMuons_dimuonDeltaEtaclosestToZ", deltaEtaclosestToZ, weight * muon1SF * muon2SF);
  histogramsHandler->Fill("LooseMuons_dimuonDeltaPhiclosestToZ", deltaPhiclosestToZ, weight * muon1SF * muon2SF);
}

void TTAlpsHistogramFiller::FillMuonMetHistograms(const shared_ptr<Event> event) {
  float weight = GetEventWeight(event);

  auto leadingTightMuon = asMuon(eventProcessor->GetMaxPtObject(event, "TightMuons"));
  float leadingMuonSF = leadingTightMuon->GetScaleFactor();

  TLorentzVector leadingMuonVector = leadingTightMuon->GetFourVector();
  TLorentzVector metVector = asNanoEvent(event)->GetMetFourVector();

  histogramsHandler->Fill("TightMuons_deltaPhiMuonMET", metVector.DeltaPhi(leadingMuonVector), weight * leadingMuonSF);
  histogramsHandler->Fill("TightMuons_minvMuonMET", (leadingMuonVector + metVector).M(), weight * leadingMuonSF);
}

void TTAlpsHistogramFiller::FillJetHistograms(const shared_ptr<Event> event){
  float weight = GetEventWeight(event);
  auto bJets = event->GetCollection("GoodTightBtaggedJets");
  auto jets = event->GetCollection("GoodNonTightBtaggedJets");

  for (auto bJet : *bJets) {
    TLorentzVector bJetVector = asJet(bJet)->GetFourVector();

    for (int iJet = 0; iJet < jets->size(); iJet++) {
      TLorentzVector jet1vector = asJet(jets->at(iJet))->GetFourVector();

      for (int jJet = iJet + 1; jJet < jets->size(); jJet++) {
        TLorentzVector jet2vector = asJet(jets->at(jJet))->GetFourVector();
        histogramsHandler->Fill("GoodJets_minvBjet2jets", (bJetVector + jet1vector + jet2vector).M(), weight);
      }
    }
  }
}

void TTAlpsHistogramFiller::FillLooseDSAMuonsHistograms(const shared_ptr<Event> event){
  float weight = GetEventWeight(event);
  auto looseDSAMuons = event->GetCollection("LooseDSAMuons");

  float nLooseDSAMuons = looseDSAMuons->size();
  histogramsHandler->Fill("Event_nLooseDSAMuons", nLooseDSAMuons, weight);

  for(auto dsaMuonObj : *looseDSAMuons){
    float dxy = dsaMuonObj->Get("dxyPV");
    float dz = dsaMuonObj->Get("dzPV");
    float pt = dsaMuonObj->Get("pt");
    float eta = dsaMuonObj->Get("eta");

    histogramsHandler->Fill("LooseDSAMuons_dxy", dxy, weight);
    histogramsHandler->Fill("LooseDSAMuons_dz", dz, weight);
    histogramsHandler->Fill("LooseDSAMuons_pt", pt, weight);
    histogramsHandler->Fill("LooseDSAMuons_eta", eta, weight);
  }


}

void TTAlpsHistogramFiller::FillAllLooseMuonsHistograms(const shared_ptr<Event> event){
  float weight = GetEventWeight(event);
  auto looseMuons = event->GetCollection("LooseMuons");
  auto looseDsaMuons = event->GetCollection("LooseDSAMuons");

  PhysicsObjects allLooseMuons;

  float min_deltaR = 99999;
  float pt, eta, dxy, dz, dxyPV, dzPV;

  for(auto muonObj : *looseMuons){
    auto muon = asMuon(muonObj);
    auto muonP4 = muon->GetFourVector();

    allLooseMuons.push_back(muonObj);

    float dxy = muonObj->Get("dxy");
    float dz = muonObj->Get("dz");
    pt = muonObj->Get("pt");
    eta = muonObj->Get("eta");

    histogramsHandler->Fill("AllLooseMuons_dxy", dxy, weight);
    histogramsHandler->Fill("AllLooseMuons_dz", dz, weight);
    histogramsHandler->Fill("AllLooseMuons_pt", pt, weight);
    histogramsHandler->Fill("AllLooseMuons_eta", eta, weight);

    for(auto dsaMuonObj : *looseDsaMuons){
      auto dsaMuon = asMuon(dsaMuonObj);
      auto dsaMuonP4 = dsaMuon->GetFourVector();
      
      if(muonP4.DeltaR(dsaMuonP4) < 0.01) continue;

      float dxyPV = dsaMuonObj->Get("dxyPV");
      float dzPV = dsaMuonObj->Get("dzPV");
      pt = dsaMuonObj->Get("pt");
      eta = dsaMuonObj->Get("eta");
      histogramsHandler->Fill("AllLooseMuons_pt", pt, weight);
      histogramsHandler->Fill("AllLooseMuons_eta", eta, weight);
      histogramsHandler->Fill("AllLooseMuons_dxy", dxyPV, weight);
      histogramsHandler->Fill("AllLooseMuons_dz", dzPV, weight);
      allLooseMuons.push_back(dsaMuonObj);
    }
  }
  float nAllLooseMuons = allLooseMuons.size();
  histogramsHandler->Fill("Event_nAllLooseMuons", nAllLooseMuons, weight);
  if (nAllLooseMuons < 2) {
    warn() << "Not enough total muons in event to fill dimuon histograms" << endl;
    return;
  }

  for (int iMuon1 = 0; iMuon1 < allLooseMuons.size(); iMuon1++) {
    auto muon1 = asMuon(allLooseMuons.at(iMuon1));
    TLorentzVector muon1vector = muon1->GetFourVector();

    for (int iMuon2 = iMuon1 + 1; iMuon2 < allLooseMuons.size(); iMuon2++) {
      auto muon2 = asMuon(allLooseMuons.at(iMuon2));
      TLorentzVector muon2vector = muon2->GetFourVector();
      float deltaR = muon1vector.DeltaR(muon2vector);
      min_deltaR = std::min(min_deltaR,deltaR);
      histogramsHandler->Fill("AllLooseMuons_deltaR", deltaR, weight);
    }
  }
  histogramsHandler->Fill("AllLooseMuons_minDeltaR", min_deltaR, weight);
}

void TTAlpsHistogramFiller::FillCustomTTAlpsVariables(const shared_ptr<Event> event) {
  for (auto &[histName, params] : ttalpsHistVariables) {
    if (params.variable == "subleadingPt") {
      FillAllSubLeadingPt(event, histName, params);
    } else if (params.variable == "leadingPt") {
      FillLeadingPt(event, histName, params);
    }
  }
  FillDimuonHistograms(event);
  FillDiumonClosestToZhistgrams(event);
  FillMuonMetHistograms(event);
  FillJetHistograms(event);
  FillLooseDSAMuonsHistograms(event);
  FillAllLooseMuonsHistograms(event);
}

void TTAlpsHistogramFiller::FillGenMuonsFromALPs(const std::shared_ptr<Event> event) {
  float weight = 1.0;
  try {
    weight = GetEventWeight(event);
  } catch (...) {
  }

  auto genParticles = event->GetCollection("GenPart");
  for(auto genpart : *genParticles)
  {
    auto genParticle = asGenParticle(genpart);
    int pdgid = genParticle->GetPdgId();
    if(abs(pdgid) != 13) continue;

    int motherIndex = genParticle->GetMotherIndex();
    if (motherIndex < 0) continue;
    auto mother = asGenParticle(genParticles->at(motherIndex));
    int mother_pdgid = mother->GetPdgId();
    if(mother_pdgid != 54) continue;
    
    float vx = genpart->Get("vx");
    float vy = genpart->Get("vy");
    float vz = genpart->Get("vz");
    float pt = genpart->Get("pt");
    float mass = genpart->Get("mass");
    float boost = abs(pt)/mass;
    float vxy = sqrt(vx*vx + vy*vy);
    float proper_vxy = vxy/boost;
    histogramsHandler->Fill("GenMuonFromALP_vx"         , vx,          weight);
    histogramsHandler->Fill("GenMuonFromALP_vy"         , vy,          weight);
    histogramsHandler->Fill("GenMuonFromALP_vz"         , vz,          weight);
    histogramsHandler->Fill("GenMuonFromALP_pt"         , pt,          weight);
    histogramsHandler->Fill("GenMuonFromALP_mass"       , mass,        weight);
    histogramsHandler->Fill("GenMuonFromALP_boost"      , boost,       weight);
    histogramsHandler->Fill("GenMuonFromALP_vxy"        , vxy,         weight);
    histogramsHandler->Fill("GenMuonFromALP_proper_vxy" , proper_vxy,  weight);
  }
}

void TTAlpsHistogramFiller::FillCustomLLPNanoAODVariables(const std::shared_ptr<Event> event) {

  float weight = 1.0;
  try {
    weight = GetEventWeight(event);
  } catch (...) {
  }
  
  // GenMuons from ALPs
  FillGenMuonsFromALPs(event);

  // DSAMuon variables

  int nDSAMuons = 0;
  int nDSAMuons_pt5 = 0;
  auto dsamuons = event->GetCollection("DSAMuon");
  for(auto dsamuon : *dsamuons)
  {
    float chi2 = dsamuon->Get("chi2");
    float ndof = dsamuon->Get("ndof");
    histogramsHandler->Fill("DSAMuon_chi2overndof", chi2/ndof, weight);
    float ptErr = dsamuon->Get("ptErr");
    float pt = dsamuon->Get("pt");
    histogramsHandler->Fill("DSAMuon_ptErroverpt", chi2/ndof, weight);
    int displacedId = dsamuon->Get("displacedId");
    histogramsHandler->Fill("DSAMuon_displacedId", displacedId, weight);

    // auto DSAMuon = asDSAMuon(dsamuon);
    // if(DSAMuon->passesDSAID()) nDSAMuons = nDSAMuons + 1;
    // if(DSAMuon->passesDSAID(5)) nDSAMuons_pt5 = nDSAMuons_pt5 + 1;

    float dxy = dsamuon->Get("dxy");
    float dz = dsamuon->Get("dz");

    // eta regions
    float eta = dsamuon->Get("eta");
    if(eta <0.9){
      histogramsHandler->Fill("DSAMuon_dxy_eta-max0p9", dxy, weight);
      histogramsHandler->Fill("DSAMuon_dz_eta-max0p9", dz, weight);
    }
    else if(eta <1.2){
      histogramsHandler->Fill("DSAMuon_dxy_eta-max1p2", dxy, weight);
      histogramsHandler->Fill("DSAMuon_dz_eta-max1p2", dz, weight);
    } 
    else if(eta <2.4){
      histogramsHandler->Fill("DSAMuon_dxy_eta-max2p4", dxy, weight);
      histogramsHandler->Fill("DSAMuon_dz_eta-max2p4", dz, weight);
    }

  }
  histogramsHandler->Fill("nDSAMuonID", nDSAMuons, weight);
  histogramsHandler->Fill("nDSAMuonIDPt5", nDSAMuons_pt5, weight);

  // Muons
  int j = 0;
  auto muons = event->GetCollection("Muon");
  auto muons_extended = event->GetCollection("MuonExtended");
  for(auto muon : *muons){
    auto muon_extended = muons_extended->at(j);
    float dxy = muon->Get("dxy");
    float dz = muon->Get("dz");
    float dxy_extended = muon_extended->Get("dxyPV");
    float dz_extended = muon_extended->Get("dzPV");
    histogramsHandler->Fill("MuonDxyDiff", dxy-dxy_extended, weight);
    histogramsHandler->Fill("MuonDzDiff", dz-dz_extended, weight);
    float eta = muon->Get("eta");
    float eta_extended = muon->Get("eta");
    histogramsHandler->Fill("MuonEtaDiff", eta-eta_extended, weight);

    // eta regions
    if(eta < 0.9){
      histogramsHandler->Fill("Muon_dxy_eta-max0p9", dxy, weight);
      histogramsHandler->Fill("Muon_dz_eta-max0p9", dz, weight);
    }
    else if(eta < 1.2){
      histogramsHandler->Fill("Muon_dxy_eta-max1p2", dxy, weight);
      histogramsHandler->Fill("Muon_dz_eta-max1p2", dz, weight);
    } 
    else if(eta < 2.4){
      histogramsHandler->Fill("Muon_dxy_eta-max2p4", dxy, weight);
      histogramsHandler->Fill("Muon_dz_eta-max2p4", dz, weight);
    }
    if(eta_extended < 0.9){
      histogramsHandler->Fill("MuonExtended_dxy_eta-max0p9", dxy_extended, weight);
      histogramsHandler->Fill("MuonExtended_dz_eta-max0p9", dz_extended, weight);
    }
    else if(eta_extended < 1.2){
      histogramsHandler->Fill("MuonExtended_dxy_eta-max1p2", dxy_extended, weight);
      histogramsHandler->Fill("MuonExtended_dz_eta-max1p2", dz_extended, weight);
    } 
    else if(eta_extended < 2.4){
      histogramsHandler->Fill("MuonExtended_dxy_eta-max2p4", dxy_extended, weight);
      histogramsHandler->Fill("MuonExtended_dz_eta-max2p4", dz_extended, weight);
    }

    j++;

  }

}
