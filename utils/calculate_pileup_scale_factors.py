import ROOT
from ROOT import gPad, gStyle, TCanvas, TFile, TLegend
import os

def main():
  gStyle.SetOptStat(0)
  
  base_path = "/nfs/dust/cms/user/jniedzie/ttalps_cms"
  data_file_path = f"{base_path}/collision_data2018/SingleMuon2018__histograms_pileup.root"
  background_file_paths = {
    "tt (semi-leptonic)": f"{base_path}/backgrounds2018/TTToSemiLeptonic/histograms_pileup/histograms.root",
    "ST_tW_antitop": f"{base_path}/backgrounds2018/ST_tW_antitop/histograms_pileup/histograms.root",
    "ST_t-channel_antitop": f"{base_path}/backgrounds2018/ST_t-channel_antitop/histograms_pileup/histograms.root",
    # "DYJetsToMuMu_M-10to50": f"{base_path}/backgrounds2018/DYJetsToMuMu_M-10to50/histograms_pileup/histograms.root",
    "WJetsToLNu": f"{base_path}/backgrounds2018/WJetsToLNu/histograms_pileup/histograms.root",
    "TTZToLLNuNu": f"{base_path}/backgrounds2018/TTZToLLNuNu/histograms_pileup/histograms.root",
    "TTWJetsToLNu": f"{base_path}/backgrounds2018/TTWJetsToLNu/histograms_pileup/histograms.root",
    "ttHTobb": f"{base_path}/backgrounds2018/ttHTobb/histograms_pileup/histograms.root",
    "ttHToNonbb": f"{base_path}/backgrounds2018/ttHToNonbb/histograms_pileup/histograms.root",
    "TTZZ": f"{base_path}/backgrounds2018/TTZZ/histograms_pileup/histograms.root",
    "TTZH": f"{base_path}/backgrounds2018/TTZH/histograms_pileup/histograms.root",
  }

  data_file = TFile(data_file_path, "READ")
  data_hist = data_file.Get("Event_PV_npvsGood")
  data_hist.Sumw2()
  data_hist.Scale(1.0 / data_hist.Integral())
  data_hist.SetLineColor(ROOT.kBlack)
  
  canvas = TCanvas("canvas", "canvas", 800, 600)
  canvas.Divide(1, 2)

  canvas.cd(1)
  gPad.SetBottomMargin(0.0)
  gPad.SetLogy()
  data_hist.Draw("hist")
  
  data_hist.GetXaxis().SetRangeUser(0, 150)
  data_hist.GetXaxis().SetTitle("Number of good vertices")
  data_hist.GetXaxis().SetTitleSize(0.05)
  data_hist.GetXaxis().SetTitleOffset(0.9)
  
  data_hist.GetYaxis().SetTitle("Number of entries")
  data_hist.GetYaxis().SetTitleSize(0.05)
  data_hist.GetYaxis().SetTitleOffset(0.9)
  
  data_hist.SetTitle("")

  legend = TLegend(0.7, 0.3, 0.9, 0.9)
  legend.AddEntry(data_hist, "Data", "l")

  colors = (ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kMagenta, ROOT.kCyan, ROOT.kOrange, ROOT.kYellow, ROOT.kGray, ROOT.kOrange, ROOT.kViolet, ROOT.kCyan+2)

  background_files = []
  background_hists = []
  ratio_hists = []

  for i, (background_name, background_file_path) in enumerate(background_file_paths.items()):
    background_files.append(TFile(background_file_path, "READ"))
    background_hists.append(background_files[-1].Get("Event_PV_npvsGood"))
    
    background_hists[-1].Sumw2()
    background_hists[-1].Scale(1.0 / background_hists[-1].Integral())
    background_hists[-1].SetLineColor(colors[i])
  
    canvas.cd(1)
    background_hists[-1].Draw("same")
    legend.AddEntry(background_hists[-1], background_name, "l")
    
    canvas.cd(2)
    gPad.SetLogy()
    ratio_hists.append(data_hist.Clone())
    ratio_hists[-1].SetLineColor(colors[i])
    ratio_hists[-1].Divide(background_hists[-1])
    ratio_hists[-1].Draw("" if i==0 else "same")
    
    if i == 0:
      gPad.SetTopMargin(0.0)
      ratio_hists[-1].GetXaxis().SetTitle("Number of good vertices")
      ratio_hists[-1].GetXaxis().SetTitleSize(0.05)
      ratio_hists[-1].GetXaxis().SetTitleOffset(0.9)
      
      ratio_hists[-1].GetYaxis().SetRangeUser(1e-1, 1e3)
      ratio_hists[-1].GetYaxis().SetTitle("Scale factor")
      ratio_hists[-1].GetYaxis().SetTitleSize(0.05)
      ratio_hists[-1].GetYaxis().SetTitleOffset(0.9)
  
  backgrounds_sum_hist = background_hists[0].Clone()
  backgrounds_sum_hist.Sumw2()
  
  for background_hist in background_hists[1:]:
    backgrounds_sum_hist.Add(background_hist)
    
  backgrounds_sum_hist.Scale(1.0 / backgrounds_sum_hist.Integral())
  
  ratio_sum_hist = data_hist.Clone()
  ratio_sum_hist.Divide(backgrounds_sum_hist)
  ratio_sum_hist.SetLineColor(ROOT.kBlack)
  ratio_sum_hist.SetLineWidth(2)
  ratio_sum_hist.Draw("same")
  
  canvas.cd(1)
  legend.Draw()
  
  canvas.Update()
  canvas.SaveAs("pileup.pdf")
  
  # create output directory if it doesn't exist
  os.system("mkdir -p ../data/pileup")
  ratio_sum_hist.SetName("pileup_scale_factors")
  ratio_sum_hist.SaveAs("../data/pileup/pileup_scale_factors.root")
  
if __name__ == '__main__':
  main()