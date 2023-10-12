#include "TemplateName.hpp"

#include "ConfigManager.hpp"
#include "ExtensionsHelpers.hpp"

using namespace std;

TemplateName::TemplateName(std::shared_ptr<ConfigManager> _config, shared_ptr<HistogramsHandler> histogramsHandler_)
    : histogramsHandler(histogramsHandler_) {
  
  // Here you can get some parameters from the config file
  // map<string, vector<string>> triggerSets;
  // _config->GetMap("triggerSets", triggerSets);

  eventProcessor = make_unique<EventProcessor>();
}

TemplateName::~TemplateName() {}


void TemplateName::Fill(const std::shared_ptr<Event> event) {
  // Fill the histogram for given event (e.g. use EventProcessor to get some variables)
  histogramsHandler->Fill("test", eventProcessor->GetMaxPt(event, "Muon"));
}