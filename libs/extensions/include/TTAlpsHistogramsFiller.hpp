//  TTAlpsHistogramsFiller.hpp
//
//  Created by Jeremi Niedziela on 10/08/2023.

#ifndef TTAlpsHistogramsFiller_hpp
#define TTAlpsHistogramsFiller_hpp

#include "Event.hpp"
#include "Helpers.hpp"
#include "HistogramsHandler.hpp"
#include "CutFlowManager.hpp"
#include "EventProcessor.hpp"

class TTAlpsHistogramsFiller {
 public:
  TTAlpsHistogramsFiller(std::string configPath, std::shared_ptr<HistogramsHandler> histogramsHandler_);
  ~TTAlpsHistogramsFiller();

  void FillTriggerEfficiencies();
  void FillTriggerVariables(const std::shared_ptr<Event> event, std::string prefix = "", std::string suffix = "");
  void FillTriggerVariablesPerTriggerSet(const std::shared_ptr<Event> event, std::string ttbarCategory = "");

  void FillDefaultVariables(const std::shared_ptr<Event> event);
  void FillLeadingPt(const std::shared_ptr<Event> event, std::string histName, std::vector<std::string> variableLocation);
  void FillAllSubLeadingPt(const std::shared_ptr<Event> event, std::string histName, std::vector<std::string> variableLocation);

  void FillCutFlow(const std::shared_ptr<CutFlowManager> cutFlowManager);

  void FillCustomTTAlpsVariables(const std::shared_ptr<Event> event);
  

 private:
  std::shared_ptr<HistogramsHandler> histogramsHandler;
  std::unique_ptr<EventProcessor> eventProcessor;

  std::map<std::string, std::vector<std::string>> triggerSets;
  std::map<std::string, std::vector<std::string>> defaultHistVariables;
  std::map<std::string, std::vector<std::string>> ttalpsHistVariables;

  std::vector<std::string> triggerNames;
  bool EndsWithTriggerName(std::string name);
};

#endif /* TTAlpsHistogramsFiller_hpp */
