//  EventProcessor.hpp
//
//  Created by Jeremi Niedziela on 08/08/2023.

#ifndef EventProcessor_hpp
#define EventProcessor_hpp

#include "ConfigManager.hpp"
#include "Event.hpp"
#include "Helpers.hpp"
#include "PhysicsObject.hpp"
#include "CutFlowManager.hpp"

class EventProcessor {
 public:
  EventProcessor();
  
  float GetMaxPt(std::shared_ptr<Event> event, std::string collectionName);
  std::shared_ptr<PhysicsObject> GetMaxPtObject(std::shared_ptr<Event> event, std::string collectionName);

  float GetHt(std::shared_ptr<Event> event, std::string collectionName);

  void RegisterCuts(std::shared_ptr<CutFlowManager> cutFlowManager);

  bool PassesTriggerSelections(const std::shared_ptr<Event> event);
  bool PassesEventSelections(const std::shared_ptr<Event> event, std::shared_ptr<CutFlowManager> cutFlowManager);

 private:
  std::vector<std::string> triggerNames;
  std::unordered_map<std::string, std::pair<float, float>> eventSelections;
  std::vector<std::string> triggerWarningsPrinted;
};

#endif /* EventProcessor_hpp */
