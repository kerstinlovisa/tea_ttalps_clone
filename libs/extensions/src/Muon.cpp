#include "Muon.hpp"

using namespace std;

Muon::Muon(shared_ptr<PhysicsObject> physicsObject_) : physicsObject(physicsObject_) {
  

}

TLorentzVector Muon::GetFourVector() {
  TLorentzVector v;
  v.SetPtEtaPhiM(GetPt(), GetEta(), GetPhi(), 0.105);
  return v;
}

float Muon::GetRecoScaleFactor() {
  auto &scaleFactorsManager = ScaleFactorsManager::GetInstance();
  return scaleFactorsManager.GetMuonRecoScaleFactor(GetEta(), GetPt());
}