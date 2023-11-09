//  ConfigManager.cpp
//
//  Created by Jeremi Niedziela on 09/08/2023.

#include "ConfigManager.hpp"

#include <type_traits>

#include "Logger.hpp"

using namespace std;

ConfigManager::ConfigManager(std::string *const _configPath) : configPath(move(*_configPath)) {
  if (nullptr == _configPath) throw std::runtime_error{"ConfigManager not initialized"};

  Py_Initialize();

  pythonFile = fopen(configPath.c_str(), "r");

  if (!pythonFile) {
    fatal() << "Could not parse python config\n";
    Py_Finalize();
    exit(1);
  }

  PyRun_SimpleFile(pythonFile, configPath.c_str());
  fclose(pythonFile);

  pythonModule = PyImport_ImportModule("__main__");
  if (!pythonModule) {
    fatal() << "Couldn't import __main__ from the python module\n";
    Py_Finalize();
    exit(1);
  }

  config = PyModule_GetDict(pythonModule);
}

ConfigManager::~ConfigManager() { Py_Finalize(); }

int ConfigManager::GetCollectionSize(PyObject *collection) {
  int size = -1;
  if (PyList_Check(collection))
    size = PyList_Size(collection);
  else if (PyTuple_Check(collection))
    size = PyTuple_Size(collection);
  return size;
}

PyObject *ConfigManager::GetItem(PyObject *collection, int index) {
  PyObject *item;

  if (PyList_Check(collection))
    item = PyList_GetItem(collection, index);
  else if (PyTuple_Check(collection))
    item = PyTuple_GetItem(collection, index);

  return item;
}

//-------------------------------------------------------------------------------------------------
// Methods to retrieve a value/list/dict from the python file
//-------------------------------------------------------------------------------------------------

PyObject *ConfigManager::GetPythonValue(string name) {
  PyObject *pythonValue = PyDict_GetItemString(config, name.c_str());
  if (!pythonValue) {
    throw Exception(("Could not find a value in python config file: " + name).c_str());
  }
  return pythonValue;
}

PyObject *ConfigManager::GetPythonList(string name) {
  PyObject *pythonList = PyDict_GetItemString(config, name.c_str());

  if (!pythonList || (!PyList_Check(pythonList) && !PyTuple_Check(pythonList))) {
    throw Exception(("Could not find a list/tuple in python config file: " + name).c_str());
  }
  return pythonList;
}

PyObject *ConfigManager::GetPythonDict(string name) {
  PyObject *pythonDict = PyDict_GetItemString(config, name.c_str());
  if (!pythonDict || !PyDict_Check(pythonDict)) {
    throw Exception(("Could not find a dict in python config file: " + name).c_str());
  }
  return pythonDict;
}

//-------------------------------------------------------------------------------------------------
// Template specializations to extract a value from the python file
//-------------------------------------------------------------------------------------------------

template <>
void ConfigManager::GetValue<string>(std::string name, string &outputValue) {
  if (name == "inputFilePath" && inputPath != "") {
    outputValue = inputPath;
    return;
  }
  if ((name == "treeOutputFilePath" || name == "histogramsOutputFilePath") && outputPath != "") {
    outputValue = outputPath;
    return;
  }

  PyObject *pythonValue = GetPythonValue(name);
  if (!pythonValue || !PyUnicode_Check(pythonValue)) {
    error() << "Failed retriving python value (string)\n";
    return;
  }
  outputValue = PyUnicode_AsUTF8(pythonValue);
}

template <>
void ConfigManager::GetValue<int>(std::string name, int &outputValue) {
  PyObject *pythonValue = GetPythonValue(name);
  if (!pythonValue || (!PyUnicode_Check(pythonValue) && !PyLong_Check(pythonValue))) {
    error() << "Failed retriving python value (int)\n";
    return;
  }
  outputValue = PyLong_AsLong(pythonValue);
}

template <>
void ConfigManager::GetValue<bool>(std::string name, bool &outputValue) {
  if (name == "applyMuonScaleFactors" && applyMuonScaleFactors.has_value()) {
    outputValue = applyMuonScaleFactors.value();
    return;
  }
  if (name == "applyMuonTriggerScaleFactors" && applyMuonTriggerScaleFactors.has_value()) {
    outputValue = applyMuonTriggerScaleFactors.value();
    return;
  }

  PyObject *pythonValue = GetPythonValue(name);
  if (!pythonValue || (!PyUnicode_Check(pythonValue) && !PyBool_Check(pythonValue))) {
    error() << "Failed retriving python value (int)\n";
    return;
  }
  outputValue = PyLong_AsLong(pythonValue);
}

template <>
void ConfigManager::GetValue<float>(std::string name, float &outputValue) {
  PyObject *pythonValue = GetPythonValue(name);
  if (!pythonValue || !PyFloat_Check(pythonValue)) {
    error() << "Failed retriving python value (float)\n";
    return;
  }
  outputValue = PyFloat_AsDouble(pythonValue);
}

//-------------------------------------------------------------------------------------------------
// Template specializations to extract a vector from the python file
//-------------------------------------------------------------------------------------------------

template <>
void ConfigManager::GetVector<std::string>(std::string name, std::vector<std::string> &outputVector) {
  PyObject *pythonList = GetPythonList(name);

  for (Py_ssize_t i = 0; i < GetCollectionSize(pythonList); ++i) {
    PyObject *item = GetItem(pythonList, i);

    if (!item || !PyUnicode_Check(item)) {
      error() << "Failed retriving python vector<string>\n";
      continue;
    }
    std::string value = PyUnicode_AsUTF8(item);
    outputVector.push_back(value);
  }
}

//-------------------------------------------------------------------------------------------------
// Template specializations to extract a map from the python file
//-------------------------------------------------------------------------------------------------

template <>
void ConfigManager::GetMap<std::string, std::string>(std::string name, std::map<std::string, std::string> &outputMap) {
  PyObject *pythonDict = GetPythonDict(name);

  PyObject *pKey, *pValue;
  Py_ssize_t pos = 0;

  while (PyDict_Next(pythonDict, &pos, &pKey, &pValue)) {
    if (!PyUnicode_Check(pKey) || !PyUnicode_Check(pValue)) {
      error() << "Failed retriving python key-value pair (string-string)\n";
      continue;
    }
    outputMap[PyUnicode_AsUTF8(pKey)] = PyUnicode_AsUTF8(pValue);
  }
}

template <>
void ConfigManager::GetMap<std::string, int>(std::string name, std::map<std::string, int> &outputMap) {
  PyObject *pythonDict = GetPythonDict(name);

  PyObject *pKey, *pValue;
  Py_ssize_t pos = 0;

  while (PyDict_Next(pythonDict, &pos, &pKey, &pValue)) {
    if (!PyUnicode_Check(pKey) || !PyLong_Check(pValue)) {
      error() << "Failed retriving python key-value pair (string-int)\n";
      continue;
    }
    outputMap[PyUnicode_AsUTF8(pKey)] = PyLong_AsLong(pValue);
  }
}

template <>
void ConfigManager::GetMap<std::string, float>(std::string name, std::map<std::string, float> &outputMap) {
  PyObject *pythonDict = GetPythonDict(name);

  PyObject *pKey, *pValue;
  Py_ssize_t pos = 0;

  while (PyDict_Next(pythonDict, &pos, &pKey, &pValue)) {
    if (!PyUnicode_Check(pKey) || (!PyFloat_Check(pValue) && !PyLong_Check(pValue))) {
      error() << "Failed retriving python key-value pair (string-float)\n";
      continue;
    }
    outputMap[PyUnicode_AsUTF8(pKey)] = PyFloat_AsDouble(pValue);
  }
}

template <>
void ConfigManager::GetMap<string, vector<string>>(string name, map<string, vector<string>> &outputMap) {
  PyObject *pythonDict = GetPythonDict(name);

  PyObject *pKey, *pValue;
  Py_ssize_t pos = 0;

  while (PyDict_Next(pythonDict, &pos, &pKey, &pValue)) {
    if (!PyUnicode_Check(pKey) || (!PyList_Check(pValue) && !PyTuple_Check(pValue))) {
      error() << "Failed retriving python key-value pair (string-vector<string>)\n";
      continue;
    }
    vector<string> outputVector;
    for (Py_ssize_t i = 0; i < GetCollectionSize(pValue); ++i) {
      PyObject *item = GetItem(pValue, i);
      outputVector.push_back(PyUnicode_AsUTF8(item));
    }
    outputMap[PyUnicode_AsUTF8(pKey)] = outputVector;
  }
}

//-------------------------------------------------------------------------------------------------
// Other methods
//-------------------------------------------------------------------------------------------------

void ConfigManager::GetExtraEventCollections(map<string, ExtraCollection> &extraEventCollections) {
  PyObject *pythonDict = GetPythonDict("extraEventCollections");

  PyObject *collectionName, *collectionSettings;
  Py_ssize_t pos = 0;

  while (PyDict_Next(pythonDict, &pos, &collectionName, &collectionSettings)) {
    if (!PyUnicode_Check(collectionName)) {
      error() << "Failed retriving python collection name (string)\n";
      continue;
    }
    PyObject *pyKey = nullptr;
    PyObject *pyValue = nullptr;
    Py_ssize_t pos2 = 0;
    ExtraCollection extraCollection;

    while (PyDict_Next(collectionSettings, &pos2, &pyKey, &pyValue)) {
      string keyStr = PyUnicode_AsUTF8(pyKey);
      if (keyStr == "inputCollections") {
        for (Py_ssize_t i = 0; i < GetCollectionSize(pyValue); ++i) {
          PyObject *item = GetItem(pyValue, i);
          extraCollection.inputCollections.push_back(PyUnicode_AsUTF8(item));
        }
      } else if (PyTuple_Check(pyValue)) {
        PyObject *min = GetItem(pyValue, 0);
        PyObject *max = GetItem(pyValue, 1);
        extraCollection.selections[keyStr] = {PyFloat_AsDouble(min), PyFloat_AsDouble(max)};
      } else if (PyBool_Check(pyValue)) {
        extraCollection.flags[keyStr] = PyLong_AsLong(pyValue);
      } else if (PyLong_Check(pyValue)) {
        extraCollection.options[keyStr] = PyLong_AsLong(pyValue);
      }
    }

    extraEventCollections[PyUnicode_AsUTF8(collectionName)] = extraCollection;
  }
}

void ConfigManager::GetScaleFactors(string name, map<string, ScaleFactorsMap> &scaleFactors) {
  PyObject *pythonDict = GetPythonDict(name.c_str());

  PyObject *SFname, *SFvalues;
  Py_ssize_t pos0 = 0;

  while (PyDict_Next(pythonDict, &pos0, &SFname, &SFvalues)) {
    if (!PyUnicode_Check(SFname)) {
      error() << "Failed retriving python scale factor name (string)\n";
      continue;
    }
    string SFnameStr = PyUnicode_AsUTF8(SFname);
    scaleFactors[SFnameStr] = ScaleFactorsMap();

    PyObject *etaBin, *valuesForEta;
    Py_ssize_t pos = 0;

    while (PyDict_Next(SFvalues, &pos, &etaBin, &valuesForEta)) {
      if (!PyTuple_Check(etaBin)) {
        error() << "Failed retriving python eta bin" << endl;
        continue;
      }
      PyObject *ptBin = nullptr;
      PyObject *values = nullptr;
      Py_ssize_t pos2 = 0;

      tuple<float, float> etaBinValues = {PyFloat_AsDouble(GetItem(etaBin, 0)), PyFloat_AsDouble(GetItem(etaBin, 1))};

      while (PyDict_Next(valuesForEta, &pos2, &ptBin, &values)) {
        tuple<float, float> ptBinValues = {PyFloat_AsDouble(GetItem(ptBin, 0)), PyFloat_AsDouble(GetItem(ptBin, 1))};

        PyObject *fieldName = nullptr;
        PyObject *fieldValue = nullptr;
        Py_ssize_t pos3 = 0;

        while (PyDict_Next(values, &pos3, &fieldName, &fieldValue)) {
          scaleFactors[SFnameStr][etaBinValues][ptBinValues][PyUnicode_AsUTF8(fieldName)] = PyFloat_AsDouble(fieldValue);
        }
      }
    }
  }
}

void ConfigManager::GetHistogramsParams(map<std::string, HistogramParams> &histogramsParams, string collectionName) {
  PyObject *pythonList = GetPythonList(collectionName);

  for (Py_ssize_t i = 0; i < GetCollectionSize(pythonList); ++i) {
    PyObject *params = GetItem(pythonList, i);

    HistogramParams histParams;
    string title;

    if (GetCollectionSize(params) == 6) {
      histParams.collection = PyUnicode_AsUTF8(GetItem(params, 0));
      histParams.variable = PyUnicode_AsUTF8(GetItem(params, 1));
      histParams.nBins = PyLong_AsLong(GetItem(params, 2));
      histParams.min = PyFloat_AsDouble(GetItem(params, 3));
      histParams.max = PyFloat_AsDouble(GetItem(params, 4));
      histParams.directory = PyUnicode_AsUTF8(GetItem(params, 5));
      title = histParams.collection + "_" + histParams.variable;
    } else {
      histParams.variable = PyUnicode_AsUTF8(GetItem(params, 0));
      histParams.nBins = PyLong_AsLong(GetItem(params, 1));
      histParams.min = PyFloat_AsDouble(GetItem(params, 2));
      histParams.max = PyFloat_AsDouble(GetItem(params, 3));
      histParams.directory = PyUnicode_AsUTF8(GetItem(params, 4));
      title = histParams.variable;
    }
    histogramsParams[title] = histParams;
  }
}

void ConfigManager::GetHistogramsParams(std::map<std::string, HistogramParams2D> &histogramsParams, string collectionName) {
  PyObject *pythonList = GetPythonList(collectionName);

  for (Py_ssize_t i = 0; i < GetCollectionSize(pythonList); ++i) {
    PyObject *params = GetItem(pythonList, i);

    HistogramParams2D histParams;

    histParams.variable = PyUnicode_AsUTF8(GetItem(params, 0));
    histParams.nBinsX = PyLong_AsLong(GetItem(params, 1));
    histParams.minX = PyFloat_AsDouble(GetItem(params, 2));
    histParams.maxX = PyFloat_AsDouble(GetItem(params, 3));
    histParams.nBinsY = PyLong_AsLong(GetItem(params, 4));
    histParams.minY = PyFloat_AsDouble(GetItem(params, 5));
    histParams.maxY = PyFloat_AsDouble(GetItem(params, 6));
    histParams.directory = PyUnicode_AsUTF8(GetItem(params, 7));

    histogramsParams[histParams.variable] = histParams;
  }
}

void ConfigManager::GetSelections(map<string, pair<float, float>> &selections) {
  PyObject *pythonDict = GetPythonDict("eventSelections");

  PyObject *cutName, *cutValues;
  Py_ssize_t pos = 0;

  while (PyDict_Next(pythonDict, &pos, &cutName, &cutValues)) {
    if (!PyUnicode_Check(cutName)) {
      error() << "Failed retriving python cut name (string)\n";
      continue;
    }
    PyObject *min = GetItem(cutValues, 0);
    PyObject *max = GetItem(cutValues, 1);
    selections[PyUnicode_AsUTF8(cutName)] = {PyFloat_AsDouble(min), PyFloat_AsDouble(max)};
  }
}