import json
from Logger import *

class ScaleFactorsReader:
  def __init__(self):
    self.jsonSubLevelKey = "abseta_pt"
  
  def getMuonScaleFactors(self, filePath):
    with open(filePath) as jsonFile:
      json_content = json.load(jsonFile)
    
    result = {}
    
    for jsonTopLevelKey, values in json_content.items():
      muonSFs = {}
      abseta_pt_data = values[self.jsonSubLevelKey]
    
      if abseta_pt_data is None:
        fatal("Couldn't find the top level key in the JSON file: " + filePath)
        exit(1)
      
      for abseta_key, values_for_eta in abseta_pt_data.items():
        if "abseta" not in abseta_key:
          continue
        
        eta_bin = self.__stringToTuple(abseta_key.replace("abseta:", "").strip("[]"))      
        muonSFs[eta_bin] = {}
        
        for pt_key, values in values_for_eta.items():
          pt_bin = self.__stringToTuple(pt_key.replace("pt:", "").strip("[]"))        
          muonSFs[eta_bin][pt_bin] = values

      result[jsonTopLevelKey] = muonSFs

    return result

  def __stringToTuple(self, input_string):
    return (float(input_string.split(",")[0].strip()), float(input_string.split(",")[1].strip()))
