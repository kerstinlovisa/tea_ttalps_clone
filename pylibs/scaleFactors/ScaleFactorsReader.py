import json

class ScaleFactorsReader:
  def __init__(self):
    self.muonSFsPath = "../data/NUM_TrackerMuons_DEN_genTracks_Z_abseta_pt.json"
    
  def getMuonScaleFactors(self):
    with open(self.muonSFsPath) as jsonFile:
      json_content = json.load(jsonFile)
      
    muonSFs = {}

    abseta_pt_data = json_content["NUM_TrackerMuons_DEN_genTracks"]["abseta_pt"]
    
    for abseta_key, values_for_eta in abseta_pt_data.items():
      if "abseta" not in abseta_key:
        continue
      
      eta_bin = self.__stringToTuple(abseta_key.replace("abseta:", "").strip("[]"))      
      muonSFs[eta_bin] = {}
      
      for pt_key, values in values_for_eta.items():
        pt_bin = self.__stringToTuple(pt_key.replace("pt:", "").strip("[]"))        
        muonSFs[eta_bin][pt_bin] = values

    return muonSFs

  def __stringToTuple(self, input_string):
    return (float(input_string.split(",")[0].strip()), float(input_string.split(",")[1].strip()))
