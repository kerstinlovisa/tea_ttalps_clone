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
    _config->GetHistogramsParams(defaultHistVariables, "defaultHistParams");
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

float HistogramsFiller::GetValue(shared_ptr<PhysicsObject> object, string branchName) {

  if(defaultCollectionsTypes.count(branchName)){
    string branchType = defaultCollectionsTypes[branchName];
    if(branchType == "int"){
      int value = object->Get(branchName);
      return value;
    }
    if(branchType == "bool"){
      bool value = object->Get(branchName);
      return value;
    }
    if(branchType == "float"){
      float value = object->Get(branchName);
      return value;
    }
  }

  try {
    float value = object->Get(branchName);
    defaultCollectionsTypes[branchName] = "float";
    return value;
  } catch (BadTypeException& e) {
    try {
      int value = object->Get(branchName);
      defaultCollectionsTypes[branchName] = "int";
      return value;
    } catch (BadTypeException& e) {
      try {
        bool value = object->Get(branchName);
        defaultCollectionsTypes[branchName] = "bool";
        return value;
      } catch (BadTypeException& e) {
        error() << "Couldn't get value for branch " << branchName << endl;
      }
    }
  }
  return 0;
}

void HistogramsFiller::FillDefaultVariables(const std::shared_ptr<Event> event) {
  float weight = 1.0;
  try {
    weight = event->Get(weightsBranchName);
  } catch (...) {
  }

  for (auto& [branchName, params] : defaultHistVariables) {
    string collectionName = params.collection;

    if (collectionName == "Event") {
      uint eventVariable;
      if (branchName[0] == 'n') {
        eventVariable = event->GetCollectionSize(branchName.substr(1));
      } else {
        eventVariable = event->Get(branchName);
      }
      histogramsHandler->histograms1D[branchName]->Fill(eventVariable, weight);
    } else {
      auto collection = event->GetCollection(collectionName);
      for (auto object : *collection) {
        histogramsHandler->histograms1D[branchName]->Fill(GetValue(object, branchName), weight);
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
