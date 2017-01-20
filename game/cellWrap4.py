import wx
import wx.grid
from wx.lib import wordwrap
from wx.lib.mixins.grid import GridAutoEditMixin 

# from http://stackoverflow.com/questions/5868280/auto-wrap-and-newlines-in-wxpython-grid
# ---------------------------------------------------------------------------------------
class CustomGridCellAutoWrapStringRenderer(wx.grid.PyGridCellRenderer):   
    def __init__(self): 
        wx.grid.PyGridCellRenderer.__init__(self)

    def Draw(self, grid, attr, dc, rect, row, col, isSelected):
        text = grid.GetCellValue(row, col)
        dc.SetFont( attr.GetFont() ) 
        text = wordwrap.wordwrap(text, grid.GetColSize(col), dc, breakLongWords = False)
        hAlign, vAlign = attr.GetAlignment()       
        if isSelected: 
            bg = grid.GetSelectionBackground() 
            fg = grid.GetSelectionForeground() 
        else: 
            bg = attr.GetBackgroundColour()
            fg = attr.GetTextColour() 
        dc.SetTextBackground(bg) 
        dc.SetTextForeground(fg)
        dc.SetBrush(wx.Brush(bg, wx.SOLID))
        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawRectangleRect(rect)            
        grid.DrawTextRectangle(dc, text, rect, hAlign, vAlign)

    def GetBestSize(self, grid, attr, dc, row, col): 
        text = grid.GetCellValue(row, col)
        dc.SetFont(attr.GetFont())
        text = wordwrap.wordwrap(text, grid.GetColSize(col), dc, breakLongWords = False)
        w, h, lineHeight = dc.GetMultiLineTextExtent(text)                   
        return wx.Size(w, h)        

    def Clone(self): 
        return CutomGridCellAutoWrapStringRenderer()

class MyGrid (wx.grid.Grid, GridAutoEditMixin ):
    def __init__ (self, parent, size):
        wx.grid.Grid.__init__(self, parent,size=size)
        GridAutoEditMixin.__init__(self)
        

class MyFrame(wx.Frame):
    def __init__(self, parent = None, id = -1, title = "My Test"):
        wx.Frame.__init__(self, parent, id, title, size=((350,300)) )

        panel = wx.Panel(self)

        button1 = wx.Button(panel, id=-1, label='Button1', pos=( 10, 220))
        button2 = wx.Button(panel, id=-1, label='Button2', pos=(110, 220))
        button3 = wx.Button(panel, id=-1, label='Button3', pos=(210, 220))

        grid = MyGrid (panel, size=(350, 200))
        #grid = wx.grid.Grid(panel, size=(350, 200))
        grid.CreateGrid(3, 3)

        grid.SetDefaultRenderer(CustomGridCellAutoWrapStringRenderer()) #use custom renderer

        grid.SetRowSize(0, 50)
        grid.SetRowSize(1, 50)
        grid.SetRowSize(2, 50)

        attr = self.setCellAttrib2()
        for i in range (grid.GetNumberRows()):
            grid.SetAttr(i, 0, attr)     
            grid.SetAttr(i, 1, attr)     
            grid.SetAttr(i, 2, attr) 
        grid.SetRowMinimalAcceptableHeight (50)

        grid.SetCellValue(0, 0, "1\n2\n3\non sep lines?")
        grid.SetCellValue(0, 1, "Press Enter\nfor a new line?")
        grid.AutoSizeRows(setAsMin = True)
        
        self.grid = grid
                    
        self.Center()
        self.Show()    

        grid.Bind(wx.grid.EVT_GRID_EDITOR_CREATED, self.OnEditorCreated)
        grid.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.OnSelectCell)   
        
        
    def setCellAttrib2(self):
        attr = wx.grid.GridCellAttr()
        attr.SetFont(wx.Font(8, wx.ROMAN, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        attr.SetAlignment(wx.ALIGN_LEFT, wx.ALIGN_LEFT)   
        attr.SetEditor(wx.grid.GridCellAutoWrapStringEditor())    
        #attr.SetRenderer(wx.grid.GridCellAutoWrapStringRenderer())  #Use CustomGridCellAutoWrapStringRenderer
        attr.IncRef()
        return attr
        
        
    def OnSelectCell(self, event):
        self.row = event.GetRow()
        self.col = event.GetCol() 
        #print "Selected R/C** 1", self.row, self.col
        #print self.grid.GetCellValue(self.row, self.col)
#        self.grid.AutoSizeRow(self.row, setAsMin = True) 

        # Enable This line to autosize newly entered text
        #------------------------------------------------
        self.grid.AutoSizeRows(setAsMin = True)
        event.Skip()   



# from https://groups.google.com/forum/?hl=en&fromgroups=#!searchin/wxpython-users/
#                        newline$20wx.grid/wxpython-users/bMiG-jN03k4/uf4svkiAlJ0J
# ---------------------------------------------------------------------------------
    def OnEditorCreated(self, event):
        def HandleKey(event):
            #print self.row,self.col, 'Key=',event.KeyCode
            if event.KeyCode == wx.WXK_RETURN:
                event.GetEventObject().WriteText('\n')
                #print "GOT IT"
            else:
                event.Skip()

        # Since the grid pushes a new wx.EvtHandler onto the control's
        # event handler stack, Bind to the first event handler on the
        # stack instead of directly to the control so we can get first
        # crack at the event.
        ctrlEH = event.GetControl().GetEventHandler()
        ctrlEH.Bind(wx.EVT_KEY_DOWN, HandleKey)
    


def main():
    app = wx.App()
    MyFrame()
    app.MainLoop()


if __name__ == "__main__":
    main()
