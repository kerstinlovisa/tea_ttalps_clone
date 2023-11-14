#include "ConfigManager.hpp"
#include "EventReader.hpp"
#include "ExtensionsHelpers.hpp"
#include "UserExtensionsHelpers.hpp"
#include "TTAlpsEvent.hpp"

using namespace std;

void CheckArgs(int argc, char **argv) {
  if (argc != 2 && argc != 4) {
    fatal() << "Usage: " << argv[0] << " config_path"<<endl;
    fatal() << "or"<<endl;
    fatal() << argv[0] << " config_path input_path output_path"<<endl;
    exit(1);
  }
}

int main(int argc, char **argv) {
  CheckArgs(argc, argv);
  ConfigManager::Initialize(argv[1]);

  if(argc == 4){
    auto &config = ConfigManager::GetInstance();
    config.SetInputPath(argv[2]);
    config.SetOutputPath(argv[3]);
  }

  auto eventReader = make_shared<EventReader>();

  map<string, int> categories;

  // setup printouts such that comma is used as decimal separator
  cout.imbue(locale("it_IT.UTF-8"));
  
  map<int, int> nJets;

  for (int iEvent = 0; iEvent < eventReader->GetNevents(); iEvent++) {
    auto event = eventReader->GetEvent(iEvent);
    auto ttalpsEvent = asTTAlpsEvent(event);

    string category = ttalpsEvent->GetTTbarEventCategory();

    // if category not yet in map, add it, else increment it
    if (categories.find(category) == categories.end()) {
      categories[category] = 1;
    } else {
      categories[category]++;
    }
    nJets[event->GetCollectionSize("Jet")]++;
  }

  // create a new map with categories, but merge entries with keys: "ee", "emu", "mumu", "etau", "mutau", "tautau" into one entry with key "ll"
  map<string, int> categoriesMerged;
  for (auto &category : categories) {
    string key = category.first;
    if (key == "ee" || key == "emu" || key == "mumu" || key == "etau" || key == "mutau" || key == "tautau") {
      key = "ll";
    }
    
    if (categoriesMerged.find(key) == categoriesMerged.end()) {
      categoriesMerged[key] = category.second;
    } else {
      categoriesMerged[key] += category.second;
    }
  }

  // print fraction of events in each category
  for (auto &category : categoriesMerged) {
    info() << category.first << ": " << (double)category.second / eventReader->GetNevents();
    // print also uncertainty of the fraction
    info() << " +/- " << sqrt((double)category.second * (1 - (double)category.second / eventReader->GetNevents())) / eventReader->GetNevents() << endl;
  }

  // print fraction of events with given number of jets
  for (auto &nJet : nJets) {
    info() << nJet.first << " jets: " << (double)nJet.second / eventReader->GetNevents();
    // print also uncertainty of the fraction
    info() << " +/- " << sqrt((double)nJet.second * (1 - (double)nJet.second / eventReader->GetNevents())) / eventReader->GetNevents() << endl;
  }

  return 0;
}