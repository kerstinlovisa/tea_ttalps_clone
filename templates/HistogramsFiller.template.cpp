#include "TemplateName.hpp"

#include "ConfigManager.hpp"
#include "ExtensionsHelpers.hpp"

using namespace std;

TemplateName::TemplateName(shared_ptr<HistogramsHandler> histogramsHandler_)
    : histogramsHandler(histogramsHandler_) {
  // You can get some parameters from the config file if needed
  // auto &config = ConfigManager::GetInstance();
  // map<string, vector<string>> triggerSets;
  // config->GetMap("triggerSets", triggerSets);
  eventProcessor = make_unique<EventProcessor>();
}

TemplateName::~TemplateName() {}

void TemplateName::Fill(const std::shared_ptr<Event> event) {
  // Fill the histogram for given event (e.g. use EventProcessor to get some variables)
  histogramsHandler->Fill("test", eventProcessor->GetMaxPt(event, "Muon"));
}