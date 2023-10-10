//  HistogramsHandler.cpp
//
//  Created by Jeremi Niedziela on 08/08/2023.

#include "HistogramsHandler.hpp"

#include "ConfigManager.hpp"
#include "EventProcessor.hpp"
#include "ExtensionsHelpers.hpp"

using namespace std;

HistogramsHandler::HistogramsHandler(std::shared_ptr<ConfigManager> _config) {
  _config->GetHistogramsParams(histParams);
  _config->GetValue("histogramsOutputFilePath", outputPath);
}

HistogramsHandler::~HistogramsHandler() {}

void HistogramsHandler::SetupHistograms() {
  for (auto &[name, params] : histParams) {
    histograms1D[name] = new TH1D(name.c_str(), name.c_str(), params.nBins, params.min, params.max);
  }
}

void HistogramsHandler::SaveHistograms() {
  auto outputFile = new TFile((outputPath).c_str(), "recreate");
  outputFile->cd();

  for (auto &[name, hist] : histograms1D) {
    string outputDir = histParams[name].directory;
    if (!outputFile->Get(outputDir.c_str())) outputFile->mkdir(outputDir.c_str());
    outputFile->cd(outputDir.c_str());
    hist->Write();
  }
  outputFile->Close();
}