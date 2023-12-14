#include "NanoEvent.hpp"

#include "ExtensionsHelpers.hpp"

using namespace std;

TLorentzVector NanoEvent::GetMetFourVector() {
  TLorentzVector metVector;
  metVector.SetPtEtaPhiM(event->Get("MET_pt"), 0, event->Get("MET_phi"), 0);
  return metVector;
}

float NanoEvent::GetMetPt() { return event->Get("MET_pt"); }
