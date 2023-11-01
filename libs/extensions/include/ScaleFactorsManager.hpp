//  ScaleFactorsManager.hpp
//
//  Created by Jeremi Niedziela on 01/11/2023.

#ifndef ScaleFactorsManager_hpp
#define ScaleFactorsManager_hpp

#include "Helpers.hpp"

struct MuonID;

class ScaleFactorsManager {
 public:
  static ScaleFactorsManager &GetInstance() {
    static ScaleFactorsManager instance;
    return instance;
  }

  ScaleFactorsManager(ScaleFactorsManager const &) = delete;
  void operator=(ScaleFactorsManager const &) = delete;

  float GetMuonRecoScaleFactor(float eta, float pt);
  float GetMuonIDScaleFactor(float eta, float pt, MuonID id);

 private:
  ScaleFactorsManager();
  ~ScaleFactorsManager() {}

  static ScaleFactorsManager &getInstanceImpl() {
    static ScaleFactorsManager instance;
    return instance;
  }

  std::map<std::string, TH2D *> muonSFvalues;

  void CreateMuonSFsHistogram(const ScaleFactorsMap &muonSFs, std::string outputPath, std::string histName);
  void BringEtaPtToHistRange(TH2D *hist, float &eta, float &pt);
};

struct MuonID {
  MuonID(bool soft_, bool highPt_, bool trkHighPt_, bool tight_, bool mediumPrompt_, bool medium_, bool loose_)
      : soft(soft_), highPt(highPt_), trkHighPt(trkHighPt_), tight(tight_), mediumPrompt(mediumPrompt_), medium(medium_), loose(loose_) {}

  bool soft;
  bool highPt;
  bool trkHighPt;
  bool tight;
  bool mediumPrompt;
  bool medium;
  bool loose;

  bool PassesAnyId() { return soft || highPt || trkHighPt || tight || mediumPrompt || medium || loose; }

  void Print() {
    if (soft) info() << "soft " << std::endl;
    if (highPt) info() << "highPt " << std::endl;
    if (trkHighPt) info() << "trkHighPt " << std::endl;
    if (tight) info() << "tight " << std::endl;
    if (mediumPrompt) info() << "mediumPrompt " << std::endl;
    if (medium) info() << "medium " << std::endl;
    if (loose) info() << "loose " << std::endl;
  }
};

#endif /* ScaleFactorsManager_hpp */
