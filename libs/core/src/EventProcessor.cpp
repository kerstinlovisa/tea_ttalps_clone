//  EventProcessor.cpp
//
//  Created by Jeremi Niedziela on 08/08/2023.

#include "EventProcessor.hpp"

using namespace std;

EventProcessor::EventProcessor() {
  auto &config = ConfigManager::GetInstance();

  try {
    config.GetVector("triggerSelection", triggerNames);
  } catch (const Exception &e) {
    warn() << "Couldn't read triggerSelection from _ file ";
    warn() << "(which may be fine if you're not tyring to apply trigger selection)" << endl;
  }

  try {
    config.GetSelections(eventSelections);
  } catch (const Exception &e) {
    warn() << "Couldn't read eventSelections from config file " << endl;
  }
}

bool EventProcessor::PassesTriggerSelections(const shared_ptr<Event> event) {
  bool passes = true;
  for (auto &triggerName : triggerNames) {
    passes = false;
    try {
      passes = event->Get(triggerName);
    } catch (Exception &) {
      if (find(triggerWarningsPrinted.begin(), triggerWarningsPrinted.end(), triggerName) == triggerWarningsPrinted.end()) {
        warn() << "Trigger not present: " << triggerName << "\n";
        triggerWarningsPrinted.push_back(triggerName);
      }
    }
    if (passes) return true;
  }
  return passes;
}

void EventProcessor::RegisterCuts(shared_ptr<CutFlowManager> cutFlowManager) {
  for (auto &[cutName, cutValues] : eventSelections) {
    cutFlowManager->RegisterCut(cutName);
  }
}

bool EventProcessor::PassesEventSelections(const shared_ptr<Event> event, shared_ptr<CutFlowManager> cutFlowManager) {
  for (auto &[cutName, cutValues] : eventSelections) {

    // TODO: this should be more generic, not only for MET_pt
    if (cutName == "MET_pt") {
      float metPt = event->Get("MET_pt");
      if (!inRange(metPt, cutValues)) return false;
    } else {
      if (!inRange(event->GetCollectionSize(cutName.substr(1)), cutValues)) return false;
    }
    cutFlowManager->UpdateCutFlow(cutName);
  }

  return true;
}

float EventProcessor::GetMaxPt(shared_ptr<Event> event, string collectionName) {
  auto maxPtObject = GetMaxPtObject(event, collectionName);
  if(!maxPtObject) return -1;
  float maxPt = maxPtObject->Get("pt");
  return maxPt;
}

shared_ptr<PhysicsObject> EventProcessor::GetMaxPtObject(shared_ptr<Event> event, string collectionName) {
  auto collection = event->GetCollection(collectionName);
  float maxPt = -1;

  shared_ptr<PhysicsObject> maxPtObject = nullptr;
  for (auto element : *collection) {
    float pt = element->Get("pt");
    if (pt > maxPt) {
      maxPt = pt;
      maxPtObject = element;
    }
  }
  return maxPtObject;
}

float EventProcessor::GetHt(shared_ptr<Event> event, string collectionName) {
  auto collection = event->GetCollection(collectionName);
  float ht = 0;
  for (auto element : *collection) {
    float pt = element->Get("pt");
    ht += pt;
  }
  return ht;
}
