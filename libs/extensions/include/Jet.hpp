//  Jet.hpp
//
//  Created by Jeremi Niedziela on 10/08/2023.

#ifndef Jet_hpp
#define Jet_hpp

#include "Helpers.hpp"
#include "PhysicsObject.hpp"

class Jet;
typedef Collection<std::shared_ptr<Jet>> Jets;

class Jet {
 public:
  Jet(std::shared_ptr<PhysicsObject> physicsObject_);

  auto Get(std::string branchName) { return physicsObject->Get(branchName); }
  float GetAsFloat(std::string branchName) { return physicsObject->GetAsFloat(branchName); }
  std::string GetOriginalCollection() { return physicsObject->GetOriginalCollection(); }
  void Reset() { physicsObject->Reset(); }

  inline float GetPt() { return physicsObject->Get("pt"); }
  inline float GetEta() { return physicsObject->Get("eta"); }
  inline float GetPhi() { return physicsObject->Get("phi"); }
  inline float GetMass() { return physicsObject->Get("mass"); }
  inline float GetDeepCSVscore() { return physicsObject->Get("btagDeepB"); }
  inline float GetDeepJetScore() { return physicsObject->Get("btagDeepFlavB"); }

  TLorentzVector GetFourVector();

 private:
  std::shared_ptr<PhysicsObject> physicsObject;
};

#endif /* Jet_hpp */
