#include "TTAlpsHistogramFiller.hpp"

#include "ConfigManager.hpp"
#include "TTAlpsSelections.hpp"
#include "ExtensionsHelpers.hpp"

using namespace std;

TTAlpsHistogramFiller::TTAlpsHistogramFiller(shared_ptr<ConfigManager> _config, shared_ptr<HistogramsHandler> histogramsHandler_)
    : histogramsHandler(histogramsHandler_) {
  eventProcessor = make_unique<EventProcessor>();

  try {
    _config->GetMap("triggerSets", triggerSets);
    for (auto it = triggerSets.begin(); it != triggerSets.end(); ++it) triggerNames.push_back(it->first);
  }
  catch (const Exception& e){
    warn() << "Couldn't read triggerSets from config file ";
    warn() << "(which may be fine if you're not trying to apply trigger selection)" << endl;
  }

  try {
    _config->GetMap("defaultHistVariables", defaultHistVariables);
  }
  catch (const Exception& e){
    warn() << "Couldn't read defaultHistVariables from config file - no default histograms will be included" << endl;
  }
  try {
    _config->GetMap("ttalpsHistVariables", ttalpsHistVariables);
  }
  catch (const Exception& e){
    warn() << "Couldn't read ttalpsHistVariables from config file - no custom ttalps histograms will be included" << endl;
  }

  try {
    _config->GetValue("weightsBranchName", weightsBranchName);
  } catch (const Exception& e) {
    info() << "Weights branch not specified -- will assume weight is 1 for all events" << endl;
  }
}

TTAlpsHistogramFiller::~TTAlpsHistogramFiller() {}

bool TTAlpsHistogramFiller::EndsWithTriggerName(string name) {
  string lastPart = name.substr(name.rfind("_") + 1);
  return find(triggerNames.begin(), triggerNames.end(), lastPart) != triggerNames.end();
}

void TTAlpsHistogramFiller::FillTriggerEfficiencies() {
  TH1D *hist_tmp;

  for (auto &[name, hist] : histogramsHandler->histograms1D) {
    if (!EndsWithTriggerName(name)) continue;
    string nameWithoutTrigger = name.substr(0, name.rfind("_"));
    string newName = name + "_eff";
    hist_tmp = (TH1D *)histogramsHandler->histograms1D[name]->Clone(newName.c_str());
    hist_tmp->Divide(hist_tmp, histogramsHandler->histograms1D[nameWithoutTrigger], 1, 1, "B");
    histogramsHandler->histograms1D[newName] = hist_tmp;
  }
}

void TTAlpsHistogramFiller::FillTriggerVariables(const std::shared_ptr<Event> event, std::string prefix, std::string suffix) {
  if (prefix != "") prefix = prefix + "_";
  if (suffix != "") suffix = "_" + suffix;

  string muonName = prefix + "muonMaxPt" + suffix;
  string eleName = prefix + "eleMaxPt" + suffix;
  string jetPtName = prefix + "jetMaxPt" + suffix;
  string jetHtName = prefix + "jetHt" + suffix;

  if (!histogramsHandler->histograms1D.count(muonName)) error() << "Couldn't find key: " << muonName << " in histograms map\n";
  if (!histogramsHandler->histograms1D.count(eleName)) error() << "Couldn't find key: " << eleName << " in histograms map\n";
  if (!histogramsHandler->histograms1D.count(jetPtName)) error() << "Couldn't find key: " << jetPtName << " in histograms map\n";
  if (!histogramsHandler->histograms1D.count(jetHtName)) error() << "Couldn't find key: " << jetHtName << " in histograms map\n";

  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  histogramsHandler->histograms1D[muonName]->Fill(eventProcessor->GetMaxPt(event, "Muon"), weight);
  histogramsHandler->histograms1D[eleName]->Fill(eventProcessor->GetMaxPt(event, "Electron"), weight);
  histogramsHandler->histograms1D[jetPtName]->Fill(eventProcessor->GetMaxPt(event, "Jet"), weight);
  histogramsHandler->histograms1D[jetHtName]->Fill(eventProcessor->GetHt(event, "Jet"), weight);
}

void TTAlpsHistogramFiller::FillTriggerVariablesPerTriggerSet(const std::shared_ptr<Event> event, std::string ttbarCategory) {
  auto ttAlpsSelections = make_unique<TTAlpsSelections>();

  bool passesSingleLepton = ttAlpsSelections->PassesSingleLeptonSelections(event);
  bool passesDilepton = ttAlpsSelections->PassesDileptonSelections(event);
  bool passesHadron = ttAlpsSelections->PassesHadronSelections(event);

  for (auto &[triggerSetName, triggerSet] : triggerSets) {
    bool passesTrigger = false;

    for (auto &triggerName : triggerSet) {
      passesTrigger = event->Get(triggerName);
      if (passesTrigger) break;
    }
    if (!passesTrigger) continue;

    FillTriggerVariables(event, ttbarCategory, triggerSetName);
    if (passesSingleLepton) FillTriggerVariables(event, ttbarCategory, triggerSetName + "_singleLepton");
    if (passesDilepton) FillTriggerVariables(event, ttbarCategory, triggerSetName + "_dilepton");
    if (passesHadron) FillTriggerVariables(event, ttbarCategory, triggerSetName + "_hadron");
  }
}

void TTAlpsHistogramFiller::FillLeadingPt(const std::shared_ptr<Event> event, std::string histName, std::vector<std::string> variableLocation) {
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }
  histogramsHandler->histograms1D[histName]->Fill(eventProcessor->GetMaxPt(event, variableLocation[0]), weight);
}

void TTAlpsHistogramFiller::FillAllSubLeadingPt(const std::shared_ptr<Event> event, std::string histName, std::vector<std::string> variableLocation) {
  
  float maxPt = eventProcessor->GetMaxPt(event, variableLocation[0]);
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  auto collection = event->GetCollection(variableLocation[0]);
    for(auto object : *collection){
      float pt = object->Get("pt");
      if(pt == maxPt) continue;
      histogramsHandler->histograms1D[histName]->Fill(pt, weight);
    }
}

void TTAlpsHistogramFiller::FillCustomTTAlpsVariables(const std::shared_ptr<Event> event) {

  for(auto &[histName, variableLocation] : ttalpsHistVariables) {
    if(variableLocation[1] == "subleading_pt") FillAllSubLeadingPt(event, histName, variableLocation);
    else if(variableLocation[1] == "leading_pt") FillLeadingPt(event, histName, variableLocation);
  }
}
