//  skimmer.cpp
//
//  Created by Jeremi Niedziela on 10/08/2023.

#include "ConfigManager.hpp"
#include "Event.hpp"
#include "EventReader.hpp"
#include "ExtensionsHelpers.hpp"
#include "EventWriter.hpp"
#include "CutFlowManager.hpp"
#include "EventProcessor.hpp"

using namespace std;

int main(int argc, char **argv) {
  if (argc != 2) {
    fatal() << "Usage: " << argv[0] << " config_path\n";
    exit(1);
  }

  string configPath = argv[1];
  
  auto eventReader = make_shared<EventReader>(configPath);
  auto eventWriter = make_shared<EventWriter>(configPath, eventReader);
  auto cutFlowManager = make_shared<CutFlowManager>(eventReader, eventWriter);
  auto eventProcessor = make_unique<EventProcessor>(configPath);
  
  for (int i_event = 0; i_event < eventReader->GetNevents(); i_event++) {    
    auto event = eventReader->GetEvent(i_event);

    cutFlowManager->UpdateCutFlow("initial");
    if(!eventProcessor->PassesTriggerSelections(event)) continue;
    cutFlowManager->UpdateCutFlow("trigger");

    if(!eventProcessor->PassesEventSelections(event, cutFlowManager)) continue;

    eventWriter->AddCurrentEvent("Events");
  }
  cutFlowManager->SaveCutFlow();

  eventWriter->Save();

  return 0;
}
