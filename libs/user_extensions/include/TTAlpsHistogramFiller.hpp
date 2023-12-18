#ifndef TTAlpsHistogramFiller_hpp
#define TTAlpsHistogramFiller_hpp

#include "Event.hpp"
#include "EventProcessor.hpp"
#include "Helpers.hpp"
#include "HistogramsHandler.hpp"
#include "CutFlowManager.hpp"
#include "NanoEventProcessor.hpp"

class TTAlpsHistogramFiller {
 public:
  TTAlpsHistogramFiller(std::shared_ptr<HistogramsHandler> histogramsHandler_);
  ~TTAlpsHistogramFiller();

  void FillTriggerEfficiencies();
  void FillTriggerVariables(const std::shared_ptr<Event> event, std::string prefix = "", std::string suffix = "");
  void FillTriggerVariablesPerTriggerSet(const std::shared_ptr<Event> event, std::string ttbarCategory = "");

  void FillLeadingPt(const std::shared_ptr<Event> event, std::string histName, const HistogramParams &params);
  void FillAllSubLeadingPt(const std::shared_ptr<Event> event, std::string histName, const HistogramParams &params);

  void FillDefaultVariables(const std::shared_ptr<Event> event);
  void FillCustomTTAlpsVariables(const std::shared_ptr<Event> event);
  void FillCustomTTAlpsVariablesFromLLPNanoAOD(const std::shared_ptr<Event> event);

  void FillGenMuonsFromALPs(const std::shared_ptr<Event> event);

  void FillNormCheck(const std::shared_ptr<Event> event);

 private:
  std::shared_ptr<HistogramsHandler> histogramsHandler;
  std::unique_ptr<EventProcessor> eventProcessor;
  std::unique_ptr<NanoEventProcessor> nanoEventProcessor;

  std::map<std::string, std::vector<std::string>> triggerSets;
  std::map<std::string, HistogramParams> defaultHistVariables;
  std::map<std::string, HistogramParams> ttalpsHistVariables;

  std::vector<std::string> triggerNames;
  bool EndsWithTriggerName(std::string name);

  float GetEventWeight(const std::shared_ptr<Event> event);

  void FillDimuonHistograms(const std::shared_ptr<Event> event);
  void FillDiumonClosestToZhistgrams(const std::shared_ptr<Event> event);
  void FillMuonMetHistograms(const std::shared_ptr<Event> event);
  void FillJetHistograms(const std::shared_ptr<Event> event);
  void FillLooseDSAMuonsHistograms(const std::shared_ptr<Event> event);
  void FillAllLooseMuonsHistograms(const std::shared_ptr<Event> event);
};

#endif /* TTAlpsHistogramFiller_hpp */
