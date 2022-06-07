# -*- coding: utf-8 -*- 
import wx
import wx.xrc
import wx.grid
import numpy as np
import wx.lib.plot as wxPyPlot

###########################################################################
## Class NumPanel
###########################################################################
class NumPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.TAB_TRAVERSAL )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.gridNum = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.gridNum.CreateGrid( 500, 4 )
		self.gridNum.EnableEditing( True )
		self.gridNum.EnableGridLines( True )
		self.gridNum.EnableDragGridSize( False )
		self.gridNum.SetMargins( 0, 0 )
		
		# Columns
		self.gridNum.EnableDragColMove( False )
		self.gridNum.EnableDragColSize( True )
		self.gridNum.SetColLabelSize( 30 )
		self.gridNum.SetColLabelValue( 0, u"values" )
		self.gridNum.SetColLabelValue( 1, u"x" )
		self.gridNum.SetColLabelValue( 2, u"y" )
		self.gridNum.SetColLabelValue( 3, u"z" )
		self.gridNum.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gridNum.EnableDragRowSize( True )
		self.gridNum.SetRowLabelSize( 70 )
		self.gridNum.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.gridNum.SetDefaultCellAlignment( wx.ALIGN_RIGHT, wx.ALIGN_TOP )
		bSizer.Add( self.gridNum, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
	
	def __del__( self ):
		pass


###########################################################################
## Class FigPanel
###########################################################################
class FigPanel(wx.Frame):
	def __init__(self, parent=None, id=wx.ID_ANY, title="SV solutions"):
		wx.Frame.__init__(self, parent, id, title,size=(600, 400))
		self.pc = wxPyPlot.PlotCanvas(self)     # 此处导入绘图面板
		self.Centre()
		# closeBtn = wx.Button(self, label="Close")
		# closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
		# vbox = wx.BoxSizer(wx.VERTICAL)
		# vbox.Add(closeBtn, 0, flag=wx.ALIGN_CENTER|wx.BOTTOM, border=5)
		# self.SetSizer(vbox)
		# self.Center()

	def onClose(self, event):
		self.Close()

	def OnPlotDraw1(self, Data): #绘图函数
		# x = np.linspace(0,2*np.pi,10)
		# y = np.sin(x)
		# Data = [x,y]
		self.pc.Draw( MyDataObject( Data ) )


def MyDataObject(Data):
	data = list( map( list, zip(*[Data[1], Data[0]]) ) )
	markers = wxPyPlot.PolySpline( data, legend='Approximate solution', colour='red' )
	ret = [markers]
	GraphTitle = "SV Approximate solution"
	return wxPyPlot.PlotGraphics(ret, GraphTitle, "X Axis", "U Axis")


###########################################################################
## Class pnl_1d
###########################################################################

class pnl_1d ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 250,250 ), style = wx.TAB_TRAVERSAL )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.staticText_divide = wx.StaticText( self, wx.ID_ANY, u"输入域", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_divide.Wrap( -1 )
		self.staticText_divide.SetFont( wx.Font( 9, 70, 90, 92, False, "宋体" ) )
		
		bSizer.Add( self.staticText_divide, 0, wx.ALIGN_CENTER|wx.ALIGN_TOP|wx.ALL, 5 )
		
		gSizer = wx.GridSizer( 4, 2, 0, 0 )
		
		self.staticText_a = wx.StaticText( self, wx.ID_ANY, u"边界 a", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.staticText_a.Wrap( -1 )
		gSizer.Add( self.staticText_a, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.textCtrl_a = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT )
		gSizer.Add( self.textCtrl_a, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.staticText_b = wx.StaticText( self, wx.ID_ANY, u"边界 b", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.staticText_b.Wrap( -1 )
		gSizer.Add( self.staticText_b, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.textCtrl_b = wx.TextCtrl( self, wx.ID_ANY, u"6.2831853072", wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT )
		gSizer.Add( self.textCtrl_b, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.staticText_t = wx.StaticText( self, wx.ID_ANY, u"起始时间 t0", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.staticText_t.Wrap( -1 )
		gSizer.Add( self.staticText_t, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.textCtrl_t = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT )
		gSizer.Add( self.textCtrl_t, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.staticText_tend = wx.StaticText( self, wx.ID_ANY, u"终止时间 t", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.staticText_tend.Wrap( -1 )
		gSizer.Add( self.staticText_tend, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.textCtrl_tend = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT )
		gSizer.Add( self.textCtrl_tend, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer.Add( gSizer, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.divide_bot = wx.Button( self, wx.ID_ANY, u"网格剖分", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer.Add( self.divide_bot, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		
		# Connect Events
		self.divide_bot.Bind( wx.EVT_BUTTON, self.OnButtonDiv )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonDiv( self, event ):
		event.Skip()


###########################################################################
## Class pnl_2d
###########################################################################

class pnl_2d ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 250,270 ), style = wx.TAB_TRAVERSAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.staticText_divide = wx.StaticText( self, wx.ID_ANY, u"输入域", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_divide.Wrap( -1 )
		self.staticText_divide.SetFont( wx.Font( 9, 70, 90, 92, False, "宋体" ) )
		
		bSizer14.Add( self.staticText_divide, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		gSizer1 = wx.GridSizer( 5, 2, 0, 0 )
		
		self.staticText_a = wx.StaticText( self, wx.ID_ANY, u"边界 a", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.staticText_a.Wrap( -1 )
		gSizer1.Add( self.staticText_a, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_a = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT )
		gSizer1.Add( self.textCtrl_a, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.staticText_b = wx.StaticText( self, wx.ID_ANY, u"边界 b", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.staticText_b.Wrap( -1 )
		gSizer1.Add( self.staticText_b, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_b = wx.TextCtrl( self, wx.ID_ANY, u"6.2831853072", wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT )
		gSizer1.Add( self.textCtrl_b, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.staticText_c = wx.StaticText( self, wx.ID_ANY, u"边界 c", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.staticText_c.Wrap( -1 )
		gSizer1.Add( self.staticText_c, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_c = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT )
		gSizer1.Add( self.textCtrl_c, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.staticText_d = wx.StaticText( self, wx.ID_ANY, u"边界 d", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.staticText_d.Wrap( -1 )
		gSizer1.Add( self.staticText_d, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_d = wx.TextCtrl( self, wx.ID_ANY, u"6.2831853072", wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT )
		gSizer1.Add( self.textCtrl_d, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.staticText_t = wx.StaticText( self, wx.ID_ANY, u"时间 t", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.staticText_t.Wrap( -1 )
		gSizer1.Add( self.staticText_t, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_t = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT )
		gSizer1.Add( self.textCtrl_t, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer14.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		self.divide_bot = wx.Button( self, wx.ID_ANY, u"网格剖分", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.divide_bot, 0, wx.ALIGN_CENTER|wx.ALIGN_TOP|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()
		
		# Connect Events
		self.divide_bot.Bind( wx.EVT_BUTTON, self.OnButtonDiv )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonDiv( self, event ):
		event.Skip()