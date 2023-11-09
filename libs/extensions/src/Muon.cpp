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
  auto &scaleFactorsManager = ScaleFactorsManager::GetInstance();
  float recoSF = scaleFactorsManager.GetMuonRecoScaleFactor(fabs(GetEta()), GetPt());

  auto id = GetID();
  float idSF = scaleFactorsManager.GetMuonIDScaleFactor(fabs(GetEta()), GetPt(), id);

  auto iso = GetIso();
  float isoSF = scaleFactorsManager.GetMuonIsoScaleFactor(fabs(GetEta()), GetPt(), id, iso);

  return recoSF * idSF * isoSF;
}

MuonID Muon::GetID() {
  UChar_t highPtID = Get("highPtId");
  return MuonID(Get("softId"), highPtID == 2, highPtID == 1, Get("tightId"), Get("mediumPromptId"), Get("mediumId"), Get("looseId"));
}

MuonIso Muon::GetIso() {
  UChar_t pfIso = Get("pfIsoId");
  UChar_t tkIso = Get("tkIsoId");
  return MuonIso(tkIso == 1, tkIso == 2, pfIso == 1, pfIso == 2, pfIso == 3, pfIso == 4, pfIso == 5, pfIso == 6);
}