#ifndef HexaquarksHistogramsFiller_hpp
#define HexaquarksHistogramsFiller_hpp

#include "Event.hpp"
#include "EventProcessor.hpp"
#include "Helpers.hpp"
#include "HepMCParticle.hpp"
#include "HistogramsHandler.hpp"

class HexaquarksHistogramsFiller {
 public:
  HexaquarksHistogramsFiller(std::string configPath, std::shared_ptr<HistogramsHandler> histogramsHandler_);
  ~HexaquarksHistogramsFiller();

  void FillMinvHists(std::vector<std::vector<TLorentzVector>> &particle0, std::vector<std::vector<TLorentzVector>> &particle1,
                     std::vector<std::vector<TLorentzVector>> &particle2, std::string histName);

  void FillDeltaHists(std::vector<std::vector<TLorentzVector>> &particle0, std::vector<std::vector<TLorentzVector>> &particle1,
                      std::string histName);

  void FillPtHists(std::vector<std::vector<TLorentzVector>> &particle, std::string histName);

 private:
  std::shared_ptr<HistogramsHandler> histogramsHandler;
  std::unique_ptr<EventProcessor> eventProcessor;

  float nMixedEventsScale;
};

#endif /* HexaquarksHistogramsFiller_hpp */
