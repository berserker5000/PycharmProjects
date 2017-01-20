__author__ = 'kud'
# coding: utf-8

import wx
from wx.lib import wordwrap

# when point on answer use wx.CURSOR_HAND

def monkey_q():
    question = "You see an angry monkey. What would you do?"


def monkey_a():
    answer = {1: "Give a banana to monkey.", 2: "Shut her down with pistol.", 3: "Kiss monkey.",
              4: "Sing a sleeping song for monkey."}

    for item in answer.values():
        return str(item)




class Monkey_Frame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, size=(500,500))
        box = wx.BoxSizer(wx.VERTICAL)
        gs = wx.GridSizer(3,2)

        self.label=wx.StaticText(self,5,"Some_text")
        self.btn1 = wx.Button(self, 1, "Give a bananasfgsgrgsd to monkey.")
        font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.label.SetFont(font)
        self.SetBackgroundColour(wx.Colour(255,255,0))
        self.label.Bind(wx.EVT_SIZE, self.__WrapText__)

        gs.Add(self.label)
        gs.Add(wx.StaticText(self, 0, ""))
        gs.Add(self.btn1)
        gs.Add(wx.Button(self, 2, "Give a banana to monkey."))
        gs.Add(wx.Button(self, 3, "Give a banana to monkey."))
        gs.Add(wx.Button(self, 4, "Give a banana to monkey."))

        box.Add(gs, 1, wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, id=1)
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, id=2)
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, id=3)
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, id=4)

        self.Centre()
        self.SetAutoLayout(True)
        self.SetSizer(box)
        self.Layout()

        # wx.Frame.__init__(self, parent, ID, title, pos, size=wx.SIZE_AUTO)
        # panel = wx.Panel(self, -1)
        # text=wx.StaticText(panel,-1,"You see an angry monkey. What would you do?", style=wx.ALIGN_CENTER)
        # font = wx.Font(18,wx.DEFAULT, wx.NORMAL, wx.BOLD)
        # text.SetFont(font)
        # text.Wrap(450)
        # panel.SetBackgroundColour(wx.Colour(255,255,0))
        #
        # button1 = wx.Button(panel, 100, "Give a banana to monkey.")
        # #button1.SetPosition(200,230)
        # button1.SetSizeHints(100, 100, 100, 100)
        # self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button1)
        #
        # self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
    def __WrapText__(self, event):
        self.label.Wrap(event.GetSize()[0])

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = Monkey_Frame(None, -1, "Logic Game")
    frame.Show()
    app.MainLoop()
