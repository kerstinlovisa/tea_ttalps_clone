#include "Muon.hpp"
#include "ConfigManager.hpp"

using namespace std;

Muon::Muon(shared_ptr<PhysicsObject> physicsObject_) : physicsObject(physicsObject_) {}

TLorentzVector Muon::GetFourVector() {
  TLorentzVector v;
  v.SetPtEtaPhiM(GetPt(), GetEta(), GetPhi(), 0.105);
  return v;
}

float Muon::GetScaleFactor() {
  auto &config = ConfigManager::GetInstance();
  bool applyMuonScaleFactors;
  config.GetValue("applyMuonScaleFactors", applyMuonScaleFactors);
  if(!applyMuonScaleFactors) return 1;

  auto &scaleFactorsManager = ScaleFactorsManager::GetInstance();
  float recoSF = scaleFactorsManager.GetMuonRecoScaleFactor(GetEta(), GetPt());

  UChar_t highPtID = Get("highPtId");
  auto id = MuonID(Get("softId"), highPtID == 2, highPtID == 1, Get("tightId"), Get("mediumPromptId"), Get("mediumId"), Get("looseId"));
  float idSF = scaleFactorsManager.GetMuonIDScaleFactor(GetEta(), GetPt(), id);

  UChar_t pfIso = Get("pfIsoId");
  UChar_t tkIso = Get("tkIsoId");

  auto iso = MuonIso(tkIso == 1, tkIso == 2, pfIso == 1, pfIso == 2, pfIso == 3, pfIso == 4, pfIso == 5, pfIso == 6);
  float isoSF = scaleFactorsManager.GetMuonIsoScaleFactor(GetEta(), GetPt(), id, iso);

  return recoSF * idSF * isoSF;
}