# -*- coding: utf-8 -*- 
import wx
import wx.xrc

###########################################################################
## Class about
###########################################################################
class about ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"关于 svFlow", pos = wx.DefaultPosition, size = wx.Size( 320,320 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MINIMIZE_BOX )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		box = wx.BoxSizer( wx.VERTICAL )
		
		bbox1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.logo = wx.StaticBitmap( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_QUESTION, wx.ART_CMN_DIALOG ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bbox1.Add( self.logo, 0, wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"svFlow 1.0.0", wx.DefaultPosition, wx.Size( 200,-1 ), wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 9, 70, 90, 92, False, "宋体" ) )
		
		bbox1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		box.Add( bbox1, 1, wx.EXPAND, 5 )
		
		self.line1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		box.Add( self.line1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.aboutText = wx.StaticText( self, wx.ID_ANY, u"\n      使用方法：谱有限体积法\n      针对方程：双曲守恒律\n      编程语言：Python", wx.Point( -1,-1 ), wx.Size( 300,150 ), wx.ALIGN_LEFT )
		self.aboutText.Wrap( -1 )
		box.Add( self.aboutText, 0, wx.ALL, 5 )
		
		self.line2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		box.Add( self.line2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bbox2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.copy = wx.Button( self, wx.ID_ANY, u"复制", wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.BU_EXACTFIT )
		bbox2.Add( self.copy, 0, wx.ALL, 5 )
		
		self.ok = wx.Button( self, wx.ID_ANY, u"确定", wx.Point( -1,-1 ), wx.DefaultSize, wx.BU_EXACTFIT )
		bbox2.Add( self.ok, 0, wx.ALL, 5 )
		
		
		box.Add( bbox2, 1, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( box )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.copy.Bind( wx.EVT_BUTTON, self.OnButtonCopy )
		self.ok.Bind( wx.EVT_BUTTON, self.OnButtonOk )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonCopy( self, event ):
		event.Skip()
	
	def OnButtonOk( self, event ):
		event.Skip()
	

###########################################################################
## Class set
###########################################################################
class set ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.Size( 320,320 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MINIMIZE_BOX )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		box = wx.BoxSizer( wx.VERTICAL )
		
		bbox1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.logo = wx.StaticBitmap( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_QUESTION, wx.ART_CMN_DIALOG ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bbox1.Add( self.logo, 0, wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"svFlow 1.0.0", wx.DefaultPosition, wx.Size( 200,-1 ), wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 9, 70, 90, 92, False, "宋体" ) )
		
		bbox1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		box.Add( bbox1, 1, wx.EXPAND, 5 )
		
		self.line1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		box.Add( self.line1, 0, wx.EXPAND |wx.ALL, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		gSizer2.SetMinSize( wx.Size( -1,150 ) ) 
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"谱体积数量 N", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer2.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.cholis11 = [ u"4", u"8", u"16" ]
		self.m_choice11 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), self.cholis11, 0 )
		self.m_choice11.SetSelection( 1 )
		gSizer2.Add( self.m_choice11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"多项式阶数 k", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		gSizer2.Add( self.m_staticText14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.cholis12 = [ u"1", u"2", u"3" ]
		self.m_choice12 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), self.cholis12, 0 )
		self.m_choice12.SetSelection( 2 )
		gSizer2.Add( self.m_choice12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"龙格-库塔法阶数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		gSizer2.Add( self.m_staticText15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.cholis13 = [ u"2", u"3", u"4" ]
		self.m_choice13 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), self.cholis13, 0 )
		self.m_choice13.SetSelection( 0 )
		gSizer2.Add( self.m_choice13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		box.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.line2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		box.Add( self.line2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bbox2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cancel = wx.Button( self, wx.ID_ANY, u"取消", wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.BU_EXACTFIT )
		bbox2.Add( self.cancel, 0, wx.ALL, 5 )
		
		self.ok = wx.Button( self, wx.ID_ANY, u"确定", wx.Point( -1,-1 ), wx.DefaultSize, wx.BU_EXACTFIT )
		bbox2.Add( self.ok, 0, wx.ALL, 5 )
		
		
		box.Add( bbox2, 1, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( box )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cancel.Bind( wx.EVT_BUTTON, self.OnButtonCanl )
		self.ok.Bind( wx.EVT_BUTTON, self.OnButtonOk )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonCanl( self, event ):
		event.Skip()
	
	def OnButtonOk( self, event ):
		event.Skip()

