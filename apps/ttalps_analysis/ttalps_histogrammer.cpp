#include "ConfigManager.hpp"
#include "CutFlowManager.hpp"
#include "Event.hpp"
#include "EventReader.hpp"
#include "HistogramsHandler.hpp"
#include "TTAlpsHistogramFiller.hpp"

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

  for (int iEvent = 0; iEvent < eventReader->GetNevents(); iEvent++) {
    auto event = eventReader->GetEvent(iEvent);

    histogramsFiller->FillDefaultVariables(event);
    histogramsFiller->FillCustomTTAlpsVariables(event);
  }

  histogramsFiller->FillCutFlow(cutFlowManager);
  histogramsHandler->SaveHistograms();

  return 0;
}