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
  if (argc != 2 && argc != 4 && argc != 6) {
    fatal() << "Usage: " << argv[0] << " config_path"<<endl;
    fatal() << "or"<<endl;
    fatal() << argv[0] << " config_path input_path output_path"<<endl;
    exit(1);
  }
}

int main(int argc, char **argv) {
  CheckArgs(argc, argv);
  ConfigManager::Initialize(argv[1]);
  auto &config = ConfigManager::GetInstance();

  if(argc == 4 || argc == 6){
    config.SetInputPath(argv[2]);
    config.SetOutputPath(argv[3]);
  }

  info() << "Creating objects..." << endl;
  auto eventReader = make_shared<EventReader>();
  auto cutFlowManager = make_shared<CutFlowManager>(eventReader);
  auto histogramsHandler = make_shared<HistogramsHandler>();
  auto histogramFiller = make_unique<HistogramsFiller>(histogramsHandler);
  auto ttalpsHistogramsFiller = make_unique<TTAlpsHistogramFiller>(histogramsHandler);

  bool runDefaultHistograms, runTriggerHistograms, runPileupHistograms;
  config.GetValue("runDefaultHistograms", runDefaultHistograms);
  config.GetValue("runTriggerHistograms", runTriggerHistograms);
  config.GetValue("runPileupHistograms", runPileupHistograms);

  if (runPileupHistograms) cutFlowManager->RegisterCut("initial");
  
  info() << "Starting event loop..." << endl;
  for (int iEvent = 0; iEvent < eventReader->GetNevents(); iEvent++) {
    auto event = eventReader->GetEvent(iEvent);

    if (runDefaultHistograms) {
      cutFlowManager->UpdateCutFlow("initial");
      ttalpsHistogramsFiller->FillNormCheck(event);
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

    if (runPileupHistograms) {
      cutFlowManager->UpdateCutFlow("initial");
      histogramFiller->FillDefaultVariables(event);
    }
  }

  if(runTriggerHistograms) ttalpsHistogramsFiller->FillTriggerEfficiencies();
  if(runDefaultHistograms || runPileupHistograms) histogramFiller->FillCutFlow(cutFlowManager);
  
  cutFlowManager->Print();
  histogramsHandler->SaveHistograms();

  auto &logger = Logger::GetInstance();
  logger.Print();

  return 0;
}