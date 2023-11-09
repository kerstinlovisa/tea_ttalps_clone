#ifndef TTAlpsHistogramFiller_hpp
#define TTAlpsHistogramFiller_hpp

#include "Event.hpp"
#include "EventProcessor.hpp"
#include "Helpers.hpp"
#include "HistogramsHandler.hpp"
#include "CutFlowManager.hpp"

class TTAlpsHistogramFiller {
 public:
  TTAlpsHistogramFiller(std::shared_ptr<HistogramsHandler> histogramsHandler_);
  ~TTAlpsHistogramFiller();

  void FillTriggerEfficiencies();
  void FillTriggerVariables(const std::shared_ptr<Event> event, std::string prefix = "", std::string suffix = "");
  void FillTriggerVariablesPerTriggerSet(const std::shared_ptr<Event> event, std::string ttbarCategory = "");

  void FillLeadingPt(const std::shared_ptr<Event> event, std::string histName, const HistogramParams &params);
  void FillAllSubLeadingPt(const std::shared_ptr<Event> event, std::string histName, const HistogramParams &params);

  void FillCustomTTAlpsVariables(const std::shared_ptr<Event> event);

  void FillGenParticleVariables(const std::shared_ptr<Event> event, std::string histName, std::string variable, int pdgid_);
  void FillGenParticleBoost(const std::shared_ptr<Event> event, std::string histName, int pdgid_);
  void FillGenParticleVxyz(const std::shared_ptr<Event> event, std::string histName, int pdgid_);
  void FillGenParticleProperVxyz(const std::shared_ptr<Event> event, std::string histName, int pdgid_);
  void FillGenMuonsFromALPs(const std::shared_ptr<Event> event, std::string histName, std::string variable);
  void FillMuonVariables(const std::shared_ptr<Event> event, std::string histName, std::string collection, std::string variable);
  void FillCustomLLPNanoAODVariables(const std::shared_ptr<Event> event);

  void FillNormCheck(const std::shared_ptr<Event> event);

 private:
  std::shared_ptr<HistogramsHandler> histogramsHandler;
  std::unique_ptr<EventProcessor> eventProcessor;

  std::map<std::string, std::vector<std::string>> triggerSets;
  std::map<std::string, HistogramParams> defaultHistVariables;
  std::map<std::string, HistogramParams> ttalpsHistVariables;

  std::string weightsBranchName;

  std::vector<std::string> triggerNames;
  bool EndsWithTriggerName(std::string name);
};

#endif /* TTAlpsHistogramFiller_hpp */
