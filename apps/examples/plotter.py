from HistogramPlotter import HistogramPlotter

from ROOT import TFile
import importlib
import sys


def getConfig():
  configPath = sys.argv[1]
  if (".py" in configPath):
    configPath = configPath[:-3]
  config = importlib.import_module(configPath)
  return config


def main():

  config = getConfig()
  plotter = HistogramPlotter(config)
  
  names = ("signal", "background", "data")
  hists = {name: plotter.getStackDict(name) for name in names}
  legends = {name: plotter.getLegendDicts(name) for name in names}

  backgrounds_included = False
  data_included = False

  input_files = {}
  
  for sample in config.samples:
    input_files[sample.name] = TFile.Open(sample.file_path, "READ")

    plotter.addHistsToStacks(input_files[sample.name], sample, hists, legends)

    backgrounds_included |= sample.sample_type == "background"
    data_included |= sample.sample_type == "data"

  plotter.drawStacks(backgrounds_included, data_included, hists, legends)

if __name__ == "__main__":
  main()
