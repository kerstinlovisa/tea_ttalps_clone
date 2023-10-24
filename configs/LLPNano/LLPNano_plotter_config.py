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
  Histogram("Muon_dxy",                     "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon d_{xy}",                  "#events"),              
  Histogram("Muon_dz",                      "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon d_{z}",                   "#events"),              
  Histogram("Muon_ip3d",                    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |ip3D|",                  "#events"),              
  Histogram("Muon_sip3d",                   "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |ip3D| significance",     "#events"),              
  
  Histogram("Event_nMuonExtended",          "",       True, NormalizationType.none,       1,    0,    10,       1e1,   1e6,   "Number of muons",              "#events"),             
  Histogram("MuonExtended_dxyPV",           "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon d_{xy}^{PV}",             "#events"),      
  # Histogram("MuonExtended_dxyPVErr",        "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon d_{xy}^{PV} error",       "#events"),    
  Histogram("MuonExtended_dzPV",            "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon d_{z}^{PV}",              "#events"),      
  # Histogram("MuonExtended_dzPVErr",         "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon d_{z}^{PV} error",        "#events"),    
  Histogram("MuonExtended_dxyPVTraj",       "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon trajectory d_{xy}^{PV}",  "#events"),      
  Histogram("MuonExtended_dxyPVTrajErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon trajectory d_{xy}^{PV} error","#events"),      
  Histogram("MuonExtended_dxyPVAbs",        "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |d_{xy}^{PV}|",            "#events"),      
  Histogram("MuonExtended_dxyPVAbsErr",     "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon |d_{xy}^{PV}| error",      "#events"),      
  Histogram("MuonExtended_dxyPVSigned",     "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon signed d_{xy}^{PV}",       "#events"),      
  Histogram("MuonExtended_dxyPVSignedErr",  "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon signed d_{xy}^{PV} error", "#events"),      
  # Histogram("MuonExtended_ip3DPVAbs",       "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |ip3D|",                   "#events"),    
  # Histogram("MuonExtended_ip3DPVAbsErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |ip3D| error",             "#events"),    
  Histogram("MuonExtended_ip3DPVSigned",    "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon signed ip3D",              "#events"),      
  Histogram("MuonExtended_ip3DPVSignedErr", "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon signed ip3D error",        "#events"),      
  
  Histogram("MuonExtended_dxyBS",           "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon d_{xy}^{BS}",             "#events"),      
  # Histogram("MuonExtended_dxyBSErr",        "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon d_{xy}^{BS} error",       "#events"),    
  Histogram("MuonExtended_dzBS",            "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon d_{z}^{BS}",              "#events"),      
  # Histogram("MuonExtended_dzBSErr",         "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon d_{z}^{BS} error",        "#events"),    
  Histogram("MuonExtended_dxyBSTraj",       "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon trajectory d_{xy}^{BS}",  "#events"),      
  Histogram("MuonExtended_dxyBSTrajErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon trajectory d_{xy}^{BS} error","#events"),      
  Histogram("MuonExtended_dxyBSAbs",        "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |d_{xy}^{BS}|",            "#events"),      
  Histogram("MuonExtended_dxyBSAbsErr",     "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon |d_{xy}^{BS}| error",      "#events"),      
  Histogram("MuonExtended_dxyBSSigned",     "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon signed d_{xy}^{BS}",       "#events"),      
  Histogram("MuonExtended_dxyBSSignedErr",  "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon signed d_{xy}^{BS} error", "#events"),      
  # Histogram("MuonExtended_ip3DBSAbs",       "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |ip3D|",                   "#events"),    
  # Histogram("MuonExtended_ip3DBSAbsErr",    "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon |ip3D| error",             "#events"),    
  Histogram("MuonExtended_ip3DBSSigned",    "",       True, NormalizationType.none,       1,    -10,  10,       1e-2,  1e6,   "Muon signed ip3D",              "#events"),      
  Histogram("MuonExtended_ip3DBSSignedErr", "",       True, NormalizationType.none,       1,    0,    10,       1e-2,  1e6,   "Muon signed ip3D error",        "#events"),   

  # Histogram("Event_nDSAMuon",                "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),             
  # Histogram("DSAMuon_pt",                        "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_eta",                       "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyPV",                     "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyPVErr",                "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),         
  # Histogram("DSAMuon_dzPV",                      "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dzPVErr",                 "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),         
  # Histogram("DSAMuon_dxyPVTraj",                 "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyPVTrajErr",              "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyPVAbs",                  "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyPVAbsErr",               "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyPVSigned",               "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyPVSignedErr",            "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_ip3DPVAbs",               "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),         
  # Histogram("DSAMuon_ip3DPVAbsErr",            "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),         
  # Histogram("DSAMuon_ip3DPVSigned",              "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_ip3DPVSignedErr",           "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyBS",                     "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyBSErr",                "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),         
  # Histogram("DSAMuon_dzBS",                      "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dzBSErr",                 "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),         
  # Histogram("DSAMuon_dxyBSTraj",                 "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyBSTrajErr",              "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyBSAbs",                  "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyBSAbsErr",               "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyBSSigned",               "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_dxyBSSignedErr",            "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_ip3DBSAbs",               "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),         
  # Histogram("DSAMuon_ip3DBSAbsErr",            "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),         
  # Histogram("DSAMuon_ip3DBSSigned",              "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("DSAMuon_ip3DBSSignedErr",           "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           

  # Histogram("nElectron",               "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),             
  # Histogram("Electron_pt",                        "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),          
  # Histogram("Electron_eta",                       "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),          
  # Histogram("Electron_dxy",                       "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),          
  # Histogram("Electron_dz",                        "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),          
  # Histogram("Electron_ip3d",                      "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),          
  # Histogram("Electron_sip3d",                     "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),          

  # Histogram("nElectronExtended",       "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),             
  # Histogram("ElectronExtended_dxyPV",                             "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyPVErr",                        "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),
  # Histogram("ElectronExtended_dzPV",                              "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dzPVErr",                         "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),
  # Histogram("ElectronExtended_dxyPVTraj",                         "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyPVTrajErr",                      "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyPVAbs",                          "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyPVAbsErr",                       "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyPVSigned",                       "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyPVSignedErr",                    "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_ip3DPVAbs",                       "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),
  # Histogram("ElectronExtended_ip3DPVAbsErr",                    "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),
  # Histogram("ElectronExtended_ip3DPVSigned",                      "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_ip3DPVSignedErr",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyBS",                             "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyBSErr",                        "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),
  # Histogram("ElectronExtended_dzBS",                              "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dzBSErr",                         "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),
  # Histogram("ElectronExtended_dxyBSTraj",                         "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyBSTrajErr",                      "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyBSAbs",                          "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyBSAbsErr",                       "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyBSSigned",                       "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_dxyBSSignedErr",                    "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_ip3DBSAbs",                       "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),
  # Histogram("ElectronExtended_ip3DBSAbsErr",                    "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),
  # Histogram("ElectronExtended_ip3DBSSigned",                      "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("ElectronExtended_ip3DBSSignedErr",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),  
  # Histogram("nSV",                     "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),             
  # Histogram("SV_x",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),                
  # Histogram("SV_y",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),                
  # Histogram("SV_z",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),                
  # Histogram("SV_chi2",                "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),                
  # Histogram("SV_ndof",                "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),                
  # Histogram("nPV",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),           
  # Histogram("PV_x",                 "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),              
  # Histogram("PV_y",                 "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),              
  # Histogram("PV_z",                 "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),              
  # Histogram("PV_chi2",              "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),              
  # Histogram("PV_ndof",              "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),              
  # Histogram("nBS",                     "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),             
  # Histogram("BS_x",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),                
  # Histogram("BS_y",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),                
  # Histogram("BS_z",                   "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),                
  # Histogram("BS_chi2",                "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),                
  # Histogram("BS_ndof",                "",                     True, NormalizationType.none,       1,    0,    20,       1e1,   1e9,   "",       "#events"),                
  # 
  # 
  # Histogram("n_good_muons", "Number of good muons",                       True, NormalizationType.to_data, 1,   0, 20,    1e1, 1e9,   "Number of good muons",                    "# events (2018)"),
  # Histogram("n_almost_good_muons", "Number of almost good muons",         True, NormalizationType.to_data, 1,   0, 20,    1e1, 1e9,   "Number of almost good muons",                    "# events (2018)"),
  # Histogram("good_muon_pt", "Muon p_{T}",                                 True, NormalizationType.to_data, 10,   0, 500,   1e-2, 1e6,   "p_{T}^{#mu} [GeV]",                 "# events (2018)"),
  # Histogram("good_muon_leading_pt", "Leading muon p_{T}",                 True, NormalizationType.to_data, 10,   0, 500,   1e-2, 1e6,   "Leading p_{T}^{#mu} [GeV]",         "# events (2018)"),
  # Histogram("good_muon_subleading_pt", "All subleading muons p_{T}",      True, NormalizationType.to_data, 10,   0, 500,   1e-2, 1e6,   "All subleading p_{T}^{#mu} [GeV]",  "# events (2018)"),
  # Histogram("good_muon_eta","Muon #eta",                                  True, NormalizationType.to_data, 5,-3.5, 3.5,    1e0, 1e6,  "#eta^{#mu}",                         "# events (2018)"),
  # Histogram("good_muon_dxy","Muon d_{xy}",                                True, NormalizationType.to_data, 10,  -10, 10,   1e-2, 1e6,  "d_{xy}^{#mu}",                       "# events (2018)"),
  # Histogram("good_muon_dz", "Muon d_{z}",                                 True, NormalizationType.to_data, 10,  -10, 10,   1e-2, 1e6,  "d_{z}^{#mu}",                        "# events (2018)"),
  
  # Histogram("n_good_electrons",  "Number of electrons",                   True, NormalizationType.to_data, 1,   0, 10,    1e1, 1e9,   "Number of electrons", "# events (2018)"),
  # Histogram("good_electron_pt",  "Electron p_{T}",                        True, NormalizationType.to_data, 10,   0, 500,   1e-2, 1e6,   "p_{T}^{e} [GeV]",  "# events (2018)"),
  # Histogram("good_electron_leading_pt",  "Leading electron p_{T}",        True, NormalizationType.to_data, 10,   0, 500,   1e-2, 1e6,   "Leading p_{T}^{e} [GeV]",  "# events (2018)"),
  # Histogram("good_electron_subleading_pt","All subleading electron p_{T}",True, NormalizationType.to_data, 10,   0, 500,   1e-2, 1e6,   "All subleading p_{T}^{e} [GeV]",  "# events (2018)"),
  # Histogram("good_electron_eta", "Electron #eta",                         True, NormalizationType.to_data, 5, -3.5, 3.5, 1e-2,  1e6,  "#eta^{e}",         "# events (2018)"),
  # Histogram("good_electron_dxy", "Electron d_{xy}",                       True, NormalizationType.to_data, 10,   -10, 10,  1e-2, 1e6,  "d_{xy}^{e}",       "# events (2018)"),
  # Histogram("good_electron_dz",  "Electron d_{z}",                        True, NormalizationType.to_data, 10,   -10, 10,  1e-2, 1e6,  "d_{z}^{e}",        "# events (2018)"),
  
  # Histogram("n_good_jets",  "Number of jets",                             True, NormalizationType.to_data, 1,   0, 30,    1e0, 1e9,   "Number of jets",   "# events (2018)"),
  # Histogram("good_jet_pt",  "Jet p_{T}",                                  True, NormalizationType.to_data, 5,   0, 500,   10, 1e8,    "p_{T}^{j} [GeV]",  "# events (2018)"),
  # Histogram("good_jet_eta", "Jet #eta",                                   True, NormalizationType.to_data, 5, -3.5, 3.5, 1e0, 1e10,  "#eta^{j}",         "# events (2018)"),
  # Histogram("good_jet_btagDeepB", "Jet btagDeepB",                        True, NormalizationType.to_data, 2,  -1, 1,     1e0, 1e7,  "jet btagDeepB",    "# events (2018)"),
  
  # Histogram("n_good_bjets",  "Number of b-jets",                          True, NormalizationType.to_data, 1,   0, 30,    1e0, 1e9,   "Number of b-jets",   "# events (2018)"),
  # Histogram("good_bjet_pt",  "b-jet p_{T}",                               True, NormalizationType.to_data, 5,   0, 500,   10, 1e8,    "p_{T}^{j} [GeV]",  "# events (2018)"),
  # Histogram("good_bjet_eta", "b-jet #eta",                                True, NormalizationType.to_data, 5, -3.5, 3.5, 1e0, 1e10,  "#eta^{j}",         "# events (2018)"),
  # Histogram("good_bjet_btagDeepB", "b-jet btagDeepB",                     True, NormalizationType.to_data, 2,  -1, 1,     1e0, 1e7,  "b-jet btagDeepB",    "# events (2018)"),
  
  # Histogram("n_good_nonbjets",  "Number of non-b jets",                   True, NormalizationType.to_data, 1,   0, 30,    1e0, 1e9,   "Number of non-b jets",   "# events (2018)"),
  # Histogram("good_nonbjet_pt",  "non-b jet p_{T}",                        True, NormalizationType.to_data, 5,   0, 500,   10, 1e8,    "p_{T}^{j} [GeV]",  "# events (2018)"),
  # Histogram("good_nonbjet_eta", "non-b jet #eta",                         True, NormalizationType.to_data, 5, -3.5, 3.5, 1e0, 1e10,  "#eta^{j}",         "# events (2018)"),
  # Histogram("good_nonbjet_btagDeepB", "non-b jet btagDeepB",              True, NormalizationType.to_data, 2,  -1, 1,     1e0, 1e7,  "non-b jet btagDeepB",    "# events (2018)"),
  
  # Histogram("MET_pt", "MET p_{T}",                                        True, NormalizationType.to_data, 5,  0, 1000,     1e0, 1e5,  "MET p_{T} (GeV)",    "# events (2018)"),
  # Histogram("almost_good_dimuon_minv", "Dimuon Mass",                     True, NormalizationType.to_data, 1,  70, 110,     1e0, 1e6,  "m_{#mu#mu} (GeV)",    "# events (2018)"),
  # Histogram("dimuon_minv_closestToZ", "Dimuon Mass (Closest to Z mass)",  True, NormalizationType.to_data, 1,  70, 110,     1e0, 1e6,  "m_{#mu#mu} (GeV)",    "# events (2018)"),
  # Histogram("dimuon_deltaR_closestToZ", "#Delta R_{#mu#mu} (Closest to Z mass)", True, NormalizationType.to_data, 1,  -1, 6,     1e0, 1e5,  "#Delta R_{#mu#mu}",    "# events (2018)"),
  # Histogram("deltaPhi_lepton_MET", "#Delta #phi (MET, l)",                True, NormalizationType.to_data, 1,  -4, 4,     1e0, 1e5,  "#Delta #phi(MET, l)",    "# events (2018)"),
  # Histogram("minv_lepton_MET", "m_{MET, l}",                              True, NormalizationType.to_data, 2,  0, 500,     1e0, 1e6,  "m_{MET, l} (GeV)",    "# events (2018)"),
  # Histogram("minv_bjet_2jets", "m_(bjj)",                                 True, NormalizationType.to_data, 5,  0, 500,     1e0, 1e6,  "m_(bjj) (GeV)",    "# events (2018)"),
  
  # Histogram("cutFlow", "cutflow",                                         True, NormalizationType.to_data, 1,   0, 8,     1e2, 1e10,     "Selection",        "Number of events"),
  # Histogram("norm_check", "Norm check",                                   True, NormalizationType.to_data, 1,  0, 1,      1e-2, 1e7,  "norm check",    "# events (2018)"),
)

histograms2D = ()

weightsBranchName = "genWeight"

# data&signals must be listed after backgrounds for now
samples = (
  Sample(
    name="tta_mAlp-0p35GeV_ctau-1e3mm",
    file_path=f"{basePath}/signal/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e3mm_nEvents-100000_hist.root",
    type=SampleType.signal,
    cross_section=1,
    line_alpha=1,
    line_color=ROOT.kRed,
    fill_color=ROOT.kWhite,
    fill_alpha=0,
    marker_size=0,
    legend_description="ctau = 1e3 mm",
  ),
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
    legend_description="ctau = 1e5 mm",
  ),
  Sample(
    name="tta_mAlp-0p35GeV_ctau-1e7mm",
    file_path=f"{basePath}/signal/tta_mAlp-0p35GeV_ctau-1e7mm_nEvents-1000/histograms/tta_mAlp-0p35GeV_ctau-1e7mm_nEvents-100000_hist.root",
    type=SampleType.signal,
    cross_section=1,
    line_alpha=1,
    line_color=ROOT.kGreen,
    fill_color=ROOT.kWhite,
    fill_alpha=0,
    marker_size=0,
    legend_description="ctau = 1e7 mm",
  ),

)

plotting_options = {
  SampleType.background: "hist",
  SampleType.signal: "nostack",
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
