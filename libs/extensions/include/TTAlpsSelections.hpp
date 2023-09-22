//  TTAlpsSelections.hpp
//
//  Created by Jeremi Niedziela on 16/08/2023.

#ifndef TTAlpsSelections_hpp
#define TTAlpsSelections_hpp

#include "ConfigManager.hpp"
#include "CutFlowManager.hpp"
#include "Event.hpp"
#include "EventProcessor.hpp"
#include "Helpers.hpp"
#include "PhysicsObject.hpp"

class TTAlpsSelections : public EventProcessor {
 public:
  TTAlpsSelections(std::string configPath = "") : EventProcessor(configPath) {}

  // Very inclusive semileptonic tt selections. Requires:
  // - at least one good lepton (allows for additional leptons)
  // - at least 4 good jets
  // - at least 1 good b-tagged jet
  // - some amount of MET
  bool PassesLooseSemileptonicSelections(const std::shared_ptr<Event> event, std::shared_ptr<CutFlowManager> cutFlowManager);

  // Selections targetting semi-leptonic ttbar + two muons. Requires:
  // - 1 good e/μ (the top-lepton)
  // - at least 2 additional good muons (different than the top-lepton)
  // - at least 4 good jets
  // - at least 1 good b-tagged jet
  // - some amount of MET
  bool PassesSignalLikeSelections(const std::shared_ptr<Event> event, std::shared_ptr<CutFlowManager> cutFlowManager);

  // Selections targetting semi-leptonic ttbar, and additional leptons. Requires:
  // - 1 good e/μ (the top-lepton)
  // - 0 other quasi-good leptons
  // - at least 4 good jets
  // - at least 1 good b-tagged jet
  // - some amount of MET
  bool PassesSingleLeptonSelections(const std::shared_ptr<Event> event, std::shared_ptr<CutFlowManager> cutFlowManager=nullptr);

  bool PassesDileptonSelections(const std::shared_ptr<Event> event);
  bool PassesHadronSelections(const std::shared_ptr<Event> event);
  bool PassesTriggerSelections(const std::shared_ptr<Event> event);

 private:
  std::vector<std::string> triggerWarningsPrinted;
};

#endif /* TTAlpsSelections_hpp */
