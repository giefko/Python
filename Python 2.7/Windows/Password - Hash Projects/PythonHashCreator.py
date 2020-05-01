import wx
import hashlib,binascii
import sys
 
if "2.8" in wx.version():
    import wx.lib.pubsub.setupkwargs
    from wx.lib.pubsub import pub
else:
    from wx.lib.pubsub import pub
 
 
########################################################################
class CreateHash(wx.Dialog):
    """
    Class to define login dialog
    """
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Hash creator")
 
 
        
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)
 
        p_lbl = wx.StaticText(self, label="Password:")
        p_sizer.Add(p_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.password = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        p_sizer.Add(self.password, 0, wx.ALL, 5)
 
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(p_sizer, 0, wx.ALL, 5)
 
        btn = wx.Button(self, label="Create")
        btn.Bind(wx.EVT_BUTTON, self.onCreate)
        main_sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        clearbtn = wx.Button(self,label="Clear")
        clearbtn.Bind(wx.EVT_BUTTON, self.onClear)
        main_sizer.Add(clearbtn, 0, wx.ALL|wx.CENTER, 5)

        
        exitbtn = wx.Button(self,label="Exit")
        exitbtn.Bind(wx.EVT_BUTTON, self.OnFileExit)
        main_sizer.Add(exitbtn, 0, wx.ALL|wx.CENTER, 5)

        textarea = wx.TextCtrl(self,
                                style=wx.TE_MULTILINE|wx.BORDER_SUNKEN|wx.TE_READONLY|
                                wx.TE_RICH2, size=(300,100))
        main_sizer.Add(textarea, 0, wx.ALL|wx.CENTER, 5)
        self.usertext = textarea
 
        self.SetSizer(main_sizer)
 
    #----------------------------------------------------------------------
    def onCreate(self, event):
        
        
        user_password = self.password.GetValue()
        m = hashlib.md5(user_password )
        m2=hashlib.sha512(m.hexdigest())
        self.usertext.AppendText( m2.hexdigest())
        
        
     
        
    #----------------------------------------------------------------------
    def onClear(self, event):
        
        
        
        self.usertext.Clear()
        self.password.Clear()
        
        
     
        

    #----------------------------------------------------------------------

    def OnFileExit(self, evt):

        extmsg="Do you want to exit?"
        
        dlg = wx.MessageDialog(
        self, extmsg, '',
        wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES: 
            dlg.Destroy() 
            self.Close(True)
            sys.exit(True)
        else: 
            dlg.Destroy()
        
        
 
########################################################################
class MyPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
 
 
########################################################################
class MainFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Main App")
        panel = MyPanel(self)
        pub.subscribe(self.myListener, "frameListener")
 
        # Ask user to login
        dlg = CreateHash()
        dlg.ShowModal()
 
    #----------------------------------------------------------------------
    def myListener(self, message, arg2=None):
        """
        Show the frame
        """
        self.Show()
 
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
