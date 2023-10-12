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

void CheckArgs(int argc, char **argv) {
  if (argc != 2 && argc != 4) {
    fatal() << "Usage: " << argv[0] << " config_path"<<endl;
    fatal() << "or"<<endl;
    fatal() << argv[0] << " config_path input_path output_path"<<endl;
    exit(1);
  }
}

int main(int argc, char **argv) {
  CheckArgs(argc, argv);
  ConfigManager::Initialize(argv[1]);
  
  if(argc == 4){
    auto &config = ConfigManager::GetInstance();
    config.SetInputPath(argv[2]);
    config.SetOutputPath(argv[3]);
  }

  auto eventReader = make_shared<EventReader>();
  auto eventWriter = make_shared<EventWriter>(eventReader);
  auto cutFlowManager = make_shared<CutFlowManager>(eventReader, eventWriter);
  auto eventProcessor = make_unique<EventProcessor>();
  
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
