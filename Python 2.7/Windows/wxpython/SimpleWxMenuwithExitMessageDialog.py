import wx

ID_FILE_OPEN = wx.NewId() 
ID_FILE_CLOSE =  wx.NewId() 
ID_FILE_EXIT =  wx.NewId() 
ID_HELP_ABOUT =  wx.NewId()

class MyFrame(wx.Frame): 

    def __init__(self, parent, id, title): 

        wx.Frame.__init__(self, parent, id, title) 
 
        filemenu =  wx.Menu()
        filemenu. Append(ID_FILE_OPEN, 'Open File') 
        filemenu. Append(ID_FILE_CLOSE, 'Close File') 
        filemenu. AppendSeparator() 
        filemenu. Append(ID_FILE_EXIT, 'Exit Program') 
 
        helpmenu =  wx.Menu() 
        helpmenu. Append(ID_HELP_ABOUT, 'About') 
 
        menubar =  wx.MenuBar() 
 
        menubar. Append(filemenu, 'File') 
        menubar. Append(helpmenu, 'Help') 
 
        self.SetMenuBar(menubar) 
 
        wx.EVT_MENU(self, ID_FILE_OPEN, self.ToDo) 
        wx.EVT_MENU(self, ID_FILE_CLOSE, self.ToDo) 
        wx.EVT_MENU(self, ID_FILE_EXIT, self.OnFileExit) 
        wx.EVT_MENU(self, ID_HELP_ABOUT, self.ToDo) 
 
    def OnFileExit(self, evt): 
        dlg = wx.MessageDialog(
            self, 
            'Exit Program?', 
            'I Need To Know!', 
            wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES: 
            dlg.Destroy() 
            self.Close(True) 
        else: 
            dlg.Destroy() 
 
    def ToDo(self, evt): 
        dlg = wx.MessageDialog(
            self, 
            'Not Yet Implimented!', 
            'ToDo', 
            wx.OK | wx.ICON_INFORMATION) 
        dlg.ShowModal() 
        dlg.Destroy() 
 
class MyMenuApp(wx.App): 
    def OnInit(self): 
        frame = MyFrame(None , -1, 'Menu Demo') 
        frame.Show(True) 
        self.SetTopWindow(frame) 
        return True 
 
# Run program
app=MyMenuApp() 
app.MainLoop()
