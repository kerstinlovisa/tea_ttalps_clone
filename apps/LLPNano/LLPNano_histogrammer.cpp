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
  auto cutFlowManager = make_shared<CutFlowManager>(eventReader);
  auto histogramsHandler = make_shared<HistogramsHandler>();
  auto histogramFiller = make_unique<HistogramsFiller>(histogramsHandler);
  auto ttalpsHistogramsFiller = make_unique<TTAlpsHistogramFiller>(histogramsHandler);

  bool runDefaultHistograms, runLLPNanoHistograms;
  config.GetValue("runDefaultHistograms", runDefaultHistograms);
  config.GetValue("runLLPNanoHistograms", runLLPNanoHistograms);

  for (int iEvent = 0; iEvent < eventReader->GetNevents(); iEvent++) {
    auto event = eventReader->GetEvent(iEvent);

    cutFlowManager->UpdateCutFlow("initial");
    // ttalpsHistogramsFiller->FillNormCheck(event);

    if (runDefaultHistograms) {
      histogramFiller->FillDefaultVariables(event);
    }

    // if (runLLPNanoHistograms) {
    //   ttalpsHistogramsFiller->FillCustomLLPVariables(event);
    // }
  }

  if(runDefaultHistograms) histogramFiller->FillCutFlow(cutFlowManager);
  
  cutFlowManager->Print();
  histogramsHandler->SaveHistograms();

  return 0;
}