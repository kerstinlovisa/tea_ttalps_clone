#include "ConfigManager.hpp"
#include "CutFlowManager.hpp"
#include "EventReader.hpp"
#include "ExtensionsHelpers.hpp"
#include "HistogramsFiller.hpp"
#include "HistogramsHandler.hpp"

using namespace std;

void CheckArgs(int argc, char **argv) {
  if (argc != 2 && argc != 4 && argc != 6) {
    fatal() << "Usage: " << argv[0] << " config_path"<<endl;
    fatal() << "or"<<endl;
    fatal() << argv[0] << " config_path input_path output_path"<<endl;
    fatal() << "or"<<endl;
    fatal() << argv[0] << " config_path input_path output_path apply_muon_scale_factors apply_muon_trigger_scale_factors"<<endl;
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
  if(argc == 6){
    bool applyMounScaleFactors = atoi(argv[4]);
    if (applyMounScaleFactors) info() << "Muon Scale Factors will be applied" << endl;
    else info() << "Muon Scale Factors were explicitely turned off" << endl;

    if (applyMounTriggerScaleFactors) info() << "Muon Trigger Scale Factors will be applied" << endl;
    else info() << "Muon Trigger Scale Factors were explicitely turned off" << endl;
    config.SetApplyMuonScaleFactors(applyMounScaleFactors);
    config.SetApplyMuonTriggerScaleFactors(applyMounTriggerScaleFactors);
  }

  auto eventReader = make_shared<EventReader>();
  auto histogramsHandler = make_shared<HistogramsHandler>();
  auto cutFlowManager = make_shared<CutFlowManager>(eventReader);
  auto histogramsFiller = make_unique<HistogramsFiller>(histogramsHandler);

  cutFlowManager->RegisterCut("initial");

  for (int iEvent = 0; iEvent < eventReader->GetNevents(); iEvent++) {
    auto event = eventReader->GetEvent(iEvent);

    cutFlowManager->UpdateCutFlow("initial");
    histogramsFiller->FillDefaultVariables(event);
  }

  cutFlowManager->Print();
  histogramsFiller->FillCutFlow(cutFlowManager);
  histogramsHandler->SaveHistograms();

  auto &logger = Logger::GetInstance();
  logger.Print();
  return 0;
}