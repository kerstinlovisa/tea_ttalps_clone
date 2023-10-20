from ROOT import TObject
import ROOT

class Styler:
  
  def __init__(self, config):
    self.config = config
  
  def setup_ratio_pad(self, pad):
    pad.SetPad(0, 0, 1, 0.3)
    pad.SetLeftMargin(0.15)
    pad.SetTopMargin(0)
    pad.SetBottomMargin(0.3)
    pad.SetLogy(False)
    
  def setup_main_pad_with_ratio(self, pad):
    pad.SetPad(0, 0.3, 1, 1)
    pad.SetLeftMargin(0.15)
    pad.SetBottomMargin(0.0)
  
  def setup_main_pad_without_ratio(self, pad):
    pad.SetLeftMargin(0.15)
    pad.SetBottomMargin(0.15)
    pad.SetRightMargin(0.20)
  
  def setupFigure(self, plot, hist, is_ratio=False):
    if plot is None or type(plot) is TObject:
      return

    if is_ratio:
      plot.SetMinimum(0.7)
      plot.SetMaximum(1.3)
    else:
      if (hist.y_min > 0):
        plot.SetMinimum(hist.y_min)
      if (hist.y_max > 0):
        plot.SetMaximum(hist.y_max)
      
    try:
      plot.SetTitle("" if is_ratio else hist.title)
      plot.GetXaxis().SetLimits(hist.x_min, hist.x_max)
      
      plot.GetXaxis().SetTitle(hist.x_label)
      plot.GetXaxis().SetTitleSize(0.12 if is_ratio else 0.06)
      plot.GetXaxis().SetTitleOffset(1.0 if is_ratio else 1.0)
      
      plot.GetXaxis().SetLabelSize(0.1 if is_ratio else 0.06)
      
      plot.GetYaxis().SetTitle("Data/MC" if is_ratio else hist.y_label)
      plot.GetYaxis().SetTitleSize(0.1 if is_ratio else 0.05)
      plot.GetYaxis().SetTitleOffset(0.5 if is_ratio else 1.2)
      
      plot.GetYaxis().SetLabelSize(0.1 if is_ratio else 0.08)
      
      plot.GetYaxis().CenterTitle()
      plot.GetYaxis().SetNdivisions(505)
      
    except:
      print("Couldn't set axes limits")
      return
  
  def setupFigure2D(self, plot, hist):
    if plot is None or type(plot) is TObject:
      return

    if (hist.y_min > 0):
      plot.SetMinimum(hist.y_min)
    if (hist.y_max > 0):
      plot.SetMaximum(hist.y_max)
      
    if (hist.z_min > 0):
      plot.SetMinimum(hist.z_min)
    if (hist.z_max > 0):
      plot.SetMaximum(hist.z_max)
    
    try:
      plot.SetTitle(hist.title)
      plot.GetXaxis().SetRangeUser(hist.x_min, hist.x_max)
      plot.GetXaxis().SetTitle(hist.x_label)
      plot.GetXaxis().SetTitleSize(0.06)
      plot.GetXaxis().SetTitleOffset(1.0)
      plot.GetXaxis().SetLabelSize(0.06)
      
      plot.GetYaxis().SetRangeUser(hist.y_min, hist.y_max)
      plot.GetYaxis().SetTitle(hist.y_label)
      plot.GetYaxis().SetTitleSize(0.06)
      plot.GetYaxis().SetTitleOffset(1.2)
      plot.GetYaxis().CenterTitle()
      plot.GetYaxis().SetLabelSize(0.06)
      plot.GetYaxis().SetNdivisions(505)
      
      plot.GetZaxis().SetTitle(hist.z_label)
      plot.GetZaxis().SetTitleSize(0.06)
      plot.GetZaxis().SetTitleOffset(0.8)
      plot.GetZaxis().CenterTitle()
      plot.GetZaxis().SetLabelSize(0.06)
      plot.GetZaxis().SetNdivisions(505)

    except:
      print("Couldn't set axes limits")
      return
    
  def setupUncertaintyHistogram(self, hist):
    if hasattr(self.config, "background_uncertainty"):
      color = self.config.background_uncertainty_color
    else:
      color = ROOT.kBlack
    
    if hasattr(self.config, "background_uncertainty_alpha"):
      alpha = self.config.background_uncertainty_alpha
    else:
      alpha = 0.3
    
    if hasattr(self.config, "background_uncertainty_style"):
      style = self.config.background_uncertainty_style
    else:
      style = 3244
    
    hist.SetFillColorAlpha(color, alpha)
    hist.SetLineColor(color)
    hist.SetFillStyle(style)