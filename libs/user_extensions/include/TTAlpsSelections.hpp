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

class TTAlpsSelections {
 public:
  TTAlpsSelections();
  
  // Selections targetting semi-leptonic ttbar + two muons. Requires:
  // - 1 good e/μ (the top-lepton)
  // - at least 2 additional good muons (different than the top-lepton)
  // - at least 4 good jets
  // - at least 1 good b-tagged jet
  // - some amount of MET
  bool PassesSignalLikeSelections(const std::shared_ptr<Event> event, std::shared_ptr<CutFlowManager> cutFlowManager);
  void RegisterSignalLikeSelections(std::shared_ptr<CutFlowManager> cutFlowManager);

  // Selections targetting semi-leptonic ttbar, and additional leptons. Requires:
  // - 1 good e/μ (the top-lepton)
  // - 0 other quasi-good leptons
  // - at least 4 good jets
  // - at least 1 good b-tagged jet
  // - some amount of MET
  bool PassesSingleLeptonSelections(const std::shared_ptr<Event> event, std::shared_ptr<CutFlowManager> cutFlowManager = nullptr);
  void RegisterSingleLeptonSelections(std::shared_ptr<CutFlowManager> cutFlowManager);

  // Selections targetting ttZ, Z->μμ process. Requires:
  // - 1 good e/μ (the top-lepton)
  // - 2 additional quasi-good muons
  // - at least 4 good jets
  // - at least 1 good b-tagged jet
  // - some amount of MET
  bool PassesTTZLikeSelections(const std::shared_ptr<Event> event, std::shared_ptr<CutFlowManager> cutFlowManager = nullptr);
  void RegisterTTZLikeSelections(std::shared_ptr<CutFlowManager> cutFlowManager);

  bool PassesDileptonSelections(const std::shared_ptr<Event> event);
  bool PassesHadronSelections(const std::shared_ptr<Event> event);

 private:
  std::unique_ptr<EventProcessor> eventProcessor;

};

#endif /* TTAlpsSelections_hpp */
