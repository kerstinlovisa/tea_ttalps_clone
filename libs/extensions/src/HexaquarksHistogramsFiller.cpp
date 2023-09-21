#include "HexaquarksHistogramsFiller.hpp"

#include "ConfigManager.hpp"
#include "ExtensionsHelpers.hpp"

using namespace std;

HexaquarksHistogramsFiller::HexaquarksHistogramsFiller(string configPath, shared_ptr<HistogramsHandler> histogramsHandler_)
    : histogramsHandler(histogramsHandler_) {
  auto configManager = make_unique<ConfigManager>(configPath);
  // configManager->GetValue("nMixedEventsScale", nMixedEventsScale);

  eventProcessor = make_unique<EventProcessor>();
}

HexaquarksHistogramsFiller::~HexaquarksHistogramsFiller() {}

void HexaquarksHistogramsFiller::FillMinvHists(vector<vector<TLorentzVector>> &particle0, vector<vector<TLorentzVector>> &particle1,
                                               vector<vector<TLorentzVector>> &particle2, string histName) {
  histogramsHandler->CheckHistogram(histName);

  string histNameAfterCuts = regex_replace(histName, std::regex("m_inv"), "m_inv_after_cuts");
  histogramsHandler->CheckHistogram(histNameAfterCuts);

  int nEvents = particle0.size();

  for (int iEvent = 0; iEvent < nEvents; iEvent++) {
    for (auto p0 : particle0[iEvent]) {
      for (auto p1 : particle1[iEvent]) {
        for (auto p2 : particle2[iEvent]) {
          auto sum = p0 + p1 + p2;
          histogramsHandler->histograms1D[histName]->Fill(sum.M());

          // if (fabs(p0.Eta() - p1.Eta()) < 1.5 && fabs(p1.Eta() - p2.Eta()) < 1.5 && fabs(p0.Eta() - p2.Eta()) < 1.5 &&
          //     fabs(p0.DeltaPhi(p1)) < 1.5 && fabs(p1.DeltaPhi(p2)) < 1.5 && fabs(p0.DeltaPhi(p2)) < 1.5) {

          if (fabs(p0.DeltaR(p1)) < 1.5 && fabs(p1.DeltaR(p2)) < 1.5 && fabs(p0.DeltaR(p2)) < 1.5) {
            histogramsHandler->histograms1D[histNameAfterCuts]->Fill(sum.M());
          }
        }
      }
    }
  }
}

void HexaquarksHistogramsFiller::FillDeltaHists(vector<vector<TLorentzVector>> &particle0, vector<vector<TLorentzVector>> &particle1,
                                                string histName) {
  histogramsHandler->CheckHistogram(histName);

  int nEvents = particle0.size();

  for (int iEvent = 0; iEvent < nEvents; iEvent++) {
    for (auto p0 : particle0[iEvent]) {
      for (auto p1 : particle1[iEvent]) {
        if (histName.find("delta_eta") != string::npos) {
          histogramsHandler->histograms1D[histName]->Fill(fabs(p0.Eta() - p1.Eta()));
        } else if (histName.find("delta_phi") != string::npos) {
          histogramsHandler->histograms1D[histName]->Fill(fabs(p0.DeltaPhi(p1)));
        } else if (histName.find("delta_r") != string::npos) {
          histogramsHandler->histograms1D[histName]->Fill(fabs(p0.DeltaR(p1)));
        }
      }
    }
  }
}

void HexaquarksHistogramsFiller::FillPtHists(vector<vector<TLorentzVector>> &particle, string histName) {
  histogramsHandler->CheckHistogram(histName);

  int nEvents = particle.size();

  for (int iEvent = 0; iEvent < nEvents; iEvent++) {
    for (auto p0 : particle[iEvent]) {
      histogramsHandler->histograms1D[histName]->Fill(p0.Pt());
    }
  }
}