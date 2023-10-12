//  HistogramsFiller.hpp
//
//  Created by Jeremi Niedziela on 10/08/2023.

#ifndef HistogramsFiller_hpp
#define HistogramsFiller_hpp

#include "Event.hpp"
#include "Helpers.hpp"
#include "HistogramsHandler.hpp"
#include "CutFlowManager.hpp"
#include "EventProcessor.hpp"

class HistogramsFiller {
 public:
  HistogramsFiller(std::shared_ptr<HistogramsHandler> histogramsHandler_);
  ~HistogramsFiller();

  void FillDefaultVariables(const std::shared_ptr<Event> event);

  void FillCutFlow(const std::shared_ptr<CutFlowManager> cutFlowManager);  

 private:
  std::shared_ptr<HistogramsHandler> histogramsHandler;
  std::map<std::string, HistogramParams> defaultHistVariables;
  std::string weightsBranchName;

  std::map<std::string, std::string> defaultCollectionsTypes;

  float GetValue(std::shared_ptr<PhysicsObject> object, std::string branchName);
};

#endif /* HistogramsFiller_hpp */
