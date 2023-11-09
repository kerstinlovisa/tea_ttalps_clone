#include "TTAlpsHistogramFiller.hpp"

#include "ConfigManager.hpp"
#include "ExtensionsHelpers.hpp"
#include "TTAlpsSelections.hpp"

using namespace std;

TTAlpsHistogramFiller::TTAlpsHistogramFiller(shared_ptr<HistogramsHandler> histogramsHandler_) : histogramsHandler(histogramsHandler_) {
  eventProcessor = make_unique<EventProcessor>();
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

  try {
    config.GetValue("weightsBranchName", weightsBranchName);
  } catch (const Exception &e) {
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
  auto maxPtObject = eventProcessor->GetMaxPtObject(event, params.collection);
  if(!maxPtObject) return;

  float pt = maxPtObject->Get("pt");
  if (params.collection == "Muon" || maxPtObject->GetOriginalCollection() == "Muon") {
    
    auto muon = asMuon(maxPtObject);
    float muonSF = muon->GetScaleFactor();

    histogramsHandler->Fill(histName, pt, weight * muonSF);
  } else {
    histogramsHandler->Fill(histName, pt, weight);
  }
}

void TTAlpsHistogramFiller::FillAllSubLeadingPt(const std::shared_ptr<Event> event, std::string histName, const HistogramParams &params) {
  float maxPt = eventProcessor->GetMaxPt(event, params.collection);
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  auto collection = event->GetCollection(params.collection);
  for (auto object : *collection) {
    float pt = object->Get("pt");
    if (pt == maxPt) continue;

    if (params.collection == "Muon" || object->GetOriginalCollection() == "Muon") {
      auto muon = asMuon(object);
      float muonSF = muon->GetScaleFactor();
      histogramsHandler->Fill(histName, pt, weight * muonSF);
    } else {
      histogramsHandler->Fill(histName, pt, weight);
    }
  }
}

void TTAlpsHistogramFiller::FillCustomTTAlpsVariables(const std::shared_ptr<Event> event) {
  for (auto &[histName, params] : ttalpsHistVariables) {
    if (params.variable == "subleadingPt")
      FillAllSubLeadingPt(event, histName, params);
    else if (params.variable == "leadingPt")
      FillLeadingPt(event, histName, params);
  }

  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }
  auto &scaleFactorsManager = ScaleFactorsManager::GetInstance();
  bool IsoMu24included = false;
  bool IsoMu50included = false;

  try {
    IsoMu24included = event->Get("HLT_IsoMu24");
  } catch (...) {
  }

  try {
    IsoMu50included = event->Get("HLT_IsoMu50");
  } catch (...) {
  }

  float leadingMuonPhi = -1;
  float leadingMuonPt = -1;
  float leadingMuonEta = -1;
  float leadingMuonMass = -1;
  float leadingMuonSF = 1;
  float leadingMuonTriggerSF = 1;

  for (auto object : *event->GetCollection("TightMuons")) {
    float muonPt = object->Get("pt");
    if (muonPt > leadingMuonPt) {
      auto muon = asMuon(object);
      leadingMuonPt = muonPt;
      leadingMuonPhi = muon->Get("phi");
      leadingMuonEta = muon->Get("eta");
      leadingMuonMass = muon->GetOriginalCollection() == "Muon" ? 0.105 : 0.000511;
      leadingMuonSF = muon->GetScaleFactor();
      leadingMuonTriggerSF = scaleFactorsManager.GetMuonTriggerScaleFactor(muon->GetEta(), muon->GetPt(), muon->GetID(), muon->GetIso(),
                                                                           IsoMu24included, IsoMu50included);
    }
  }

  auto looseMuons = event->GetCollection("LooseMuons");

  double zMass = 91.1876;  // GeV
  double smallestDifferenceToZmass = 999999;
  double massClosestToZ = -1;
  double deltaRclosestToZ = -1;
  double deltaEtaclosestToZ = -1;
  double deltaPhiclosestToZ = -1;
  float muon1SFsave = 1.0;
  float muon2SFsave = 1.0;
  
  for (int iMuon1 = 0; iMuon1 < looseMuons->size(); iMuon1++) {
    auto muon1 = asMuon(looseMuons->at(iMuon1));
    auto muon1fourVector = TLorentzVector();
    muon1fourVector.SetPtEtaPhiM(muon1->GetPt(), muon1->GetEta(), muon1->GetPhi(), 0.105);

    float muon1SF = muon1->GetScaleFactor();
    float triggerSF1 = scaleFactorsManager.GetMuonTriggerScaleFactor(muon1->GetEta(), muon1->GetPt(), muon1->GetID(), muon1->GetIso(),
                                                                     IsoMu24included, IsoMu50included);

    for (int iMuon2 = iMuon1 + 1; iMuon2 < looseMuons->size(); iMuon2++) {
      auto muon2 = asMuon(looseMuons->at(iMuon2));
      auto muon2fourVector = TLorentzVector();
      muon2fourVector.SetPtEtaPhiM(muon2->GetPt(), muon2->GetEta(), muon2->GetPhi(), 0.105);
      double diMuonMass = (muon1fourVector + muon2fourVector).M();

      float muon2SF = muon2->GetScaleFactor();
      float triggerSF2 = scaleFactorsManager.GetMuonTriggerScaleFactor(muon2->GetEta(), muon2->GetPt(), muon2->GetID(), muon2->GetIso(),
                                                                       IsoMu24included, IsoMu50included);

      if (fabs(diMuonMass - zMass) < smallestDifferenceToZmass) {
        smallestDifferenceToZmass = fabs(diMuonMass - zMass);
        massClosestToZ = diMuonMass;
        deltaRclosestToZ = muon1fourVector.DeltaR(muon2fourVector);
        deltaEtaclosestToZ = fabs(muon1fourVector.Eta() - muon2fourVector.Eta());
        deltaPhiclosestToZ = muon1fourVector.DeltaPhi(muon2fourVector);
        muon1SFsave = muon1SF;
        muon2SFsave = muon2SF;
      }
      histogramsHandler->Fill("LooseMuons_dimuonMinv", diMuonMass, weight * muon1SF * muon2SF * leadingMuonTriggerSF);
    }
  }

  float metPhi = event->Get("MET_phi");
  float metPt = event->Get("MET_pt");

  histogramsHandler->Fill("Event_METpt", metPt, weight);

 

  histogramsHandler->Fill("LooseMuons_dimuonMinvClosestToZ", massClosestToZ, weight * muon1SFsave * muon2SFsave * leadingMuonTriggerSF);
  histogramsHandler->Fill("LooseMuons_dimuonDeltaRclosestToZ", deltaRclosestToZ, weight * muon1SFsave * muon2SFsave * leadingMuonTriggerSF);
  histogramsHandler->Fill("LooseMuons_dimuonDeltaEtaclosestToZ", deltaEtaclosestToZ, weight * muon1SFsave * muon2SFsave * leadingMuonTriggerSF);
  histogramsHandler->Fill("LooseMuons_dimuonDeltaPhiclosestToZ", deltaPhiclosestToZ, weight * muon1SFsave * muon2SFsave * leadingMuonTriggerSF);

  TLorentzVector leadingMuon, metVector, muonPlusMet;
  leadingMuon.SetPtEtaPhiM(leadingMuonPt, leadingMuonEta, leadingMuonPhi, leadingMuonMass);
  metVector.SetPtEtaPhiM(metPt, 0, metPhi, 0);
  muonPlusMet = leadingMuon + metVector;

  histogramsHandler->Fill("TightMuons_deltaPhiMuonMET", metVector.DeltaPhi(leadingMuon), weight * leadingMuonSF * leadingMuonTriggerSF);
  histogramsHandler->Fill("TightMuons_minvMuonMET", muonPlusMet.M(), weight * leadingMuonSF * leadingMuonTriggerSF);

  auto bJets = event->GetCollection("GoodBtaggedJets");
  auto jets = event->GetCollection("GoodNonBtaggedJets");

  for (auto bJet : *bJets) {
    TLorentzVector bJetVector;
    bJetVector.SetPtEtaPhiM(bJet->Get("pt"), bJet->Get("eta"), bJet->Get("phi"), bJet->Get("mass"));

    for (int iJet = 0; iJet < jets->size(); iJet++) {
      TLorentzVector jet1vector;
      auto jet1 = jets->at(iJet);
      jet1vector.SetPtEtaPhiM(jet1->Get("pt"), jet1->Get("eta"), jet1->Get("phi"), jet1->Get("mass"));

      for (int jJet = iJet + 1; jJet < jets->size(); jJet++) {
        TLorentzVector jet2vector, sum;
        auto jet2 = jets->at(jJet);
        jet2vector.SetPtEtaPhiM(jet2->Get("pt"), jet2->Get("eta"), jet2->Get("phi"), jet2->Get("mass"));
        sum = bJetVector + jet1vector + jet2vector;

        histogramsHandler->Fill("GoodJets_minvBjet2jets", sum.M(), weight);

      } 
    }

  }

}

void TTAlpsHistogramFiller::FillGenParticleVariables(const std::shared_ptr<Event> event, std::string histName, std::string variable, int pdgid_) {
  
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  auto genParticles = event->GetCollection("GenPart");
  for(auto genpart : *genParticles)
  {
    auto genParticle = asGenParticle(genpart);
    int pdgid = genParticle->GetPdgId();
    if(abs(pdgid) == pdgid_ && genParticle->IsLastCopy()){
      float var = genpart->Get(variable);
      histogramsHandler->Fill(histName, var, weight);
    }
  }
}

void TTAlpsHistogramFiller::FillGenParticleBoost(const std::shared_ptr<Event> event, std::string histName, int pdgid_) {
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  auto genparticles = event->GetCollection("GenPart");
  for(auto genpart : *genparticles)
  {
    auto genParticle = asGenParticle(genpart);
    int pdgid = genParticle->GetPdgId();
    if(abs(pdgid) == pdgid_ && genParticle->IsLastCopy()){
      float px = genpart->Get("px");
      float py = genpart->Get("py");
      float pz = genpart->Get("pz");
      float mass = genpart->Get("mass");
      float boost = sqrt(px*px + py*py + pz*pz)/mass;
      histogramsHandler->Fill(histName, boost, weight);
    }
  }
}

void TTAlpsHistogramFiller::FillGenParticleVxyz(const std::shared_ptr<Event> event, std::string histName, int pdgid_) {
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  auto genparticles = event->GetCollection("GenPart");
  for(auto genpart : *genparticles)
  {
    auto genParticle = asGenParticle(genpart);
    int pdgid = genParticle->GetPdgId();
    if(abs(pdgid) == pdgid_ && genParticle->IsLastCopy()){
      float vx = genpart->Get("vx");
      float vy = genpart->Get("vy");
      float vz = genpart->Get("vz");
      float vxyz = sqrt(vx*vx + vy*vy + vz*vz);
      histogramsHandler->Fill(histName, vxyz, weight);
    }
  }
}

void TTAlpsHistogramFiller::FillGenParticleProperVxyz(const std::shared_ptr<Event> event, std::string histName, int pdgid_) {
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  auto genparticles = event->GetCollection("GenPart");
  for(auto genpart : *genparticles)
  {
    auto genParticle = asGenParticle(genpart);
    int pdgid = genParticle->GetPdgId();
    if(abs(pdgid) == pdgid_ && genParticle->IsLastCopy()){
      float vx = genpart->Get("vx");
      float vy = genpart->Get("vy");
      float vz = genpart->Get("vz");
      float vxyz = sqrt(vx*vx + vy*vy + vz*vz);
      float px = genpart->Get("px");
      float py = genpart->Get("py");
      float pz = genpart->Get("pz");
      float mass = genpart->Get("mass");
      float boost = sqrt(px*px + py*py + pz*pz)/mass;
      float proper_vxyz = vxyz/boost;
      histogramsHandler->Fill(histName, proper_vxyz, weight);
    }
  }
}

void TTAlpsHistogramFiller::FillGenMuonsFromALPs(const std::shared_ptr<Event> event, std::string histName, std::string variable) {
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
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

    float var;
    if(variable!="vxyz") var = genpart->Get(variable);
    else{
      float vx = genpart->Get("vx");
      float vy = genpart->Get("vy");
      float vz = genpart->Get("vz");
      var = sqrt(vx*vx + vy*vy + vz*vz);
    }
    
    histogramsHandler->Fill(histName, var, weight);
  }
}

void TTAlpsHistogramFiller::FillMuonVariables(const std::shared_ptr<Event> event, std::string histName, std::string collection, std::string variable) {
  
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  auto muons = event->GetCollection(collection);
  for(auto muon : *muons)
  {
    float var;
    if(variable == "chi2overndof"){
      float chi2 = muon->Get("chi2");
      float ndof = muon->Get("ndof");
      var = chi2/ndof;
    }
    else if(variable == "ptErroverpt"){
      float ptErr = muon->Get("ptErr");
      float pt = muon->Get("pt");
      var = ptErr/pt;
    }
    else if(variable == "DThitsCheck"){
      float trkNumDTHits = muon->Get("trkNumDTHits");
      float trkNumCSCHits = muon->Get("trkNumCSCHits");
      if(trkNumCSCHits > 0){
        var = 1;
      }
      else if(trkNumDTHits > 18) {
        var = 1;
      }
      else{
        var = 0;
      }
    }
    histogramsHandler->Fill(histName, var, weight);
  }
    }

void TTAlpsHistogramFiller::FillCustomLLPNanoAODVariables(const std::shared_ptr<Event> event) {

  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  for(auto &[histName, params] : ttalpsHistVariables) {
    if(histName == "GenALP_pdgId") {
      auto genparticles = event->GetCollection("GenPart");
      for(auto genpart : *genparticles)
      {
        int pdgid = genpart->Get("pdgId");
        if(pdgid == 54){
          histogramsHandler->Fill(histName, pdgid, weight);
        }
      }
    }
    else if(histName == "GenALP_mass") FillGenParticleVariables(event, histName, "mass", 54);
    else if(histName == "GenALP_vx") FillGenParticleVariables(event, histName, "vx", 54);
    else if(histName == "GenALP_vy") FillGenParticleVariables(event, histName, "vy", 54);
    else if(histName == "GenALP_vz") FillGenParticleVariables(event, histName, "vz", 54);
    else if(histName == "GenALP_pt") FillGenParticleVariables(event, histName, "pt", 54);
    else if(histName == "GenALP_boost") FillGenParticleBoost(event, histName, 54);
    else if(histName == "GenALP_vxyz") FillGenParticleVxyz(event, histName, 54);
    else if(histName == "GenALP_proper_vxyz") FillGenParticleProperVxyz(event, histName, 54);
    if(histName == "GenMuon_pdgId") {
      auto genparticles = event->GetCollection("GenPart");
      for(auto genpart : *genparticles)
      {
        int pdgid = genpart->Get("pdgId");
        if(pdgid == 13){
          histogramsHandler->Fill(histName, pdgid, weight);
        }
      }
    }
    else if(histName == "GenMuon_mass") FillGenParticleVariables(event, histName, "mass", 13);
    else if(histName == "GenMuon_vx") FillGenParticleVariables(event, histName, "vx", 13);
    else if(histName == "GenMuon_vy") FillGenParticleVariables(event, histName, "vy", 13);
    else if(histName == "GenMuon_vz") FillGenParticleVariables(event, histName, "vz", 13);
    else if(histName == "GenMuon_pt") FillGenParticleVariables(event, histName, "pt", 13);
    else if(histName == "GenMuon_boost") FillGenParticleBoost(event, histName, 13);
    else if(histName == "GenMuon_vxyz") FillGenParticleVxyz(event, histName, 13);
    else if(histName == "GenMuon_proper_vxyz") FillGenParticleProperVxyz(event, histName, 13);

    else if(histName == "GenMuonFromALP_vx") FillGenMuonsFromALPs(event, histName, "vx");
    else if(histName == "GenMuonFromALP_vy") FillGenMuonsFromALPs(event, histName, "vy");
    else if(histName == "GenMuonFromALP_vz") FillGenMuonsFromALPs(event, histName, "vz");
    else if(histName == "GenMuonFromALP_vxyz") FillGenMuonsFromALPs(event, histName, "vxyz");

    else if(histName == "DSAMuon_chi2overndof") FillMuonVariables(event, histName, "DSAMuon", "chi2overndof");
    else if(histName == "DSAMuon_ptErroverpt") FillMuonVariables(event, histName, "DSAMuon", "ptErroverpt");
    else if(histName == "DSAMuon_DThitsCheck") FillMuonVariables(event, histName, "DSAMuon", "DThitsCheck");
  }
}