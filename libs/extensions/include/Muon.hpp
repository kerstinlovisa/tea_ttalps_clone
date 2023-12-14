//  Muon.hpp
//
//  Created by Jeremi Niedziela on 10/08/2023.

#ifndef Muon_hpp
#define Muon_hpp

#include "Helpers.hpp"
#include "PhysicsObject.hpp"
#include "ScaleFactorsManager.hpp"

class Muon;
typedef Collection<std::shared_ptr<Muon>> Muons;

class Muon {
 public:
  Muon(std::shared_ptr<PhysicsObject> physicsObject_);

  auto Get(std::string branchName) { return physicsObject->Get(branchName); }
  float GetAsFloat(std::string branchName) { return physicsObject->GetAsFloat(branchName); }
  std::string GetOriginalCollection() { return physicsObject->GetOriginalCollection(); }
  void Reset() { physicsObject->Reset(); }

  inline float GetPt() { return physicsObject->Get("pt"); }
  inline float GetEta() { return physicsObject->Get("eta"); }
  inline float GetPhi() { return physicsObject->Get("phi"); }

  TLorentzVector GetFourVector();

  float GetScaleFactor();

  MuonID GetID();
  MuonIso GetIso();

  void Print(){
    info()<<"Muon: pt="<<GetPt()<<" eta="<<GetEta()<<" phi="<<GetPhi()<<std::endl;
    GetID().Print();
    GetIso().Print();
  }

 private:
  std::shared_ptr<PhysicsObject> physicsObject;
};

#endif /* Muon_hpp */
