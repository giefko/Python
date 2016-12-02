import wx


########################################################################
class PanelOne(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        
        
        button2 =wx.Button(self, label="Panel 2", pos=(200, 325))
        button2.Bind(wx.EVT_BUTTON, parent.onSwitchPanels)
        button3 =wx.Button(self, label="Panel 3", pos=(600, 325))
        button3.Bind(wx.EVT_BUTTON, parent.onSwitchPanels3)
        button4 =wx.Button(self, label="Panel 4", pos=(1000, 325))
        button4.Bind(wx.EVT_BUTTON, parent.onSwitchPanels4)

########################################################################
class PanelTwo(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        

        button1 =wx.Button(self, label="Panel 1 ", pos=(200, 325))
        button1.Bind(wx.EVT_BUTTON, parent.onSwitchPanels2)
       


########################################################################
class PanelThree(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        
        button1 =wx.Button(self, label="Panel 1 ", pos=(200, 325))
        button1.Bind(wx.EVT_BUTTON, parent.onSwitchPanels2)
        

########################################################################
class PanelFour(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        

        button1 =wx.Button(self, label="Panel 1 ", pos=(200, 325))
        button1.Bind(wx.EVT_BUTTON, parent.onSwitchPanels2)
    

########################################################################
class MyForm(wx.Frame):
    
    
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "Panel Switcher Tutorial",
                          size=(800,600))

        self.panel_one = PanelOne(self)
        self.panel_two = PanelTwo(self)
        self.panel_three = PanelThree(self)
        self.panel_four = PanelFour(self)
       
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.sizer.Add(self.panel_three, 1, wx.EXPAND)
        self.sizer.Add(self.panel_four, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

       
    #----------------------------------------------------------------------
    def onSwitchPanels(self, event):

        if self.panel_one.IsShown():
           self.SetTitle("Panel Two Showing")
           self.panel_one.Hide()
           self.panel_two.Show()
           self.panel_three.Hide()
           self.panel_four.Hide()
        self.Layout()

      
           
    def onSwitchPanels2(self, event):

        if self.panel_two.IsShown() or self.panel_three.IsShown() or self.panel_four.IsShown():
           self.SetTitle("Panel One Showing")
           self.panel_one.Show()
           self.panel_two.Hide()
           self.panel_three.Hide()
           self.panel_four.Hide()
        self.Layout()

    def onSwitchPanels3(self, event):

        if self.panel_one.IsShown():
           self.SetTitle("Panel Three Showing")
           self.panel_one.Hide()
           self.panel_two.Hide()
           self.panel_three.Show()
           self.panel_four.Hide()
        self.Layout()

    def onSwitchPanels4(self, event):

        if self.panel_one.IsShown():
           self.SetTitle("Panel Four Showing")
           self.panel_one.Hide()
           self.panel_two.Hide()
           self.panel_three.Hide()
           self.panel_four.Show()
        self.Layout()

      
           
       

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
