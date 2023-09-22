#include "ConfigManager.hpp"
#include "CutFlowManager.hpp"
#include "Event.hpp"
#include "EventReader.hpp"
#include "EventWriter.hpp"
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
  auto config = make_unique<ConfigManager>(configPath);

  auto eventReader = make_shared<EventReader>(configPath);
  auto eventWriter = make_shared<EventWriter>(configPath, eventReader);
  auto cutFlowManager = make_shared<CutFlowManager>(eventReader, eventWriter);
  auto ttAlpsSelections = make_unique<TTAlpsSelections>(configPath);

  for (int iEvent = 0; iEvent < eventReader->GetNevents(); iEvent++) {
    auto event = eventReader->GetEvent(iEvent);

    if(!ttAlpsSelections->PassesTriggerSelections(event)) continue;
    if(!ttAlpsSelections->PassesSingleLeptonSelections(event, cutFlowManager)) continue;
    
    eventWriter->AddCurrentEvent("Events");
  }

  cutFlowManager->SaveCutFlow();
  eventWriter->Save();

  return 0;
}