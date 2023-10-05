#include "Muon.hpp"

TLorentzVector Muon::GetFourVector() { 
  TLorentzVector v;
  v.SetPtEtaPhiM(GetPt(), GetEta(), GetPhi(), 0.105);
  return v;
}