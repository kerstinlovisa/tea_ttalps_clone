//  TTAlpsEvent.hpp
//
//  Created by Jeremi Niedziela on 1/09/2023.

#ifndef TTAlpsEvent_hpp
#define TTAlpsEvent_hpp

#include "Event.hpp"
#include "Helpers.hpp"

class TTAlpsEvent {
 public:
  TTAlpsEvent(std::shared_ptr<Event> event_) : event(event_) {}

  auto Get(std::string branchName) { return event->Get(branchName); }
  std::shared_ptr<PhysicsObjects> GetCollection(std::string name) const { return event->GetCollection(name); }
  int GetCollectionSize(std::string name) { return event->GetCollectionSize(name); }
  void AddExtraCollection(std::string name, std::shared_ptr<PhysicsObjects> collection) { event->AddExtraCollection(name, collection); }
  
  std::string GetTTbarEventCategory();
  
 private:
  std::shared_ptr<Event> event;

  std::vector<int> GetTopIndices();
  std::vector<int> GetBottomIndices();
  bool IsGoodParticle(int particleIndex, std::vector<int> topIndices, std::vector<int> bottomIndices);
  bool ParticlesMotherInIndices(int particleIndex, std::vector<int> indices);
  bool ParticleHasISRmotherAfterTopMother(int particleIndex);

};

struct FinalState {
  std::map<std::string, int> nObjects = {
      {"neutrinos", 0}, {"electrons", 0}, {"muons", 0}, {"taus", 0}, {"udsc_jets", 0}, {"b_jets", 0},
  };

  void print() {
    for (auto& [name, count] : nObjects) {
      if (count > 0) std::cout << count << " " << name << ", ";
    }
    std::cout << std::endl;
  }

  void AddParticle(int pid) {
    if (abs(pid) == 12 || abs(pid) == 14 || abs(pid) == 16) nObjects["neutrinos"]++;
    if (abs(pid) == 11) nObjects["electrons"]++;
    if (abs(pid) == 13) nObjects["muons"]++;
    if (abs(pid) == 15) nObjects["taus"]++;
    if (abs(pid) >= 0 && abs(pid) <= 4) nObjects["udsc_jets"]++;
    if (abs(pid) == 5) nObjects["b_jets"]++;
  }

  bool IsConsistent() {
    if (nObjects["b_jets"] != 2) return false;
    int nLeptons = nObjects["electrons"] + nObjects["muons"] + nObjects["taus"];

    if (nLeptons == 2 && nObjects["neutrinos"] == 2) return true;                                // fully leptonic
    if (nLeptons == 1 && nObjects["neutrinos"] == 1 && nObjects["udsc_jets"] == 2) return true;  // semi-leptonic
    if (nObjects["udsc_jets"] == 4) return true;                                                 // fully hadronic

    return false;
  }

  std::string GetShortName() {
    if (nObjects["udsc_jets"] == 4) return "hh";
    if (nObjects["electrons"] == 2) return "ee";
    if (nObjects["muons"] == 2) return "mumu";
    if (nObjects["taus"] == 2) return "tautau";

    std::string name = "";
    if (nObjects["udsc_jets"] == 2) name += "h";
    if (nObjects["electrons"] == 1) name += "e";
    if (nObjects["muons"] == 1) name += "mu";
    if (nObjects["taus"] == 1) name += "tau";

    return name;
  }
};

#endif /* TTAlpsEvent_hpp */
