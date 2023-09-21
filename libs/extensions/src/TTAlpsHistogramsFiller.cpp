//  TTAlpsHistogramsFiller.cpp
//
//  Created by Jeremi Niedziela on 10/08/2023.

#include "TTAlpsHistogramsFiller.hpp"

#include "ConfigManager.hpp"
#include "TTAlpsSelections.hpp"
#include "ExtensionsHelpers.hpp"

using namespace std;

TTAlpsHistogramsFiller::TTAlpsHistogramsFiller(string configPath, shared_ptr<HistogramsHandler> histogramsHandler_)
    : histogramsHandler(histogramsHandler_) {
  auto configManager = std::make_unique<ConfigManager>(configPath);

  eventProcessor = make_unique<EventProcessor>();

  try {
    configManager->GetMap("triggerSets", triggerSets);
    for (auto it = triggerSets.begin(); it != triggerSets.end(); ++it) triggerNames.push_back(it->first);
  }
  catch (const Exception& e){
    warn() << "Couldn't read triggerSets from config file ";
    warn() << "(which may be fine if you're not trying to apply trigger selection)\n";
  }

  try {
    configManager->GetMap("defaultHistVariables", defaultHistVariables);
  }
  catch (const Exception& e){
    warn() << "Couldn't read defaultHistVariables from config file - no default histograms will be included";
  }
  try {
    configManager->GetMap("ttalpsHistVariables", ttalpsHistVariables);
  }
  catch (const Exception& e){
    warn() << "Couldn't read ttalpsHistVariables from config file - no custom ttalps histograms will be included";
  }

}

TTAlpsHistogramsFiller::~TTAlpsHistogramsFiller() {}

bool TTAlpsHistogramsFiller::EndsWithTriggerName(string name) {
  string lastPart = name.substr(name.rfind("_") + 1);
  return find(triggerNames.begin(), triggerNames.end(), lastPart) != triggerNames.end();
}

void TTAlpsHistogramsFiller::FillTriggerEfficiencies() {
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

void TTAlpsHistogramsFiller::FillTriggerVariables(const std::shared_ptr<Event> event, std::string prefix, std::string suffix) {
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

  histogramsHandler->histograms1D[muonName]->Fill(eventProcessor->GetMaxPt(event, "Muon"));
  histogramsHandler->histograms1D[eleName]->Fill(eventProcessor->GetMaxPt(event, "Electron"));
  histogramsHandler->histograms1D[jetPtName]->Fill(eventProcessor->GetMaxPt(event, "Jet"));
  histogramsHandler->histograms1D[jetHtName]->Fill(eventProcessor->GetHt(event, "Jet"));
}

void TTAlpsHistogramsFiller::FillTriggerVariablesPerTriggerSet(const std::shared_ptr<Event> event, std::string ttbarCategory) {
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

void TTAlpsHistogramsFiller::FillDefaultVariables(const std::shared_ptr<Event> event) {
  for(auto &[histName, variableLocation] : defaultHistVariables) {
    if(variableLocation[0] == "Event") {
      // Assuming uint nObject from Event for now
      uint eventVariable = event->Get(variableLocation[1]);
      histogramsHandler->histograms1D[histName]->Fill(eventVariable);
    } else {
      auto collection = event->GetCollection(variableLocation[0]);
      for(auto object : *collection){
        histogramsHandler->histograms1D[histName]->Fill(object->Get(variableLocation[1]));
      }
    }
  }
}

void TTAlpsHistogramsFiller::FillLeadingPt(const std::shared_ptr<Event> event, std::string histName, std::vector<std::string> variableLocation) {
  histogramsHandler->histograms1D[histName]->Fill(eventProcessor->GetMaxPt(event, variableLocation[0]));
}

void TTAlpsHistogramsFiller::FillAllSubLeadingPt(const std::shared_ptr<Event> event, std::string histName, std::vector<std::string> variableLocation) {
  
  float maxPt = eventProcessor->GetMaxPt(event, variableLocation[0]);
  auto collection = event->GetCollection(variableLocation[0]);
    for(auto object : *collection){
      float pt = object->Get("pt");
      if(pt == maxPt) continue;
      histogramsHandler->histograms1D[histName]->Fill(pt);
    }
}

void TTAlpsHistogramsFiller::FillCutFlow(const std::shared_ptr<CutFlowManager> cutFlowManager) {
  int bin = 1;
  int cutFlowLength = cutFlowManager->GetCutFlow().size();
  TH1D* cutFlowHist = new TH1D("cutFlow", "cutFlow", cutFlowLength, 0, cutFlowLength+1);
  for(auto &[name, weight] : cutFlowManager->GetCutFlow()){
    cutFlowHist->SetBinContent(bin, weight);
    cutFlowHist->GetXaxis()->SetBinLabel(bin, name.c_str());
    bin++;
  }
  histogramsHandler->histograms1D["cutFlow"] = cutFlowHist;
}

void TTAlpsHistogramsFiller::FillCustomTTAlpsVariables(const std::shared_ptr<Event> event) {

  for(auto &[histName, variableLocation] : ttalpsHistVariables) {
    if(variableLocation[1] == "subleading_pt") FillAllSubLeadingPt(event, histName, variableLocation);
    else if(variableLocation[1] == "leading_pt") FillLeadingPt(event, histName, variableLocation);
  }
}
