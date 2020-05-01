
import wx
import sys

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition)
        panel = wx.Panel(self, -1)

        self.Centre()

        panel.SetBackgroundColour("White")
        lbl=''' Please write you username and password'''
        wx.StaticText(panel,-1,lbl,(10,10),style=wx.LEFT)
        user="Username"
        wx.StaticText(panel, -1,user, (10, 55),style=wx.LEFT)
        self.username = wx.TextCtrl(panel, -1, '', (110, 55), (120, -1))
        pwd="Password"
        wx.StaticText(panel, -1,pwd, (10, 95),style=wx.LEFT)
        self.password = wx.TextCtrl(panel, -1, '', (110, 95), (120, -1),style=wx.TE_PASSWORD)
        cone="Login"
        con = wx.Button(panel, -1, cone, (70, 160),(130,-1))
        con.Bind(wx.EVT_BUTTON, self.OnSubmit)
        newus="Submit"
        newuser = wx.Button(panel, 1, newus, (70, 190),(130,-1))
        exitbtn="Exit"
        exitbutton = wx.Button(panel, 1, exitbtn, (70, 220),(130,-1))
        exitbutton.Bind(wx.EVT_BUTTON, self.OnFileExit)
        self.Centre()

   
    def OnFileExit(self, evt):
        a="Do you want to exit?"
      
        dlg = wx.MessageDialog(
            self, a, '',
            wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES: 
            dlg.Destroy() 
            self.Close(True) 
        else: 
            dlg.Destroy()

    def OnSubmit(self, event):
        user=self.username.GetValue()
        passwd= self.password.GetValue()
        
        emtpyuser=self.username.IsEmpty()
        emptypass=self.password.IsEmpty()

    

        if emtpyuser==True and emptypass==True:
            msg='''Please write your username and password '''
            
            
            dlg = wx.MessageDialog(
            self, msg, '',
            wx.OK | wx.ICON_ERROR)
            if dlg.ShowModal() == wx.ID_OK: 
                dlg.Destroy()
            
        
        if user=='username' and passwd=='123321':
            msg='''You have succesfully login'''
            
            dlg = wx.MessageDialog(
            self, msg, '',
            wx.OK | wx.ICON_INFORMATION)
            if dlg.ShowModal() == wx.ID_OK: 
                dlg.Destroy()
            else:
                self.errorlabel()
        else:
            self.errorlabel()

    def errorlabel(self):
        
          
        error="Please check your username and password"
        self.k=wx.StaticText(self, -1,error,(40,250))
        self.k.SetForegroundColour(wx.RED)
        self.k.SetBackgroundColour(wx.WHITE)
   
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'form1.py')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop()

