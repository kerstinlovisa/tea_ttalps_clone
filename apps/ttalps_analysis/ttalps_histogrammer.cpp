#include "ConfigManager.hpp"
#include "CutFlowManager.hpp"
#include "Event.hpp"
#include "EventReader.hpp"
#include "HistogramsHandler.hpp"
#include "TTAlpsHistogramFiller.hpp"
#include "HistogramsFiller.hpp"
#include "UserExtensionsHelpers.hpp"

using namespace std;

void CheckArgs(int argc, char **argv) {
  if (argc != 2) {
    fatal() << "Usage: " << argv[0] << " config_path\n";
    exit(1);
  }
}

int main(int argc, char **argv) {
  CheckArgs(argc, argv);

  string configPath = argv[1];
  auto config = make_shared<ConfigManager>(configPath);

  auto eventReader = make_shared<EventReader>(config);
  auto cutFlowManager = make_shared<CutFlowManager>(eventReader);
  auto histogramsHandler = make_shared<HistogramsHandler>(config);
  histogramsHandler->SetupHistograms();

  auto histogramFiller = make_unique<HistogramsFiller>(config, histogramsHandler);
  auto ttalpsHistogramsFiller = make_unique<TTAlpsHistogramFiller>(config, histogramsHandler);

  bool runDefaultHistograms, runTriggerHistograms;
  config->GetValue("runDefaultHistograms", runDefaultHistograms);
  config->GetValue("runTriggerHistograms", runTriggerHistograms);

  for (int iEvent = 0; iEvent < eventReader->GetNevents(); iEvent++) {
    auto event = eventReader->GetEvent(iEvent);

    if (runDefaultHistograms) {
      histogramFiller->FillDefaultVariables(event);
      ttalpsHistogramsFiller->FillCustomTTAlpsVariables(event);
    }

    if (runTriggerHistograms) {
      auto ttAlpsEvent = asTTAlpsEvent(event);
      string ttbarCategory = ttAlpsEvent->GetTTbarEventCategory();
      ttalpsHistogramsFiller->FillTriggerVariables(event, "inclusive");
      ttalpsHistogramsFiller->FillTriggerVariables(event, ttbarCategory);
      ttalpsHistogramsFiller->FillTriggerVariablesPerTriggerSet(event, "inclusive");
      ttalpsHistogramsFiller->FillTriggerVariablesPerTriggerSet(event, ttbarCategory);
    }
  }

  if(runTriggerHistograms) ttalpsHistogramsFiller->FillTriggerEfficiencies();
  if(runDefaultHistograms) histogramFiller->FillCutFlow(cutFlowManager);
  
  histogramsHandler->SaveHistograms();

  return 0;
}