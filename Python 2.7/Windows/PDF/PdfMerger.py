import os
import pyPdf
import winshell
import wx
 
class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window
 
    def OnDropFiles(self, x, y, filenames):
        self.window.SetInsertionPointEnd()
 
        for file in filenames:
            self.window.WriteText(file)
 
########################################################################
class JoinerPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
 
        self.currentPath = winshell.desktop()
 
 
        lblSize = (70,-1)
        pdfLblOne = wx.StaticText(self, label="PDF One:", size=lblSize)
        self.pdfOne = wx.TextCtrl(self)
        dt = MyFileDropTarget(self.pdfOne)
        self.pdfOne.SetDropTarget(dt)
        pdfOneBtn = wx.Button(self, label="Browse", name="pdfOneBtn")
        pdfOneBtn.Bind(wx.EVT_BUTTON, self.onBrowse)
 
        pdfLblTwo = wx.StaticText(self, label="PDF Two:", size=lblSize)
        self.pdfTwo = wx.TextCtrl(self)
        dt = MyFileDropTarget(self.pdfTwo)
        self.pdfTwo.SetDropTarget(dt)
        pdfTwoBtn = wx.Button(self, label="Browse", name="pdfTwoBtn")
        pdfTwoBtn.Bind(wx.EVT_BUTTON, self.onBrowse)
 
        outputLbl = wx.StaticText(self, label="Output name:", size=lblSize)
        self.outputPdf = wx.TextCtrl(self)
        widgets = [(pdfLblOne, self.pdfOne, pdfOneBtn),
                   (pdfLblTwo, self.pdfTwo, pdfTwoBtn),
                   (outputLbl, self.outputPdf)]
 
        joinBtn = wx.Button(self, label="Join PDFs")
        joinBtn.Bind(wx.EVT_BUTTON, self.onJoinPdfs)
 
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        for widget in widgets:
            self.buildRows(widget)
        self.mainSizer.Add(joinBtn, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(self.mainSizer)
 
    #----------------------------------------------------------------------
    def buildRows(self, widgets):
        """"""
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        for widget in widgets:
            if isinstance(widget, wx.StaticText):
                sizer.Add(widget, 0, wx.ALL|wx.CENTER, 5)
            elif isinstance(widget, wx.TextCtrl):
                sizer.Add(widget, 1, wx.ALL|wx.EXPAND, 5)
            else:
                sizer.Add(widget, 0, wx.ALL, 5)
        self.mainSizer.Add(sizer, 0, wx.EXPAND)
 
    #----------------------------------------------------------------------
    def onBrowse(self, event):
        """
        Browse for PDFs
        """
        widget = event.GetEventObject()
        name = widget.GetName()
 
        wildcard = "PDF (*.pdf)|*.pdf"
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentPath, 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            if name == "pdfOneBtn":
                self.pdfOne.SetValue(path)
            else:
                self.pdfTwo.SetValue(path)
            self.currentPath = os.path.dirname(path)
        dlg.Destroy()
 
    #----------------------------------------------------------------------
    def onJoinPdfs(self, event):
        """
        Join the two PDFs together and save the result to the desktop
        """
        pdfOne = self.pdfOne.GetValue()
        pdfTwo = self.pdfTwo.GetValue()
        if not os.path.exists(pdfOne):
            msg = "The PDF at %s does not exist!" % pdfOne
            dlg = wx.MessageDialog(None, msg, 'Error', wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            return
        if not os.path.exists(pdfTwo):
            msg = "The PDF at %s does not exist!" % pdfTwo
            dlg = wx.MessageDialog(None, msg, 'Error', wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            return
 
        outputPath = os.path.join(winshell.desktop(), self.outputPdf.GetValue()) + ".pdf"
        output = pyPdf.PdfFileWriter()
 
        pdfOne = pyPdf.PdfFileReader(file(pdfOne, "rb"))
        for page in range(pdfOne.getNumPages()):
            output.addPage(pdfOne.getPage(page))
        pdfTwo = pyPdf.PdfFileReader(file(pdfTwo, "rb"))
        for page in range(pdfTwo.getNumPages()):
            output.addPage(pdfTwo.getPage(page))
 
        outputStream = file(outputPath, "wb")
        output.write(outputStream)
        outputStream.close()
 
        msg = "PDF was save to " + outputPath
        dlg = wx.MessageDialog(None, msg, 'PDF Created', wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
 
        self.pdfOne.SetValue("")
        self.pdfTwo.SetValue("")
        self.outputPdf.SetValue("")
 
########################################################################
class JoinerFrame(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "PDF Joiner", size=(550, 200))
        panel = JoinerPanel(self)
 
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = JoinerFrame()
    frame.Show()
    app.MainLoop()
