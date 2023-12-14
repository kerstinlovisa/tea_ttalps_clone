#ifndef NanoEvent_hpp
#define NanoEvent_hpp

#include "Event.hpp"
#include "Helpers.hpp"

class NanoEvent {
 public:
  NanoEvent(std::shared_ptr<Event> event_) : event(event_) {}

  auto Get(std::string branchName) { return event->Get(branchName); }
  float GetAsFloat(std::string branchName) { return event->GetAsFloat(branchName); }
  std::shared_ptr<PhysicsObjects> GetCollection(std::string name) const { return event->GetCollection(name); }
  int GetCollectionSize(std::string name) { return event->GetCollectionSize(name); }
  void AddExtraCollections() { event->AddExtraCollections(); }

  TLorentzVector GetMetFourVector();
  float GetMetPt();

  std::shared_ptr<PhysicsObjects> GetAllMuons(float matchingDeltaR = 0.1);

 private:
  std::shared_ptr<Event> event;
};

#endif /* NanoEvent_hpp */
