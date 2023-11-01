//  HistogramsFiller.cpp
//
//  Created by Jeremi Niedziela on 10/08/2023.

#include "HistogramsFiller.hpp"

#include "ConfigManager.hpp"
#include "ExtensionsHelpers.hpp"

using namespace std;

HistogramsFiller::HistogramsFiller(shared_ptr<HistogramsHandler> histogramsHandler_) : histogramsHandler(histogramsHandler_) {
  auto &config = ConfigManager::GetInstance();

  try {
    config.GetHistogramsParams(defaultHistVariables, "defaultHistParams");
  } catch (const Exception& e) {
    warn() << "Couldn't read defaultHistParams from config file - no default histograms will be included" << endl;
  }

  try {
    config.GetValue("weightsBranchName", weightsBranchName);
  } catch (const Exception& e) {
    info() << "Weights branch not specified -- will assume weight is 1 for all events" << endl;
  }
}

HistogramsFiller::~HistogramsFiller() {}

float HistogramsFiller::GetValue(shared_ptr<PhysicsObject> object, string branchName) {
  if (defaultCollectionsTypes.count(branchName)) {
    string branchType = defaultCollectionsTypes[branchName];
    if (branchType == "Int_t") {
      Int_t value = object->Get(branchName);
      return value;
    }
    if (branchType == "Bool_t") {
      Bool_t value = object->Get(branchName);
      return value;
    }
    if (branchType == "Float_t") {
      Float_t value = object->Get(branchName);
      return value;
    }
    if (branchType == "UChar_t") {
      UChar_t value = object->Get(branchName);
      return value;
    }
    if (branchType == "UShort_t") {
      UShort_t value = object->Get(branchName);
      return value;
    }
    if (branchType == "Short_t") {
      Short_t value = object->Get(branchName);
      return value;
    }
    if (branchType == "UInt_t") {
      UInt_t value = object->Get(branchName);
      return value;
    }
  }

  try {
    Float_t value = object->Get(branchName);
    defaultCollectionsTypes[branchName] = "Float_t";
    return value;
  } catch (BadTypeException& e) {
    try {
      Int_t value = object->Get(branchName);
      defaultCollectionsTypes[branchName] = "Int_t";
      return value;
    } catch (BadTypeException& e) {
      try {
        UChar_t value = object->Get(branchName);
        defaultCollectionsTypes[branchName] = "UChar_t";
        return value;
      } catch (BadTypeException& e) {
        try {
          UShort_t value = object->Get(branchName);
          defaultCollectionsTypes[branchName] = "UShort_t";
          return value;
        } catch (BadTypeException& e) {
          try {
            Short_t value = object->Get(branchName);
            defaultCollectionsTypes[branchName] = "Short_t";
            return value;
          } catch (BadTypeException& e) {
            try {
              UInt_t value = object->Get(branchName);
              defaultCollectionsTypes[branchName] = "UInt_t";
              return value;
            } catch (BadTypeException& e) {
              try {
                Bool_t value = object->Get(branchName);
                defaultCollectionsTypes[branchName] = "Bool_t";
                return value;
              } catch (BadTypeException& e) {
                error() << "Couldn't get value for branch " << branchName << endl;
              }
            }
          }
        }
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

  for (auto& [title, params] : defaultHistVariables) {
    string collectionName = params.collection;
    string branchName = params.variable;

    if (collectionName == "Event") {
      uint eventVariable;
      if (branchName[0] == 'n') {
        eventVariable = event->GetCollectionSize(branchName.substr(1));
      } else {
        eventVariable = event->Get(branchName);
      }
      histogramsHandler->Fill(title, eventVariable, weight);
    } else {
      auto collection = event->GetCollection(collectionName);
      for (auto object : *collection) {
        if(collectionName == "Muon" || object->GetOriginalCollection() == "Muon") {
          auto muon = asMuon(object);
          float muonSF = muon->GetScaleFactor();
          histogramsHandler->Fill(title, GetValue(object, branchName), weight*muonSF);
        }
        else{
          histogramsHandler->Fill(title, GetValue(object, branchName), weight);
        }
      }
    }
  }
}

void HistogramsFiller::FillCutFlow(const std::shared_ptr<CutFlowManager> cutFlowManager) {
  int bin = 1;
  int cutFlowLength = cutFlowManager->GetCutFlow().size();
  TH1D* cutFlowHist = new TH1D("cutFlow", "cutFlow", cutFlowLength, 0, cutFlowLength + 1);


  map<int, pair<string, float>> sortedWeightsAfterCuts;
  for (auto &[cutName, sumOfWeights] : cutFlowManager->GetCutFlow()) {
    string number = cutName.substr(0, cutName.find("_"));
    int index = stoi(number);
    sortedWeightsAfterCuts[index]  = {cutName, sumOfWeights};
  }

  for (auto& [index, values] : sortedWeightsAfterCuts) {
    cutFlowHist->SetBinContent(bin, get<1>(values));
    cutFlowHist->GetXaxis()->SetBinLabel(bin, get<0>(values).c_str());
    bin++;
  }
  histogramsHandler->SetHistogram1D("cutFlow", cutFlowHist);
}
