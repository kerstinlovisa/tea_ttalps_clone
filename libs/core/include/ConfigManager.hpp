//  ConfigManager.hpp
//
//  Created by Jeremi Niedziela on 09/08/2023.

#ifndef ConfigManager_hpp
#define ConfigManager_hpp

#include <Python.h>

#include "Helpers.hpp"

class ConfigManager {
 public:
  static ConfigManager& GetInstance(){ return getInstanceImpl(); }
  static void Initialize(std::string _configPath) { getInstanceImpl(&_configPath); }

  ConfigManager(ConfigManager const&) = delete;
  void operator=(ConfigManager const&) = delete;

  template <typename T>
  void GetValue(std::string name, T &outputValue);

  template <typename T>
  void GetVector(std::string name, std::vector<T> &outputVector);

  template <typename T, typename U>
  void GetMap(std::string name, std::map<T, U> &outputMap);

  void GetExtraEventCollections(std::map<std::string, ExtraCollection> &extraEventCollections);
  void GetHistogramsParams(std::map<std::string, HistogramParams> &histogramsParams, std::string collectionName);
  void GetHistogramsParams(std::map<std::string, HistogramParams2D> &histogramsParams, std::string collectionName);

  void GetScaleFactors(std::string name, std::map<std::string, ScaleFactorsMap> &scaleFactors);

  void GetSelections(std::map<std::string, std::pair<float, float>> &selections);

  void SetInputPath(std::string path) { inputPath = path; }
  void SetOutputPath(std::string path) { outputPath = path; }
  void SetApplyMuonScaleFactors(bool apply) { applyMuonScaleFactors = apply; }
  void SetApplyMuonTriggerScaleFactors(bool apply) { applyMuonTriggerScaleFactors = apply; }

 private:
  std::string configPath;
  ConfigManager(std::string* const _configPath);
  ~ConfigManager();

  static ConfigManager& getInstanceImpl(std::string* const _configPath = nullptr)
  {
    static ConfigManager instance{ _configPath };
    return instance;
  }

  FILE *pythonFile;
  PyObject *pythonModule;
  PyObject *config;

  PyObject *GetPythonValue(std::string name);
  PyObject *GetPythonList(std::string name);
  PyObject *GetPythonDict(std::string name);

  int GetCollectionSize(PyObject *collection);
  PyObject *GetItem(PyObject *collection, int index);

  std::string inputPath = "";
  std::string outputPath = "";
  std::optional<bool> applyMuonScaleFactors = std::nullopt;
  std::optional<bool> applyMuonTriggerScaleFactors = std::nullopt;
};

#endif /* ConfigManager_hpp */
