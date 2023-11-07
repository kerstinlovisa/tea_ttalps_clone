#include "ConfigManager.hpp"
#include "CutFlowManager.hpp"
#include "Event.hpp"
#include "EventReader.hpp"
#include "EventWriter.hpp"
#include "HistogramsHandler.hpp"
#include "Profiler.hpp"
#include "TTAlpsSelections.hpp"
#include "UserExtensionsHelpers.hpp"

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
  auto &config = ConfigManager::GetInstance();
  
  if(argc == 4){
    config.SetInputPath(argv[2]);
    config.SetOutputPath(argv[3]);
  }

  auto eventReader = make_shared<EventReader>();
  auto eventWriter = make_shared<EventWriter>(eventReader);
  auto cutFlowManager = make_shared<CutFlowManager>(eventReader, eventWriter);
  auto eventProcessor = make_unique<EventProcessor>();
  auto ttAlpsSelections = make_unique<TTAlpsSelections>();

  bool applyLooseSkimming, applyTTbarLikeSkimming, applySignalLikeSkimming, applyTTZLikeSkimming, applyDSAMuonSkimming;
  config.GetValue("applyLooseSkimming", applyLooseSkimming);
  config.GetValue("applyTTbarLikeSkimming", applyTTbarLikeSkimming);
  config.GetValue("applySignalLikeSkimming", applySignalLikeSkimming);
  config.GetValue("applyTTZLikeSkimming", applyTTZLikeSkimming);

  for (int iEvent = 0; iEvent < eventReader->GetNevents(); iEvent++) {
    auto event = eventReader->GetEvent(iEvent);

    cutFlowManager->UpdateCutFlow("initial");

    if (!eventProcessor->PassesTriggerSelections(event)) continue;
    cutFlowManager->UpdateCutFlow("trigger");

    if (applyLooseSkimming) {
      if (!ttAlpsSelections->PassesLooseSemileptonicSelections(event, cutFlowManager)) continue;
    }

    if(applyTTbarLikeSkimming){
      if(!ttAlpsSelections->PassesSingleLeptonSelections(event, cutFlowManager)) continue;
    }

    if(applySignalLikeSkimming){
      if(!ttAlpsSelections->PassesSignalLikeSelections(event, cutFlowManager)) continue;
    }

    if(applyTTZLikeSkimming){
      if(!ttAlpsSelections->PassesTTZLikeSelections(event, cutFlowManager)) continue;
    }

    eventWriter->AddCurrentEvent("Events");
  }
  cutFlowManager->Print();
  cutFlowManager->SaveCutFlow();
  eventWriter->Save();

  return 0;
}