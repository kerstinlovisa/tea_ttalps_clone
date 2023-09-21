from plotter import *

from ROOT import TFile, TCanvas, TLegend, TObject
import ROOT
import importlib
import sys
import os
import os.path

def main():

  configPath = sys.argv[1]
  if (".py" in configPath):
    configPath = configPath[:-3]
  config = importlib.import_module(configPath)
  
  names = ("signal", "background", "data")
  hists = {name: getStackDict(config, name) for name in names}
  hists_eff = {name: getStackDict(config, name, True) for name in names}
  legends = {name: getLegendDicts(config, name) for name in names}
  legends_eff = {name: getLegendDicts(config, name, True) for name in names}

  backgrounds_included = False
  data_included = False

  input_files = {}
  
  global total_backgrounds_entries
  global total_backgrounds_integral
  global total_backgrounds_cross_section
  total_backgrounds_entries, total_backgrounds_integral, total_backgrounds_cross_section = getTotalBackgroundsIntegral(config)
  
  print(f"Total backgrounds entries: {total_backgrounds_entries}")
  print(f"Total backgrounds integral: {total_backgrounds_integral}")
  print(f"Total backgrounds cross section: {total_backgrounds_cross_section}")
  
  for name, file_info in config.files.items():
    file_name, file_type = file_info
    input_path = config.input_paths[file_type]
    skim = config.skim
    input_files[name] = TFile.Open(input_path+"/"+name+"/"+skim+"/"+file_name, "READ")

    addHistsToStacks(config, input_files, name, hists, legends, file_type)
    addHistsToStacks(config, input_files, name, hists_eff, legends_eff, file_type, True)

    backgrounds_included |= file_type == "background"
    data_included |= file_type == "data"



  drawStacks(config, backgrounds_included, data_included, hists, legends)
  drawStacks(config, backgrounds_included, data_included, hists_eff, legends_eff, True)


if __name__ == "__main__":
  main()
