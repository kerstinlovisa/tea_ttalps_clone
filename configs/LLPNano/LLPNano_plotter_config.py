import ROOT
from ROOT import TColor
from Sample import Sample, SampleType
from Legend import Legend
from Histogram import Histogram
from HistogramNormalizer import NormalizationType

basePath = "/nfs/dust/cms/user/lrygaard/ttalps_cms/"
output_path = "../plots"

luminosity = 1. # pb^-1
# luminosity = 63670. # pb^-1
# luminosity = 59830. # recommended lumi from https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2

legends = {
  SampleType.signal: Legend(0.15,0.85,0.25,0.89, "l"),
  SampleType.background: Legend(0.7,0.65,0.85,0.89, "f"),
  SampleType.data: Legend(0.15,0.8,0.25,0.85, "pl"),
}

canvas_size = (800, 600)
show_ratio_plots = False
# background_uncertainty_style = 3244 # available styles: https://root.cern.ch/doc/master/classTAttFill.html
# background_uncertainty_color = ROOT.kBlack
# background_uncertainty_alpha = 0.3


histograms = (
#           name                            title     norm_type                           rebin xmin xmax ymin ymax,  xlabel              ylabel

  Histogram("Event_nMuon",                  "",       True, NormalizationType.none,       1,    0,    10,       1e1,   1e6,   "Number of muons",              "#events"),             
  Histogram("Muon_pt",                      "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e6,   "Muon p_{T}",                   "#events"),              
  Histogram("Muon_eta",                     "",       True, NormalizationType.none,       1,    -3.5, 3.5,      1e0,   1e6,   "Muon #eta",                    "#events"),              
  Histogram("Muon_dxy",                     "",       True, NormalizationType.none,       10,   -800,800,     1e-2,  1e6,   "Muon d_{xy}",                  "#events"),              
  Histogram("Muon_dz",                      "",       True, NormalizationType.none,       10,   -800,800,     1e-2,  1e6,   "Muon d_{z}",                   "#events"),              
  Histogram("Muon_ip3d",                    "",       True, NormalizationType.none,       10,   0,    800,     1e-2,  1e6,   "Muon |ip3D|",                  "#events"),              
  Histogram("Muon_sip3d",                   "",       True, NormalizationType.none,       10,   0,    800,     1e-2,  1e6,   "Muon |ip3D| significance",     "#events"),       
  Histogram("Muon_trkNumPlanes",            "",       True, NormalizationType.none,       1,    0,    50,       1e1,   1e6,   "Number of muon tracker planes","#events"),
  Histogram("Muon_trkNumHits",              "",       True, NormalizationType.none,       1,    0,    50,       1e1,   1e6,   "Number of muon hits",          "#events"),
  Histogram("Muon_trkNumDTHits",            "",       True, NormalizationType.none,       1,    0,    50,       1e1,   1e6,   "Number of muon DT hits",       "#events"),
  Histogram("Muon_trkNumCSCHits",           "",       True, NormalizationType.none,       1,    0,    50,       1e1,   1e6,   "Number of muon CSC hits",      "#events"),
  Histogram("Muon_normChi2",                "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Muon #chi^{2}",                "#events"),                
  
  Histogram("Event_nMuonExtended",          "",       True, NormalizationType.none,       1,    0,    10,       1e1,   1e6,   "Number of muons",              "#events"),             
  Histogram("MuonExtended_dxyPV",           "",       True, NormalizationType.none,       1,    -50,  50,       1e-2,  1e6,   "Muon d_{xy}^{PV} [cm]",             "#events"),      
  Histogram("MuonExtended_dxyPVErr",        "",       True, NormalizationType.none,       1,    0,    50,       1e-2,  1e6,   "Muon d_{xy}^{PV} error",       "#events"),    
  Histogram("MuonExtended_dzPV",            "",       True, NormalizationType.none,       1,    -50,  50,       1e-2,  1e6,   "Muon d_{z}^{PV} [cm]",              "#events"),      
  Histogram("MuonExtended_dzPVErr",         "",       True, NormalizationType.none,       1,    0,    50,       1e-2,  1e6,   "Muon d_{z}^{PV} error",        "#events"),    
  Histogram("MuonExtended_dxyPVTraj",       "",       True, NormalizationType.none,       1,    -50,  50,       1e-2,  1e6,   "Muon trajectory d_{xy}^{PV} [cm]",  "#events"),      
  Histogram("MuonExtended_dxyPVTrajErr",    "",       True, NormalizationType.none,       1,    0,    50,       1e-2,  1e6,   "Muon trajectory d_{xy}^{PV} error","#events"),      
  Histogram("MuonExtended_dxyPVAbs",        "",       True, NormalizationType.none,       1,    0,    50,       1e-2,  1e6,   "Muon |d_{xy}^{PV}|",            "#events"),      
  Histogram("MuonExtended_dxyPVAbsErr",     "",       True, NormalizationType.none,       1,    -50,  50,       1e-2,  1e6,   "Muon |d_{xy}^{PV}| error",      "#events"),      
  Histogram("MuonExtended_dxyPVSigned",     "",       True, NormalizationType.none,       1,    -50,  50,       1e-2,  1e6,   "Muon signed d_{xy}^{PV} [cm]",       "#events"),      
  Histogram("MuonExtended_dxyPVSignedErr",  "",       True, NormalizationType.none,       1,    0,    50,       1e-2,  1e6,   "Muon signed d_{xy}^{PV} error", "#events"),      
  Histogram("MuonExtended_ip3DPVAbs",       "",       True, NormalizationType.none,       1,    0,    50,       1e-2,  1e6,   "Muon |ip3D|",                   "#events"),    
  Histogram("MuonExtended_ip3DPVAbsErr",    "",       True, NormalizationType.none,       1,    0,    50,       1e-2,  1e6,   "Muon |ip3D| error",             "#events"),    
  Histogram("MuonExtended_ip3DPVSigned",    "",       True, NormalizationType.none,       1,    -50,  50,       1e-2,  1e6,   "Muon signed ip3D",              "#events"),      
  Histogram("MuonExtended_ip3DPVSignedErr", "",       True, NormalizationType.none,       1,    0,    50,       1e-2,  1e6,   "Muon signed ip3D error",        "#events"),      
  
  # Histogram("MuonExtended_dxyBS",           "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon d_{xy}^{BS}",             "#events"),      
  # Histogram("MuonExtended_dxyBSErr",        "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon d_{xy}^{BS} error",       "#events"),    
  # Histogram("MuonExtended_dzBS",            "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon d_{z}^{BS}",              "#events"),      
  # Histogram("MuonExtended_dzBSErr",         "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon d_{z}^{BS} error",        "#events"),    
  # Histogram("MuonExtended_dxyBSTraj",       "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon trajectory d_{xy}^{BS}",  "#events"),      
  # Histogram("MuonExtended_dxyBSTrajErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon trajectory d_{xy}^{BS} error","#events"),      
  # Histogram("MuonExtended_dxyBSAbs",        "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |d_{xy}^{BS}|",            "#events"),      
  # Histogram("MuonExtended_dxyBSAbsErr",     "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon |d_{xy}^{BS}| error",      "#events"),      
  # Histogram("MuonExtended_dxyBSSigned",     "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon signed d_{xy}^{BS}",       "#events"),      
  # Histogram("MuonExtended_dxyBSSignedErr",  "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon signed d_{xy}^{BS} error", "#events"),      
  # Histogram("MuonExtended_ip3DBSAbs",       "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |ip3D|",                   "#events"),    
  # Histogram("MuonExtended_ip3DBSAbsErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |ip3D| error",             "#events"),    
  # Histogram("MuonExtended_ip3DBSSigned",    "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon signed ip3D",              "#events"),      
  # Histogram("MuonExtended_ip3DBSSignedErr", "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon signed ip3D error",        "#events"),  

  Histogram("Event_nDSAMuon",          "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    10,       1e-1,   1e6,   "Number of muons",              "#events"),
  Histogram("DSAMuon_pt",              "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    50,       1e1,   1e6,   "Muon p_{T}",                   "#events"),              
  Histogram("DSAMuon_eta",             "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    -3.5, 3.5,      1e0,   1e6,   "Muon #eta",                    "#events"),              
  Histogram("DSAMuon_trkNumPlanes",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    50,       1e1,  1e6,   "Number of muon tracker planes","#events"),
  Histogram("DSAMuon_trkNumHits",      "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    50,       1e1,  1e6,   "Number of muon hits",          "#events"),
  Histogram("DSAMuon_trkNumDTHits",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    50,       1e1,  1e6,   "Number of muon DT hits",       "#events"),
  Histogram("DSAMuon_trkNumCSCHits",   "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    50,       1e-1,  1e6,   "Number of muon CSC hits",      "#events"),
  Histogram("DSAMuon_normChi2",        "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Muon #chi^{2}",                "#events"), 

  Histogram("DSAMuon_chi2overndof",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Muon #chi^{2}/dof",             "#events"), 
  Histogram("DSAMuon_ptErroverpt",     "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    50,       1e1,   1e6,   "Muon #sigma_{pT}/p_{T}",        "#events"), 
  Histogram("DSAMuon_DThitsCheck",     "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Muon DT-CSC hits check",        "#events"), 

  Histogram("DSAMuon_dxyPV",           "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   -800,800,     1e-2,  1e6,   "Muon d_{xy}^{PV} [cm]",             "#events"),      
  Histogram("DSAMuon_dxyPVErr",        "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   0,    800,     1e-2,  1e6,   "Muon d_{xy}^{PV} error",       "#events"),    
  Histogram("DSAMuon_dzPV",            "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   -800,800,     1e-2,  1e6,   "Muon d_{z}^{PV} [cm]",              "#events"),      
  Histogram("DSAMuon_dzPVErr",         "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   0,    800,     1e-2,  1e6,   "Muon d_{z}^{PV} error",        "#events"),    
  Histogram("DSAMuon_dxyPVTraj",       "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   -800,800,     1e-2,  1e6,   "Muon trajectory d_{xy}^{PV} [cm]",  "#events"),      
  Histogram("DSAMuon_dxyPVTrajErr",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   0,    800,     1e-2,  1e6,   "Muon trajectory d_{xy}^{PV} error","#events"),      
  Histogram("DSAMuon_dxyPVAbs",        "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   0,    800,     1e-2,  1e6,   "Muon |d_{xy}^{PV}|",            "#events"),      
  Histogram("DSAMuon_dxyPVAbsErr",     "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   -800,800,     1e-2,  1e6,   "Muon |d_{xy}^{PV}| error",      "#events"),      
  Histogram("DSAMuon_dxyPVSigned",     "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   -800,800,     1e-2,  1e6,   "Muon signed d_{xy}^{PV} [cm]",       "#events"),      
  Histogram("DSAMuon_dxyPVSignedErr",  "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   0,    800,     1e-2,  1e6,   "Muon signed d_{xy}^{PV} error", "#events"),      
  Histogram("DSAMuon_ip3DPVAbs",       "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   0,    800,     1e-2,  1e6,   "Muon |ip3D|",                   "#events"),    
  Histogram("DSAMuon_ip3DPVAbsErr",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   0,    800,     1e-2,  1e6,   "Muon |ip3D| error",             "#events"),    
  Histogram("DSAMuon_ip3DPVSigned",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   -800,800,     1e-2,  1e6,   "Muon signed ip3D",              "#events"),      
  Histogram("DSAMuon_ip3DPVSignedErr", "DisplacedStandAlone Muons",       True, NormalizationType.none,       10,   0,    800,     1e-2,  1e6,   "Muon signed ip3D error",        "#events"),

  Histogram("Event_nLooseDSAMuon",          "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    10,       1e1,   1e6,   "Number of muons",              "#events"),
  Histogram("LooseDSAMuon_pt",              "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e6,   "Muon p_{T}",                   "#events"),              
  Histogram("LooseDSAMuon_eta",             "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    -3.5, 3.5,      1e0,   1e6,   "Muon #eta",                    "#events"),              
  Histogram("LooseDSAMuon_trkNumPlanes",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    50,       1e-1,  1e6,   "Number of muon tracker planes","#events"),
  Histogram("LooseDSAMuon_trkNumHits",      "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    50,       1e-1,  1e6,   "Number of muon hits",          "#events"),
  Histogram("LooseDSAMuon_trkNumDTHits",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    50,       1e-1,  1e6,   "Number of muon DT hits",       "#events"),
  Histogram("LooseDSAMuon_trkNumCSCHits",   "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    50,       1e-1,  1e6,   "Number of muon CSC hits",      "#events"),
  Histogram("LooseDSAMuon_normChi2",        "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Muon #chi^{2}",                "#events"), 

  Histogram("LooseDSAMuon_dxyPV",           "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    -800,800,     1e-2,  1e6,   "Muon d_{xy}^{PV} [cm]",             "#events"),      
  Histogram("LooseDSAMuon_dxyPVErr",        "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    800,     1e-2,  1e6,   "Muon d_{xy}^{PV} error",       "#events"),    
  Histogram("LooseDSAMuon_dzPV",            "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    -800,800,     1e-2,  1e6,   "Muon d_{z}^{PV} [cm]",              "#events"),      
  Histogram("LooseDSAMuon_dzPVErr",         "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    800,     1e-2,  1e6,   "Muon d_{z}^{PV} error",        "#events"),    
  Histogram("LooseDSAMuon_dxyPVTraj",       "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    -800,800,     1e-2,  1e6,   "Muon trajectory d_{xy}^{PV} [cm]",  "#events"),      
  Histogram("LooseDSAMuon_dxyPVTrajErr",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    800,     1e-2,  1e6,   "Muon trajectory d_{xy}^{PV} error","#events"),      
  Histogram("LooseDSAMuon_dxyPVAbs",        "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    800,     1e-2,  1e6,   "Muon |d_{xy}^{PV}|",            "#events"),      
  Histogram("LooseDSAMuon_dxyPVAbsErr",     "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    -800,800,     1e-2,  1e6,   "Muon |d_{xy}^{PV}| error",      "#events"),      
  Histogram("LooseDSAMuon_dxyPVSigned",     "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    -800,800,     1e-2,  1e6,   "Muon signed d_{xy}^{PV} [cm]",       "#events"),      
  Histogram("LooseDSAMuon_dxyPVSignedErr",  "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    800,     1e-2,  1e6,   "Muon signed d_{xy}^{PV} error", "#events"),      
  Histogram("LooseDSAMuon_ip3DPVAbs",       "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    800,     1e-2,  1e6,   "Muon |ip3D|",                   "#events"),    
  Histogram("LooseDSAMuon_ip3DPVAbsErr",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    800,     1e-2,  1e6,   "Muon |ip3D| error",             "#events"),    
  Histogram("LooseDSAMuon_ip3DPVSigned",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    -800,800,     1e-2,  1e6,   "Muon signed ip3D",              "#events"),      
  Histogram("LooseDSAMuon_ip3DPVSignedErr", "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    800,     1e-2,  1e6,   "Muon signed ip3D error",        "#events"),      
  
  # Histogram("DSAMuon_dxyBS",           "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon d_{xy}^{BS}",             "#events"),      
  # Histogram("DSAMuon_dxyBSErr",        "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon d_{xy}^{BS} error",       "#events"),    
  # Histogram("DSAMuon_dzBS",            "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon d_{z}^{BS}",              "#events"),      
  # Histogram("DSAMuon_dzBSErr",         "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon d_{z}^{BS} error",        "#events"),    
  # Histogram("DSAMuon_dxyBSTraj",       "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon trajectory d_{xy}^{BS}",  "#events"),      
  # Histogram("DSAMuon_dxyBSTrajErr",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon trajectory d_{xy}^{BS} error","#events"),      
  # Histogram("DSAMuon_dxyBSAbs",        "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |d_{xy}^{BS}|",            "#events"),      
  # Histogram("DSAMuon_dxyBSAbsErr",     "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon |d_{xy}^{BS}| error",      "#events"),      
  # Histogram("DSAMuon_dxyBSSigned",     "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon signed d_{xy}^{BS}",       "#events"),      
  # Histogram("DSAMuon_dxyBSSignedErr",  "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon signed d_{xy}^{BS} error", "#events"),      
  # Histogram("DSAMuon_ip3DBSAbs",       "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |ip3D|",                   "#events"),    
  # Histogram("DSAMuon_ip3DBSAbsErr",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |ip3D| error",             "#events"),    
  # Histogram("DSAMuon_ip3DBSSigned",    "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon signed ip3D",              "#events"),      
  # Histogram("DSAMuon_ip3DBSSignedErr", "DisplacedStandAlone Muons",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon signed ip3D error",        "#events"),   

  # Histogram("nElectron",                    "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Number of electrons",          "#events"),             
  # Histogram("Electron_pt",                  "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Electron p_{T}",               "#events"),          
  # Histogram("Electron_eta",                 "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Electron #eta",                "#events"),          
  # Histogram("Electron_dxy",                 "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Electron d_{xy}",              "#events"),          
  # Histogram("Electron_dz",                  "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Electron d_{z}",               "#events"),          
  # Histogram("Electron_ip3d",                "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Electron Muon |ip3D|",         "#events"),          
  # Histogram("Electron_sip3d",               "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Electron Muon |ip3D| significance","#events"),
  # Histogram("Electron_normChi2",            "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Electron #chi^{2}",            "#events"),                

  # Histogram("Event_nElectronExtended",          "",       True, NormalizationType.none,       1,    0,    10,       1e1,   1e6,   "Number of Electrons",              "#events"),             
  # Histogram("ElectronExtended_dxyPV",           "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Electron d_{xy}^{PV} [cm]",             "#events"),      
  # Histogram("ElectronExtended_dxyPVErr",        "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Electron d_{xy}^{PV} error",       "#events"),    
  # Histogram("ElectronExtended_dzPV",            "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Electron d_{z}^{PV} [cm]",              "#events"),      
  # Histogram("ElectronExtended_dzPVErr",         "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Electron d_{z}^{PV} error",        "#events"),    
  # Histogram("ElectronExtended_dxyPVTraj",       "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Electron trajectory d_{xy}^{PV} [cm]",  "#events"),      
  # Histogram("ElectronExtended_dxyPVTrajErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron trajectory d_{xy}^{PV} error","#events"),      
  # Histogram("ElectronExtended_dxyPVAbs",        "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron |d_{xy}^{PV}|",            "#events"),      
  # Histogram("ElectronExtended_dxyPVAbsErr",     "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Electron |d_{xy}^{PV}| error",      "#events"),      
  # Histogram("ElectronExtended_dxyPVSigned",     "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Electron signed d_{xy}^{PV} [cm]",       "#events"),      
  # Histogram("ElectronExtended_dxyPVSignedErr",  "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron signed d_{xy}^{PV} error", "#events"),      
  # Histogram("ElectronExtended_ip3DPVAbs",       "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron |ip3D|",                   "#events"),    
  # Histogram("ElectronExtended_ip3DPVAbsErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron |ip3D| error",             "#events"),    
  # Histogram("ElectronExtended_ip3DPVSigned",    "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Electron signed ip3D",              "#events"),      
  # Histogram("ElectronExtended_ip3DPVSignedErr", "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron signed ip3D error",        "#events"),      
  
  # Histogram("ElectronExtended_dxyBS",           "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron d_{xy}^{BS}",             "#events"),      
  # Histogram("ElectronExtended_dxyBSErr",        "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Electron d_{xy}^{BS} error",       "#events"),    
  # Histogram("ElectronExtended_dzBS",            "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron d_{z}^{BS}",              "#events"),      
  # Histogram("ElectronExtended_dzBSErr",         "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Electron d_{z}^{BS} error",        "#events"),    
  # Histogram("ElectronExtended_dxyBSTraj",       "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron trajectory d_{xy}^{BS}",  "#events"),      
  # Histogram("ElectronExtended_dxyBSTrajErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron trajectory d_{xy}^{BS} error","#events"),      
  # Histogram("ElectronExtended_dxyBSAbs",        "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron |d_{xy}^{BS}|",            "#events"),      
  # Histogram("ElectronExtended_dxyBSAbsErr",     "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Electron |d_{xy}^{BS}| error",      "#events"),      
  # Histogram("ElectronExtended_dxyBSSigned",     "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron signed d_{xy}^{BS}",       "#events"),      
  # Histogram("ElectronExtended_dxyBSSignedErr",  "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron signed d_{xy}^{BS} error", "#events"),      
  # Histogram("ElectronExtended_ip3DBSAbs",       "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron |ip3D|",                   "#events"),    
  # Histogram("ElectronExtended_ip3DBSAbsErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron |ip3D| error",             "#events"),    
  # Histogram("ElectronExtended_ip3DBSSigned",    "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Electron signed ip3D",              "#events"),      
  # Histogram("ElectronExtended_ip3DBSSignedErr", "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Electron signed ip3D error",        "#events"),  

  # Histogram("nLowPtElectron",                    "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Number of LowPtelectrons",          "#events"),             
  # Histogram("LowPtElectron_pt",                  "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "LowPtElectron p_{T}",               "#events"),          
  # Histogram("LowPtElectron_eta",                 "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "LowPtElectron #eta",                "#events"),          
  # Histogram("LowPtElectron_dxy",                 "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "LowPtElectron d_{xy}",              "#events"),          
  # Histogram("LowPtElectron_dz",                  "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "LowPtElectron d_{z}",               "#events"),          
  # Histogram("LowPtElectron_ip3d",                "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "LowPtElectron Muon |ip3D|",         "#events"),          
  # Histogram("LowPtElectron_sip3d",               "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "LowPtElectron Muon |ip3D| significance","#events"),
  # Histogram("LowPtElectron_normChi2",            "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "LowPtElectron #chi^{2}",            "#events"),                

  # Histogram("Event_nLowPtElectronExtended",          "",       True, NormalizationType.none,       1,    0,    10,       1e1,   1e6,   "Number of LowPtElectrons",              "#events"),             
  # Histogram("LowPtElectronExtended_dxyPV",           "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "LowPtElectron d_{xy}^{PV} [cm]",             "#events"),      
  # Histogram("LowPtElectronExtended_dxyPVErr",        "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "LowPtElectron d_{xy}^{PV} error",       "#events"),    
  # Histogram("LowPtElectronExtended_dzPV",            "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "LowPtElectron d_{z}^{PV} [cm]",              "#events"),      
  # Histogram("LowPtElectronExtended_dzPVErr",         "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "LowPtElectron d_{z}^{PV} error",        "#events"),    
  # Histogram("LowPtElectronExtended_dxyPVTraj",       "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "LowPtElectron trajectory d_{xy}^{PV} [cm]",  "#events"),      
  # Histogram("LowPtElectronExtended_dxyPVTrajErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron trajectory d_{xy}^{PV} error","#events"),      
  # Histogram("LowPtElectronExtended_dxyPVAbs",        "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron |d_{xy}^{PV}|",            "#events"),      
  # Histogram("LowPtElectronExtended_dxyPVAbsErr",     "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "LowPtElectron |d_{xy}^{PV}| error",      "#events"),      
  # Histogram("LowPtElectronExtended_dxyPVSigned",     "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "LowPtElectron signed d_{xy}^{PV} [cm]",       "#events"),      
  # Histogram("LowPtElectronExtended_dxyPVSignedErr",  "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron signed d_{xy}^{PV} error", "#events"),      
  # Histogram("LowPtElectronExtended_ip3DPVAbs",       "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron |ip3D|",                   "#events"),    
  # Histogram("LowPtElectronExtended_ip3DPVAbsErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron |ip3D| error",             "#events"),    
  # Histogram("LowPtElectronExtended_ip3DPVSigned",    "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "LowPtElectron signed ip3D",              "#events"),      
  # Histogram("LowPtElectronExtended_ip3DPVSignedErr", "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron signed ip3D error",        "#events"),      
  
  # Histogram("LowPtElectronExtended_dxyBS",           "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron d_{xy}^{BS}",             "#events"),      
  # Histogram("LowPtElectronExtended_dxyBSErr",        "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "LowPtElectron d_{xy}^{BS} error",       "#events"),    
  # Histogram("LowPtElectronExtended_dzBS",            "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron d_{z}^{BS}",              "#events"),      
  # Histogram("LowPtElectronExtended_dzBSErr",         "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "LowPtElectron d_{z}^{BS} error",        "#events"),    
  # Histogram("LowPtElectronExtended_dxyBSTraj",       "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron trajectory d_{xy}^{BS}",  "#events"),      
  # Histogram("LowPtElectronExtended_dxyBSTrajErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron trajectory d_{xy}^{BS} error","#events"),      
  # Histogram("LowPtElectronExtended_dxyBSAbs",        "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron |d_{xy}^{BS}|",            "#events"),      
  # Histogram("LowPtElectronExtended_dxyBSAbsErr",     "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "LowPtElectron |d_{xy}^{BS}| error",      "#events"),      
  # Histogram("LowPtElectronExtended_dxyBSSigned",     "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron signed d_{xy}^{BS}",       "#events"),      
  # Histogram("LowPtElectronExtended_dxyBSSignedErr",  "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron signed d_{xy}^{BS} error", "#events"),      
  # Histogram("LowPtElectronExtended_ip3DBSAbs",       "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron |ip3D|",                   "#events"),    
  # Histogram("LowPtElectronExtended_ip3DBSAbsErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron |ip3D| error",             "#events"),    
  # Histogram("LowPtElectronExtended_ip3DBSSigned",    "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "LowPtElectron signed ip3D",              "#events"),      
  # Histogram("LowPtElectronExtended_ip3DBSSignedErr", "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "LowPtElectron signed ip3D error",        "#events"),  

  Histogram("Event_nSV",                    "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Number of SV",       "#events"),             
  Histogram("SV_x",                   "",                     True, NormalizationType.none,       1,    0,    100,     1e1,   1e9,   "SV x",               "#events"),                
  Histogram("SV_y",                   "",                     True, NormalizationType.none,       1,    0,    100,     1e1,   1e9,   "SV y",               "#events"),                
  Histogram("SV_z",                   "",                     True, NormalizationType.none,       1,    0,    100,     1e1,   1e9,   "SV z",               "#events"),                
  Histogram("SV_chi2",                "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "SV #chi^{2}",        "#events"),                
  Histogram("SV_ndof",                "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "SV ndof",            "#events"),                
  
  # Histogram("nPV",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("PV_x",                 "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),              
  # Histogram("PV_y",                 "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),              
  # Histogram("PV_z",                 "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),              
  # Histogram("PV_chi2",              "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),              
  # Histogram("PV_ndof",              "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),              
  
  Histogram("Event_nBS",                    "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Number of BS",       "#events"),             
  Histogram("BS_x",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "BS x",               "#events"),                
  Histogram("BS_y",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "BS y",               "#events"),                
  Histogram("BS_z",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "BS z",               "#events"),                
  Histogram("BS_chi2",                "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "BS #chi^{2}",        "#events"),                
  Histogram("BS_ndof",                "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "BS ndof",            "#events"),                
  
  Histogram("Event_nMuonVertex",      "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Number of muon-muon vertices",     "#events"),             
  Histogram("MuonVertex_vxy",         "",                     True, NormalizationType.none,       1,    0,    200,      1e1,   1e9,   "Muon-muon vertex V_{xy}",          "#events"),                
  Histogram("MuonVertex_vxySigma",    "",                     True, NormalizationType.none,       1,    0,    200,      1e1,   1e9,   "Muon-muon vertex #sigma_{Vxy}",    "#events"),                
  Histogram("MuonVertex_vz",          "",                     True, NormalizationType.none,       1,    0,    200,      1e1,   1e9,   "Muon-muon vertex V_{z}",           "#events"),                
  Histogram("MuonVertex_chi2",        "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Muon-muon vertex #chi^{2}",        "#events"),                
  Histogram("MuonVertex_dR",          "",                     True, NormalizationType.none,       1,    0,    10,       1e1,   1e9,   "Muon-muon vertex dR",              "#events"),

  Histogram("Event_nMuonCombVertex",  "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Number of muon-DSAmuon vertices",  "#events"),             
  Histogram("MuonCombVertex_vxy",     "",                     True, NormalizationType.none,       1,    0,    200,      1e1,   1e9,   "Muon-DSAmuon vertex V_{xy}",       "#events"),                
  Histogram("MuonCombVertex_vxySigma","",                     True, NormalizationType.none,       1,    0,    200,      1e1,   1e9,   "Muon-DSAmuon vertex #sigma_{Vxy}", "#events"),                
  Histogram("MuonCombVertex_vz",      "",                     True, NormalizationType.none,       1,    0,    200,      1e1,   1e9,   "Muon-DSAmuon vertex V_{z}",        "#events"),                
  Histogram("MuonCombVertex_chi2",    "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Muon-DSAmuon vertex #chi^{2}",     "#events"),                
  Histogram("MuonCombVertex_dR",      "",                     True, NormalizationType.none,       1,    0,    10,       1e1,   1e9,   "Muon-DSAmuon vertex dR",           "#events"),

  Histogram("Event_nDSAMuonVertex",   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Number of DSAmuon-DSAmuon vertices",  "#events"),             
  Histogram("DSAMuonVertex_vxy",      "",                     True, NormalizationType.none,       1,    0,    200,      1e1,   1e9,   "DSAMuon-DSAmuon vertex V_{xy}",       "#events"),                
  Histogram("DSAMuonVertex_vxySigma", "",                     True, NormalizationType.none,       1,    0,    200,      1e1,   1e9,   "DSAMuon-DSAmuon vertex #sigma_{Vxy}", "#events"),                
  Histogram("DSAMuonVertex_vz",       "",                     True, NormalizationType.none,       1,    0,    200,      1e1,   1e9,   "DSAMuon-DSAmuon vertex V_{z}",        "#events"),                
  Histogram("DSAMuonVertex_chi2",     "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "DSAMuon-DSAmuon vertex #chi^{2}",     "#events"),                
  Histogram("DSAMuonVertex_dR",       "",                     True, NormalizationType.none,       1,    0,    10,       1e1,   1e9,   "DSAMuon-DSAmuon vertex dR",           "#events"),  
  
  # Histogram("nGenPart",               "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "Number of GenParts",          "#events"),             
  # Histogram("GenPart_pt",             "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "GenPart p_{T}",               "#events"),          
  # Histogram("GenPart_pdgid",          "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "GenPart PdgID",               "#events"),          
  # Histogram("GenPart_mass",           "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "GenPart mass",                "#events"),          
  # Histogram("GenPart_vx",             "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "GenPart v_{x}",               "#events"),
  # Histogram("GenPart_vy",             "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "GenPart v_{y}",               "#events"),
  # Histogram("GenPart_vz",             "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "GenPart v_{z}",               "#events"),
  # Histogram("GenPart_Rho",            "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "GenPart Rho",                 "#events"),  
  # Histogram("GenPart_R",              "",       True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "GenPart R",                   "#events"),  

  # Histogram("cutFlow", "cutflow",                                         True, NormalizationType.to_data, 1,   0, 8,     1e2, 1e10,     "Selection",        "Number of events"),
  # Histogram("norm_check", "Norm check",                                   True, NormalizationType.to_data, 1,  0, 1,      1e-2, 1e7,  "norm check",    "# events (2018)"),

  Histogram("nDSAMuonID",            "",                     True, NormalizationType.none,       1,    0,    10,       1e-1,   1e6,   "nDSAMuons after displaced di-muon selections", "#events"),
  Histogram("nDSAMuonIDPt5",        "",                     True, NormalizationType.none,       1,    0,    10,       1e-1,   1e6,   "nDSAMuons after displaced di-muon selections without pT cut", "#events"),
)

histograms2D = ()

weightsBranchName = "genWeight"

# data&signals must be listed after backgrounds for now
samples = (
  # Sample(
  #   name="tta_mAlp-0p35GeV_ctau-1e3mm",
  #   file_path=f"{basePath}/signal/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-100000_hist.root",
  #   type=SampleType.signal,
  #   cross_section=1,
  #   line_alpha=1,
  #   line_color=ROOT.kRed,
  #   fill_color=ROOT.kWhite,
  #   fill_alpha=0,
  #   marker_size=0,
  #   legend_description="signal m_{a} = 0.35 GeV",
  # ),
  Sample(
    name="tta_mAlp-0p35GeV_ctau-1e5mm",
    file_path=f"{basePath}/signal/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e5mm_nEvents-100000_hist.root",
    type=SampleType.signal,
    cross_section=1,
    line_alpha=1,
    line_color=ROOT.kBlue,
    fill_color=ROOT.kWhite,
    fill_alpha=0,
    marker_size=0,
    marker_style=0,
    legend_description="ctau = 1e5 mm",
  ),
  # Sample(
  #   name="tta_mAlp-0p35GeV_ctau-1e7mm",
  #   file_path=f"{basePath}/signal/tta_mAlp-0p35GeV_ctau-1e7mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e7mm_nEvents-100000_hist.root",
  #   type=SampleType.signal,
  #   cross_section=1,
  #   line_alpha=1,
  #   line_color=ROOT.kGreen,
  #   fill_color=ROOT.kWhite,
  #   fill_alpha=0,
  #   marker_size=0,
  #   legend_description="ctau = 1e7 mm",
  # ),

)

plotting_options = {
  SampleType.background: "hist",
  SampleType.signal: "nostack hist",
  SampleType.data: "nostack pe",
}

legend_width = 0.15
legend_min_x = 0.20
legend_max_x = 0.80

legend_height = 0.05
legend_max_y = 0.87


n_signal = len([s for s in samples if s.type == SampleType.signal and s.custom_legend is None])
n_data = len([s for s in samples if s.type == SampleType.data and s.custom_legend is None])
n_background = len([s for s in samples if s.type == SampleType.background and s.custom_legend is None])

# here default legends per sample type are defined. If you want to override them, specify custom_legend in the sample
legends = {
  SampleType.signal     : Legend(legend_min_x               , legend_max_y - n_signal*legend_height           , legend_min_x+legend_width , legend_max_y                        , "l" ),
}
