#include "Muon.hpp"

using namespace std;

Muon::Muon(shared_ptr<PhysicsObject> physicsObject_) : physicsObject(physicsObject_) {}

TLorentzVector Muon::GetFourVector() {
  TLorentzVector v;
  v.SetPtEtaPhiM(GetPt(), GetEta(), GetPhi(), 0.105);
  return v;
}

float Muon::GetScaleFactor() {
  auto &scaleFactorsManager = ScaleFactorsManager::GetInstance();
  float recoSF = scaleFactorsManager.GetMuonRecoScaleFactor(GetEta(), GetPt());

  UChar_t highPtID = Get("highPtId");
  auto id = MuonID(Get("softId"), highPtID == 2, highPtID == 1, Get("tightId"), Get("mediumPromptId"), Get("mediumId"), Get("looseId"));
  float idSF = scaleFactorsManager.GetMuonIDScaleFactor(GetEta(), GetPt(), id);

  return recoSF * idSF;
}