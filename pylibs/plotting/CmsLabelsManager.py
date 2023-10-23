import ROOT
from ROOT import gPad, gStyle

# iPeriod = 1*(0/1 7 TeV) + 2*(0/1 8 TeV)  + 4*(0/1 13 TeV) 
# For instance: 
#               iPeriod = 3 means: 7 TeV + 8 TeV
#               iPeriod = 7 means: 7 TeV + 8 TeV + 13 TeV 
#               iPeriod = 0 means: free form (uses lumi_sqrtS)

class CmsLabelsManager:
  def __init__(self):
    self.setTDRStyle()
    
    self.cmsText     = "CMS"
    self.cmsTextFont   = 61  

    self.writeExtraText = True
    self.extraText   = "Preliminary"
    self.extraTextFont = 52 

    self.lumiTextSize     = 0.6
    self.lumiTextOffset   = 0.2

    self.cmsTextSize      = 0.75
    self.cmsTextOffset    = 0.1

    self.relPosX    = 0.045
    self.relPosY    = 0.035
    self.relExtraDY = 1.2

    self.extraOverCmsTextSize  = 0.76

    self.lumi_13TeV = "20.1 fb^{-1}"
    self.lumi_8TeV  = "19.7 fb^{-1}" 
    self.lumi_7TeV  = "5.1 fb^{-1}"
    self.lumi_sqrtS = ""

    self.drawLogo      = False
    self.outOfFrame = False

  def __getLumiText(self, iPeriod, iPosX):
    lumiText = ""
    if iPeriod==1:
      lumiText += self.lumi_7TeV
      lumiText += " (7 TeV)"
    elif iPeriod==2:
      lumiText += self.lumi_8TeV
      lumiText += " (8 TeV)"
    elif iPeriod==3:
      lumiText = self.lumi_8TeV 
      lumiText += " (8 TeV)"
      lumiText += " + "
      lumiText += self.lumi_7TeV
      lumiText += " (7 TeV)"
    elif iPeriod==4:
      lumiText += self.lumi_13TeV
      lumiText += " (13 TeV)"
    elif iPeriod==7:
      if self.outOfFrame:
        lumiText += "#scale[0.85]{"
      lumiText += self.lumi_13TeV 
      lumiText += " (13 TeV)"
      lumiText += " + "
      lumiText += self.lumi_8TeV 
      lumiText += " (8 TeV)"
      lumiText += " + "
      lumiText += self.lumi_7TeV
      lumiText += " (7 TeV)"
      if self.outOfFrame: 
        lumiText += "}"
    elif iPeriod==12:
      lumiText += "8 TeV"
    elif iPeriod==0:
      lumiText += self.lumi_sqrtS
    return lumiText
  
  def CMS_lumi(self, pad, iPeriod, iPosX ):
    if iPosX==0:
      self.relPosX = 0.12
    
    if iPosX/10==0: 
      self.outOfFrame = True

    alignY_=3
    alignX_=2
    if( iPosX/10==0 ): alignX_=1
    if( iPosX==0    ): alignY_=1
    if( iPosX/10==1 ): alignX_=1
    if( iPosX/10==2 ): alignX_=2
    if( iPosX/10==3 ): alignX_=3
    align_ = 10*alignX_ + alignY_

    H = pad.GetWh()
    W = pad.GetWw()
    l = pad.GetLeftMargin()
    t = pad.GetTopMargin()
    r = pad.GetRightMargin()
    b = pad.GetBottomMargin()
    
    pad.cd()
    lumiText = self.__getLumiText(iPeriod, iPosX)
    
    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAngle(0)
    latex.SetTextColor(ROOT.kBlack)    
    latex.SetTextFont(42)
    latex.SetTextAlign(31) 
    latex.SetTextSize(self.lumiTextSize*t)
    latex.DrawLatex(1-r,1-t+self.lumiTextOffset * t, lumiText)

    if self.outOfFrame:
      latex.SetTextFont(self.cmsTextFont)
      latex.SetTextAlign(11) 
      latex.SetTextSize(self.cmsTextSize*t)    
      latex.DrawLatex(l,1-t+self.lumiTextOffset*t, self.cmsText)
  
    pad.cd()

    posX_ = 0
    if iPosX%10 <= 1:
        posX_ = l + self.relPosX*(1-l-r)
    elif iPosX%10==2:
        posX_ =  l + 0.5*(1-l-r)
    elif iPosX%10==3:
        posX_ = 1-r - self.relPosX*(1-l-r)

    posY_ = 1-t - self.relPosY*(1-t-b)

    extraTextSize = self.extraOverCmsTextSize * self.cmsTextSize

    if not self.outOfFrame:
      if self.drawLogo:
        posX_ =   l + 0.045*(1-l-r)*W/H
        posY_ = 1-t - 0.045*(1-t-b)
        xl_0 = posX_
        yl_0 = posY_ - 0.15
        xl_1 = posX_ + 0.15*H/W
        yl_1 = posY_
        CMS_logo = ROOT.TASImage("CMS-BW-label.png")
        pad_logo =  ROOT.TPad("logo","logo", xl_0, yl_0, xl_1, yl_1 )
        pad_logo.Draw()
        pad_logo.cd()
        CMS_logo.Draw("X")
        pad_logo.Modified()
        pad.cd()
      else:
          latex.SetTextFont(self.cmsTextFont)
          latex.SetTextSize(self.cmsTextSize*t)
          latex.SetTextAlign(align_)
          latex.DrawLatex(posX_, posY_, self.cmsText)
          if self.writeExtraText:
            latex.SetTextFont(self.extraTextFont)
            latex.SetTextAlign(align_)
            latex.SetTextSize(extraTextSize*t)
            latex.DrawLatex(posX_, posY_- self.relExtraDY*self.cmsTextSize*t, self.extraText)
    elif self.writeExtraText:
      if iPosX==0:
          posX_ = l +  self.relPosX*(1-l-r)
          posY_ = 1-t + self.lumiTextOffset*t

      latex.SetTextFont(self.extraTextFont)
      latex.SetTextSize(extraTextSize*t)
      latex.SetTextAlign(align_)
      latex.DrawLatex(posX_, posY_, self.extraText)      

    pad.Update()

  def setTDRStyle(self):
    # tdrStyle =  ROOT.TStyle("tdrStyle", "Style for P-TDR")

    #for the canvas:
    gStyle.SetCanvasBorderMode(0)
    gStyle.SetCanvasColor(ROOT.kWhite)
    gStyle.SetCanvasDefH(600) #Height of canvas
    gStyle.SetCanvasDefW(600) #Width of canvas
    gStyle.SetCanvasDefX(0)   #POsition on screen
    gStyle.SetCanvasDefY(0)


    gStyle.SetPadBorderMode(0)
    #gStyle.SetPadBorderSize(Width_t size = 1)
    gStyle.SetPadColor(ROOT.kWhite)
    gStyle.SetPadGridX(False)
    gStyle.SetPadGridY(False)
    gStyle.SetGridColor(0)
    gStyle.SetGridStyle(3)
    gStyle.SetGridWidth(1)

  #For the frame:
    gStyle.SetFrameBorderMode(0)
    gStyle.SetFrameBorderSize(1)
    gStyle.SetFrameFillColor(0)
    gStyle.SetFrameFillStyle(0)
    gStyle.SetFrameLineColor(1)
    gStyle.SetFrameLineStyle(1)
    gStyle.SetFrameLineWidth(1)
    
  #For the histo:
    #gStyle.SetHistFillColor(1)
    #gStyle.SetHistFillStyle(0)
    gStyle.SetHistLineColor(1)
    gStyle.SetHistLineStyle(0)
    gStyle.SetHistLineWidth(1)
    #gStyle.SetLegoInnerR(Float_t rad = 0.5)
    #gStyle.SetNumberContours(Int_t number = 20)

    gStyle.SetEndErrorSize(2)
    #gStyle.SetErrorMarker(20)
    #gStyle.SetErrorX(0.)
    
    gStyle.SetMarkerStyle(20)
    
  #For the fit/function:
    gStyle.SetOptFit(1)
    gStyle.SetFitFormat("5.4g")
    gStyle.SetFuncColor(2)
    gStyle.SetFuncStyle(1)
    gStyle.SetFuncWidth(1)

  #For the date:
    gStyle.SetOptDate(0)
    # gStyle.SetDateX(Float_t x = 0.01)
    # gStyle.SetDateY(Float_t y = 0.01)

  # For the statistics box:
    gStyle.SetOptFile(0)
    gStyle.SetOptStat(0) # To display the mean and RMS:   SetOptStat("mr")
    gStyle.SetStatColor(ROOT.kWhite)
    gStyle.SetStatFont(42)
    gStyle.SetStatFontSize(0.025)
    gStyle.SetStatTextColor(1)
    gStyle.SetStatFormat("6.4g")
    gStyle.SetStatBorderSize(1)
    gStyle.SetStatH(0.1)
    gStyle.SetStatW(0.15)
    # gStyle.SetStatStyle(Style_t style = 1001)
    # gStyle.SetStatX(Float_t x = 0)
    # gStyle.SetStatY(Float_t y = 0)

  # Margins:
    gStyle.SetPadTopMargin(0.05)
    gStyle.SetPadBottomMargin(0.13)
    gStyle.SetPadLeftMargin(0.16)
    gStyle.SetPadRightMargin(0.02)

  # For the Global title:

    gStyle.SetOptTitle(0)
    gStyle.SetTitleFont(42)
    gStyle.SetTitleColor(1)
    gStyle.SetTitleTextColor(1)
    gStyle.SetTitleFillColor(10)
    gStyle.SetTitleFontSize(0.05)
    # gStyle.SetTitleH(0) # Set the height of the title box
    # gStyle.SetTitleW(0) # Set the width of the title box
    # gStyle.SetTitleX(0) # Set the position of the title box
    # gStyle.SetTitleY(0.985) # Set the position of the title box
    # gStyle.SetTitleStyle(Style_t style = 1001)
    # gStyle.SetTitleBorderSize(2)

  # For the axis titles:

    gStyle.SetTitleColor(1, "XYZ")
    gStyle.SetTitleFont(42, "XYZ")
    gStyle.SetTitleSize(0.06, "XYZ")
    # gStyle.SetTitleXSize(Float_t size = 0.02) # Another way to set the size?
    # gStyle.SetTitleYSize(Float_t size = 0.02)
    gStyle.SetTitleXOffset(0.9)
    gStyle.SetTitleYOffset(1.25)
    # gStyle.SetTitleOffset(1.1, "Y") # Another way to set the Offset

  # For the axis labels:

    gStyle.SetLabelColor(1, "XYZ")
    gStyle.SetLabelFont(42, "XYZ")
    gStyle.SetLabelOffset(0.007, "XYZ")
    gStyle.SetLabelSize(0.05, "XYZ")

  # For the axis:

    gStyle.SetAxisColor(1, "XYZ")
    gStyle.SetStripDecimals(True)
    gStyle.SetTickLength(0.03, "XYZ")
    gStyle.SetNdivisions(510, "XYZ")
    gStyle.SetPadTickX(1)  # To get tick marks on the opposite side of the frame
    gStyle.SetPadTickY(1)

  # Change for log plots:
    gStyle.SetOptLogx(0)
    gStyle.SetOptLogy(0)
    gStyle.SetOptLogz(0)

  # Postscript options:
    gStyle.SetPaperSize(20.,20.)
    # gStyle.SetLineScalePS(Float_t scale = 3)
    # gStyle.SetLineStyleString(Int_t i, const char* text)
    # gStyle.SetHeaderPS(const char* header)
    # gStyle.SetTitlePS(const char* pstitle)

    # gStyle.SetBarOffset(Float_t baroff = 0.5)
    # gStyle.SetBarWidth(Float_t barwidth = 0.5)
    # gStyle.SetPaintTextFormat(const char* format = "g")
    # gStyle.SetPalette(Int_t ncolors = 0, Int_t* colors = 0)
    # gStyle.SetTimeOffset(Double_t toffset)
    # gStyle.SetHistMinimumZero(kTRUE)

    # gStyle.SetHatchesLineWidth(5)
  #   gStyle.SetHatchesSpacing(0.05)

    # tdrStyle.cd()