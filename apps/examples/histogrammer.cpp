#include "ConfigManager.hpp"
#include "Event.hpp"
#include "EventReader.hpp"
#include "HistogramsFiller.hpp"
#include "HistogramsHandler.hpp"
#include "CutFlowManager.hpp"

using namespace std;

int main(int argc, char **argv) {
  if (argc != 2 && argc != 4) {
    fatal() << "Usage: " << argv[0] << " config_path"<<endl;
    fatal() << "or"<<endl;
    fatal() << argv[0] << " config_path input_path output_path"<<endl;
    exit(1);
  }

  string configPath = argv[1];
  auto config = make_shared<ConfigManager>(configPath);

  if(argc == 4){
    config->SetInputPath(argv[2]);
    config->SetOutputPath(argv[3]);
  }

  auto eventReader = make_shared<EventReader>(config);
  auto histogramsHandler = make_shared<HistogramsHandler>(config);
  auto cutFlowManager = make_shared<CutFlowManager>(config, eventReader);
  auto histogramsFiller = make_unique<HistogramsFiller>(config, histogramsHandler);

  histogramsHandler->SetupHistograms();
  bool cutFlowEmpty = cutFlowManager->isEmpty();

  for (int i_event = 0; i_event < eventReader->GetNevents(); i_event++) {
    auto event = eventReader->GetEvent(i_event);

    if(cutFlowEmpty) cutFlowManager->UpdateCutFlow("initial");
    histogramsFiller->FillDefaultVariables(event);
  }
  
  cutFlowManager->Print();
  histogramsFiller->FillCutFlow(cutFlowManager);

  histogramsHandler->SaveHistograms();

  return 0;
}