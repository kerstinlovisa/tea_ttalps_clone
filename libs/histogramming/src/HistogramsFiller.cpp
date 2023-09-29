//  HistogramsFiller.cpp
//
//  Created by Jeremi Niedziela on 10/08/2023.

#include "HistogramsFiller.hpp"

#include "ConfigManager.hpp"
#include "ExtensionsHelpers.hpp"

using namespace std;

HistogramsFiller::HistogramsFiller(shared_ptr<ConfigManager> _config, shared_ptr<HistogramsHandler> histogramsHandler_)
    : histogramsHandler(histogramsHandler_) {
  eventProcessor = make_unique<EventProcessor>();

  try {
    _config->GetMap("defaultHistVariables", defaultHistVariables);
  } catch (const Exception& e) {
    warn() << "Couldn't read defaultHistVariables from config file - no default histograms will be included" << endl;
  }

  try {
    _config->GetValue("weightsBranchName", weightsBranchName);
  } catch (const Exception& e) {
    info() << "Weights branch not specified -- will assume weight is 1 for all events" << endl;
  }
}

HistogramsFiller::~HistogramsFiller() {}

void HistogramsFiller::FillDefaultVariables(const std::shared_ptr<Event> event) {
  
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }
  
  for (auto& [histName, variableLocation] : defaultHistVariables) {
    string collectionName = variableLocation[0];
    string branchName = variableLocation[1];
    
    if (collectionName == "Event") {
      
      uint eventVariable;
      if(branchName[0] == 'n'){
        eventVariable = event->GetCollectionSize(branchName.substr(1));
      }
      else{
        eventVariable = event->Get(branchName);
      }
      histogramsHandler->histograms1D[histName]->Fill(eventVariable, weight);
    } else {
      auto collection = event->GetCollection(collectionName);
      for (auto object : *collection) {
        histogramsHandler->histograms1D[histName]->Fill(object->Get(branchName), weight);
      }
    }
  }
}

void HistogramsFiller::FillCutFlow(const std::shared_ptr<CutFlowManager> cutFlowManager) {
  int bin = 1;
  int cutFlowLength = cutFlowManager->GetCutFlow().size();
  TH1D* cutFlowHist = new TH1D("cutFlow", "cutFlow", cutFlowLength, 0, cutFlowLength + 1);
  for (auto& [name, weight] : cutFlowManager->GetCutFlow()) {
    cutFlowHist->SetBinContent(bin, weight);
    cutFlowHist->GetXaxis()->SetBinLabel(bin, name.c_str());
    bin++;
  }
  histogramsHandler->histograms1D["cutFlow"] = cutFlowHist;
}
