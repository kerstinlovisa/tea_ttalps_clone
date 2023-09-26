#include "ConfigManager.hpp"
#include "CutFlowManager.hpp"
#include "Event.hpp"
#include "EventReader.hpp"
#include "HistogramsHandler.hpp"
#include "TTAlpsHistogramFiller.hpp"
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
  auto config = make_unique<ConfigManager>(configPath);

  auto eventReader = make_shared<EventReader>(configPath);
  auto cutFlowManager = make_shared<CutFlowManager>(eventReader);
  auto histogramsHandler = make_shared<HistogramsHandler>(configPath);
  histogramsHandler->SetupHistograms();

  auto histogramsFiller = make_unique<TTAlpsHistogramFiller>(configPath, histogramsHandler);

  bool runDefaultHistograms, runTriggerHistograms;
  config->GetValue("runDefaultHistograms", runDefaultHistograms);
  config->GetValue("runTriggerHistograms", runTriggerHistograms);

  for (int iEvent = 0; iEvent < eventReader->GetNevents(); iEvent++) {
    auto event = eventReader->GetEvent(iEvent);

    if (runDefaultHistograms) {
      histogramsFiller->FillDefaultVariables(event);
      histogramsFiller->FillCustomTTAlpsVariables(event);
    }

    if (runTriggerHistograms) {
      auto ttAlpsEvent = asTTAlpsEvent(event);
      string ttbarCategory = ttAlpsEvent->GetTTbarEventCategory();
      histogramsFiller->FillTriggerVariables(event, "inclusive");
      histogramsFiller->FillTriggerVariables(event, ttbarCategory);
      histogramsFiller->FillTriggerVariablesPerTriggerSet(event, "inclusive");
      histogramsFiller->FillTriggerVariablesPerTriggerSet(event, ttbarCategory);
    }
  }


  if(runTriggerHistograms) histogramsFiller->FillTriggerEfficiencies();
  if(runDefaultHistograms) histogramsFiller->FillCutFlow(cutFlowManager);
  
  histogramsHandler->SaveHistograms();

  return 0;
}