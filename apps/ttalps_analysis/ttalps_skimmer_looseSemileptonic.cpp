#include "ConfigManager.hpp"
#include "CutFlowManager.hpp"
#include "Event.hpp"
#include "EventReader.hpp"
#include "EventWriter.hpp"
#include "UserExtensionsHelpers.hpp"
#include "HistogramsHandler.hpp"
#include "Profiler.hpp"
#include "TTAlpsSelections.hpp"

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
  auto eventWriter = make_shared<EventWriter>(config, eventReader);
  auto cutFlowManager = make_shared<CutFlowManager>(eventReader, eventWriter);
  
  auto eventProcessor = make_unique<EventProcessor>(config);
  auto ttAlpsSelections = make_unique<TTAlpsSelections>(config);
  
  for (int iEvent = 0; iEvent < eventReader->GetNevents(); iEvent++) {
    auto event = eventReader->GetEvent(iEvent);

    cutFlowManager->UpdateCutFlow("initial");

    if(!eventProcessor->PassesTriggerSelections(event)) continue;
    cutFlowManager->UpdateCutFlow("trigger");

    if(!ttAlpsSelections->PassesLooseSemileptonicSelections(event, cutFlowManager)) continue;
    
    eventWriter->AddCurrentEvent("Events");
  }

  cutFlowManager->SaveCutFlow();
  eventWriter->Save();

  return 0;
}