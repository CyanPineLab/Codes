# -*- coding: utf-8 -*- 
import wx
import wx.xrc

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"main", pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.div = None
		self.pnl = None

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, 70, 90, 90, False, "宋体" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		self.statusBar = self.CreateStatusBar( 1, 0, wx.ID_ANY )
		self.statusBar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		self.menubar = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.into = wx.MenuItem( self.file, wx.ID_ANY, u"导入(I)...", u"导入网格信息", wx.ITEM_NORMAL )
		self.file.AppendItem( self.into )
		
		self.output = wx.MenuItem( self.file, wx.ID_ANY, u"导出(E)...", u"导出数值结果", wx.ITEM_NORMAL )
		self.file.AppendItem( self.output )
		
		self.file.AppendSeparator()
		
		self.exit = wx.MenuItem( self.file, wx.ID_ANY, u"退出(X)"+ u"\t" + u"CTRL+Q", u"关闭程序", wx.ITEM_NORMAL )
		self.file.AppendItem( self.exit )
		
		self.menubar.Append( self.file, u"文件(F)" ) 
		
		self.edit = wx.Menu()
		self.set = wx.MenuItem( self.edit, wx.ID_ANY, u"设置(S)", u"打开设置对话框", wx.ITEM_NORMAL )
		self.edit.AppendItem( self.set )
		
		self.menubar.Append( self.edit, u"编辑(E)" ) 
		
		self.help = wx.Menu()
		self.about = wx.MenuItem( self.help, wx.ID_ANY, u"关于(A)", u"打开关于对话框", wx.ITEM_NORMAL )
		self.help.AppendItem( self.about )
		
		self.menubar.Append( self.help, u"帮助(H)" ) 
		
		self.SetMenuBar( self.menubar )
		
		box = wx.BoxSizer( wx.HORIZONTAL )
		
		bbox1 = wx.BoxSizer( wx.VERTICAL )
		
		self.staticline_top = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bbox1.Add( self.staticline_top, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.staticText_form = wx.StaticText( self, wx.ID_ANY, u"选择方程形式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_form.Wrap( -1 )
		self.staticText_form.SetFont( wx.Font( 9, 70, 90, 92, False, "宋体" ) )
		
		bbox1.Add( self.staticText_form, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice4Choices = [ u"1D-线性对流方程", u"1D-Burgers 方程", u"2D-线性对流方程", u"2D-浅水方程", u"3D-线性对流方程", u"3D- N-S方程" ]
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 220,-1 ), m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		bbox1.Add( self.m_choice4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.eq_bot = wx.Button( self, wx.ID_ANY, u"确定方程", wx.DefaultPosition, wx.DefaultSize, 0 )
		bbox1.Add( self.eq_bot, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.staticline_mid = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bbox1.Add( self.staticline_mid, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_domain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,300 ), wx.TAB_TRAVERSAL )
		bbox1.Add( self.pnl_domain, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.staticline_midd = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bbox1.Add( self.staticline_midd, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.staticText_cal = wx.StaticText( self, wx.ID_ANY, u"数值计算", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_cal.Wrap( -1 )
		self.staticText_cal.SetFont( wx.Font( 9, 70, 90, 92, False, "宋体" ) )
		
		bbox1.Add( self.staticText_cal, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.staticText_select = wx.StaticText( self, wx.ID_ANY, u"选择初始值文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_select.Wrap( -1 )
		bbox1.Add( self.staticText_select, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.filePicker_init = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bbox1.Add( self.filePicker_init, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.cal_bot = wx.Button( self, wx.ID_ANY, u"开始计算", wx.DefaultPosition, wx.DefaultSize, 0 )
		bbox1.Add( self.cal_bot, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.staticline_bot = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bbox1.Add( self.staticline_bot, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		box.Add( bbox1, 1, 0, 5 )
		
		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		box.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		bbox2 = wx.BoxSizer( wx.VERTICAL )
		
		bbox2.SetMinSize( wx.Size( 600,-1 ) ) 
		self.staticText_result = wx.StaticText( self, wx.ID_ANY, u"数值结果", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.staticText_result.Wrap( -1 )
		self.staticText_result.SetFont( wx.Font( 9, 70, 90, 92, False, "宋体" ) )
		
		bbox2.Add( self.staticText_result, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline81 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bbox2.Add( self.m_staticline81, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,400 ), wx.TAB_TRAVERSAL )
		bbox2.Add( self.panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bbox2.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.numerical_bot = wx.Button( self, wx.ID_ANY, u"数值结果", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.numerical_bot, 0, wx.ALL, 5 )
		
		self.figure_bot = wx.Button( self, wx.ID_ANY, u"数值图像", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.figure_bot, 0, wx.ALL, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.output_bot = wx.Button( self, wx.ID_ANY, u"导出数据", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.output_bot, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		
		bbox2.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bbox2.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		box.Add( bbox2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( box )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.OnMenuExit, id = self.exit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSet, id = self.set.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuAbout, id = self.about.GetId() )
		self.eq_bot.Bind( wx.EVT_BUTTON, self.OnButtonForm )
		self.cal_bot.Bind( wx.EVT_BUTTON, self.OnButtonCal )
		self.numerical_bot.Bind( wx.EVT_BUTTON, self.OnButtonNum )
		self.figure_bot.Bind( wx.EVT_BUTTON, self.OnButtonFig )
		self.output_bot.Bind( wx.EVT_BUTTON, self.OnButtonOut )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnMenuExit( self, event ):
		event.Skip()
	
	def OnMenuSet( self, event ):
		event.Skip()
	
	def OnMenuAbout( self, event ):
		event.Skip()
	
	def OnButtonForm( self, event ):
		event.Skip()
	
	def OnButtonCal( self, event ):
		event.Skip()
	
	def OnButtonNum( self, event ):
		event.Skip()
	
	def OnButtonFig( self, event ):
		event.Skip()
	
	def OnButtonOut( self, event ):
		event.Skip()
	

