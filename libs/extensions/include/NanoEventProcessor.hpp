//  NanoEventProcessor.hpp
//
//  Created by Jeremi Niedziela on 24/11/2023.

#ifndef NanoEventProcessor_hpp
#define NanoEventProcessor_hpp

#include "Event.hpp"
#include "ExtensionsHelpers.hpp"
#include "EventProcessor.hpp"
#include "Muon.hpp"

class NanoEventProcessor {
 public:
  NanoEventProcessor();

  float GetGenWeight(const std::shared_ptr<Event> event);
  float GetPileupScaleFactor(const std::shared_ptr<Event> event);
  float GetMuonTriggerScaleFactor(const std::shared_ptr<Event> event);

  std::pair<std::shared_ptr<Muon>, std::shared_ptr<Muon>> GetMuonPairClosestToZ(const std::shared_ptr<Event> event, std::string collection);

 private:
 std::unique_ptr<EventProcessor> eventProcessor;
 
 std::string weightsBranchName;
};

#endif /* NanoEventProcessor_hpp */
