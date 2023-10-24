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

  input_files = {}
  
  for sample in config.samples:
    input_files[sample.name] = TFile.Open(sample.file_path, "READ")
    
    for hist in config.histograms:
      plotter.addHistosample(hist, sample, input_files[sample.name])
    
    if not hasattr(config, "histograms2D"):
      continue
    
    for hist in config.histograms2D:
      plotter.addHistosample2D(hist, sample, input_files[sample.name])
  
  print("Setting up legends")
  plotter.setupLegends()
  
  print("Building stacks")
  plotter.buildStacks()
  plotter.addHists2D(input_files[sample.name], sample)

  plotter.drawStacks()
  plotter.drawHists2D()

if __name__ == "__main__":
  main()
