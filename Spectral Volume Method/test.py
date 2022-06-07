# -*- coding: utf-8 -*- 
import wx
import wx.xrc
import numpy as np
from MyFrame import MyFrame
from Dialog import about, set
from Panel import NumPanel, FigPanel, pnl_1d, pnl_2d
from Division import Division
from SV1d import SV1d

# SV设置
N = 8
k = 3
rk = 2

# 方程形式
Equation = 0
Dimension = 1

# 空间域
a, b = 0, 2*np.pi
c, d = 0, 2*np.pi
e, f = 0, 2*np.pi

# 时间域
t0, t = 0, 1

# 数值解
data = []

#########################################################################
# 继承类
#########################################################################
class About(about):
    def OnButtonCopy( self, event ):
        text_obj = wx.TextDataObject()
        text_obj.SetText(self.aboutText.GetLabel())
        if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
            wx.TheClipboard.SetData(text_obj)
            wx.TheClipboard.Close()

    def OnButtonOk( self, event ):
        self.Close(True)


class Set(set):
	def OnButtonCanl( self, event ):
		self.Close(True)
	
	def OnButtonOk( self, event ):
		global N, k, rk
		N = int( self.cholis11[ self.m_choice11.GetSelection() ] )
		k = int( self.cholis12[ self.m_choice12.GetSelection() ] )
		rk = int( self.cholis13[ self.m_choice13.GetSelection() ] )
		dlg = wx.MessageDialog( self, u"设置修改成功！", u"设置", wx.OK | wx.ICON_INFORMATION )
		if dlg.ShowModal() == wx.ID_OK:
			self.Close( True )
		dlg.Destroy()


class Pnl_1d(pnl_1d):
	def OnButtonDiv( self, event ):
		global a, b, t0, t
		a = float( self.textCtrl_a.GetValue() )
		b = float( self.textCtrl_b.GetValue() )
		t0 = float( self.textCtrl_t.GetValue() )
		t = float( self.textCtrl_tend.GetValue() )
		S = np.linspace(a, b, N+1)
		divion = Division(S, k, 5)
		with open( 'division.txt', 'w' ) as file:
			for i in range(N):
				for j in range(len(divion[i])):
					file.write('{}\n'.format( divion[i,j] ) )

		dlg = wx.MessageDialog( self, u"剖分成功！剖分点已导出到division.txt文件", u"剖分提示", wx.OK | wx.ICON_INFORMATION )
		if dlg.ShowModal() == wx.ID_OK:
			dlg.Destroy()


class Pnl_2d(pnl_2d):
	def OnButtonDiv( self, event ):
		global a, b, c, d, t
		a = float( self.textCtrl_a.GetValue() )
		b = float( self.textCtrl_b.GetValue() )
		c = float( self.textCtrl_c.GetValue() )
		d = float( self.textCtrl_d.GetValue() )
		t = float( self.textCtrl_tend.GetValue() )
		S = np.linspace(a, b, N+1)
		divion = Division(S, k, 5)
		with open( 'division.txt', 'w' ) as file:
			for i in range(N):
				for j in range(len(divion[i])):
					file.write('{}\n'.format( divion[i,j] )) 

		dlg = wx.MessageDialog( self, u"剖分成功！剖分点已导出到division.txt文件", u"剖分提示", wx.OK | wx.ICON_INFORMATION )
		if dlg.ShowModal() == wx.ID_OK:
			dlg.Destroy()


#########################################################################
# 主界面
#########################################################################
class MianWindow(MyFrame):
	def OnMenuExit( self, event ):
		self.Close(True)

	def OnMenuSet( self, event ):
		set_dlg = Set(self)
		set_dlg.Show()

	def OnMenuAbout( self, event ):
		abt_dlg = About(self)
		abt_dlg.Show()

	def OnButtonNum( self, event ):
		if self.pnl:
			self.pnl.Destroy()
		self.pnl = NumPanel(self.panel)
		for row in range(len(data[0])):
			for col in range(Dimension+1):
				self.pnl.gridNum.SetCellValue(row, col,"{}".format(data[col][row]))
		self.pnl.Show()

	def OnButtonFig( self, event ):
		if self.pnl:
			self.pnl.Destroy()
		self.pnl = FigPanel(self.panel)
		self.pnl.OnPlotDraw1(data)
		self.pnl.Show()
	
	def OnButtonForm( self, event ):
		global Equation, Dimension
		Equation = self.m_choice4.GetSelection()
		if self.div:
			self.div.Destroy()
		if Equation == 0 or Equation == 1:
			Dimension = 1
			self.div = Pnl_1d(self.pnl_domain)
		else:
			Dimension = 2
			self.div = Pnl_2d(self.pnl_domain)
		self.div.Show()
	
	def OnButtonCal( self, event ):
		global data
		if Equation == 0 or Equation == 1:
			ini_path = self.filePicker_init.GetPath()
			print(ini_path)
			style = 0
			with open( ini_path, 'r' ) as file:
				s = file.readline()
				if s[0] != '0':
					style = 1
			data = SV1d(a, b, N, k, t0, t, style)
		dlg = wx.MessageDialog( self, u"计算完成！", u"计算提示", wx.OK | wx.ICON_INFORMATION )
		if dlg.ShowModal() == wx.ID_OK:
			dlg.Destroy()
	
	def OnButtonOut( self, event ):
		with open( 'result.txt', 'w' ) as file:
			for i in range(len(data[0])):
				if Dimension == 1:
					file.write( '{} {}\n'.format(data[0][i], data[1][i]) )
				if Dimension == 2:
					file.write( '{} {} {}\n'.format(data[0][i], data[1][i], data[2][i]) )
				if Dimension == 3:
					file.write( '{} {} {} {}\n'.format(data[0][i], data[1][i], data[2][i], data[3][i]) )
		dlg = wx.MessageDialog( self, u"导出成功！数值解已导出到result.txt文件", u"导出提示", wx.OK | wx.ICON_INFORMATION )
		if dlg.ShowModal() == wx.ID_OK:
			dlg.Destroy()

#########################################################################
# main函数
#########################################################################
if __name__ == '__main__':
    app = wx.App()
    main_win = MianWindow(None)
    main_win.Show()
    app.MainLoop()
