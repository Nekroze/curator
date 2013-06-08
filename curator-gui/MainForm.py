import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._splitContainer1 = System.Windows.Forms.SplitContainer()
		self._SearchText = System.Windows.Forms.TextBox()
		self._CodeList = System.Windows.Forms.ListBox()
		self._LoadButton = System.Windows.Forms.Button()
		self._ButtonSave = System.Windows.Forms.Button()
		self._TextName = System.Windows.Forms.TextBox()
		self._TextCode = System.Windows.Forms.TextBox()
		self._labelCode = System.Windows.Forms.Label()
		self._labelName = System.Windows.Forms.Label()
		self._labelAttributes = System.Windows.Forms.Label()
		self._labelAbilities = System.Windows.Forms.Label()
		self._ComboAbilities = System.Windows.Forms.ComboBox()
		self._labelInfo = System.Windows.Forms.Label()
		self._ComboInfo = System.Windows.Forms.ComboBox()
		self._CreateButton = System.Windows.Forms.Button()
		self._TextAttributes = System.Windows.Forms.TextBox()
		self._TextAbilities = System.Windows.Forms.TextBox()
		self._TextInfo = System.Windows.Forms.TextBox()
		self._splitContainer1.BeginInit()
		self._splitContainer1.Panel1.SuspendLayout()
		self._splitContainer1.Panel2.SuspendLayout()
		self._splitContainer1.SuspendLayout()
		self.SuspendLayout()
		# 
		# splitContainer1
		# 
		self._splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill
		self._splitContainer1.Location = System.Drawing.Point(0, 0)
		self._splitContainer1.Name = "splitContainer1"
		# 
		# splitContainer1.Panel1
		# 
		self._splitContainer1.Panel1.Controls.Add(self._CreateButton)
		self._splitContainer1.Panel1.Controls.Add(self._LoadButton)
		self._splitContainer1.Panel1.Controls.Add(self._CodeList)
		self._splitContainer1.Panel1.Controls.Add(self._SearchText)
		# 
		# splitContainer1.Panel2
		# 
		self._splitContainer1.Panel2.Controls.Add(self._TextInfo)
		self._splitContainer1.Panel2.Controls.Add(self._TextAbilities)
		self._splitContainer1.Panel2.Controls.Add(self._TextAttributes)
		self._splitContainer1.Panel2.Controls.Add(self._ComboInfo)
		self._splitContainer1.Panel2.Controls.Add(self._labelInfo)
		self._splitContainer1.Panel2.Controls.Add(self._ComboAbilities)
		self._splitContainer1.Panel2.Controls.Add(self._labelAbilities)
		self._splitContainer1.Panel2.Controls.Add(self._labelAttributes)
		self._splitContainer1.Panel2.Controls.Add(self._labelName)
		self._splitContainer1.Panel2.Controls.Add(self._labelCode)
		self._splitContainer1.Panel2.Controls.Add(self._TextCode)
		self._splitContainer1.Panel2.Controls.Add(self._TextName)
		self._splitContainer1.Panel2.Controls.Add(self._ButtonSave)
		self._splitContainer1.Size = System.Drawing.Size(600, 490)
		self._splitContainer1.SplitterDistance = 212
		self._splitContainer1.TabIndex = 0
		# 
		# SearchText
		# 
		self._SearchText.Location = System.Drawing.Point(3, 3)
		self._SearchText.Name = "SearchText"
		self._SearchText.Size = System.Drawing.Size(153, 20)
		self._SearchText.TabIndex = 0
		# 
		# CodeList
		# 
		self._CodeList.FormattingEnabled = True
		self._CodeList.Items.AddRange(System.Array[System.Object](
			["test",
			"test2"]))
		self._CodeList.Location = System.Drawing.Point(3, 29)
		self._CodeList.MultiColumn = True
		self._CodeList.Name = "CodeList"
		self._CodeList.Size = System.Drawing.Size(206, 433)
		self._CodeList.Sorted = True
		self._CodeList.TabIndex = 1
		# 
		# LoadButton
		# 
		self._LoadButton.Location = System.Drawing.Point(3, 464)
		self._LoadButton.Name = "LoadButton"
		self._LoadButton.Size = System.Drawing.Size(206, 23)
		self._LoadButton.TabIndex = 2
		self._LoadButton.Text = "Load"
		self._LoadButton.UseVisualStyleBackColor = True
		# 
		# ButtonSave
		# 
		self._ButtonSave.Location = System.Drawing.Point(3, 464)
		self._ButtonSave.Name = "ButtonSave"
		self._ButtonSave.Size = System.Drawing.Size(376, 23)
		self._ButtonSave.TabIndex = 0
		self._ButtonSave.Text = "Save"
		self._ButtonSave.UseVisualStyleBackColor = True
		# 
		# TextName
		# 
		self._TextName.Location = System.Drawing.Point(116, 29)
		self._TextName.Name = "TextName"
		self._TextName.Size = System.Drawing.Size(263, 20)
		self._TextName.TabIndex = 1
		# 
		# TextCode
		# 
		self._TextCode.Location = System.Drawing.Point(3, 29)
		self._TextCode.Name = "TextCode"
		self._TextCode.Size = System.Drawing.Size(107, 20)
		self._TextCode.TabIndex = 2
		# 
		# labelCode
		# 
		self._labelCode.Location = System.Drawing.Point(3, 3)
		self._labelCode.Name = "labelCode"
		self._labelCode.Size = System.Drawing.Size(107, 20)
		self._labelCode.TabIndex = 3
		self._labelCode.Text = "Code"
		# 
		# labelName
		# 
		self._labelName.Location = System.Drawing.Point(116, 3)
		self._labelName.Name = "labelName"
		self._labelName.Size = System.Drawing.Size(263, 20)
		self._labelName.TabIndex = 4
		self._labelName.Text = "Name"
		# 
		# labelAttributes
		# 
		self._labelAttributes.Location = System.Drawing.Point(3, 52)
		self._labelAttributes.Name = "labelAttributes"
		self._labelAttributes.Size = System.Drawing.Size(100, 13)
		self._labelAttributes.TabIndex = 6
		self._labelAttributes.Text = "Attributes"
		# 
		# labelAbilities
		# 
		self._labelAbilities.Location = System.Drawing.Point(3, 140)
		self._labelAbilities.Name = "labelAbilities"
		self._labelAbilities.Size = System.Drawing.Size(100, 14)
		self._labelAbilities.TabIndex = 7
		self._labelAbilities.Text = "Abilities"
		# 
		# ComboAbilities
		# 
		self._ComboAbilities.FormattingEnabled = True
		self._ComboAbilities.Location = System.Drawing.Point(3, 157)
		self._ComboAbilities.Name = "ComboAbilities"
		self._ComboAbilities.Size = System.Drawing.Size(376, 21)
		self._ComboAbilities.TabIndex = 9
		# 
		# labelInfo
		# 
		self._labelInfo.Location = System.Drawing.Point(3, 282)
		self._labelInfo.Name = "labelInfo"
		self._labelInfo.Size = System.Drawing.Size(100, 13)
		self._labelInfo.TabIndex = 10
		self._labelInfo.Text = "Info"
		# 
		# ComboInfo
		# 
		self._ComboInfo.FormattingEnabled = True
		self._ComboInfo.Location = System.Drawing.Point(3, 298)
		self._ComboInfo.Name = "ComboInfo"
		self._ComboInfo.Size = System.Drawing.Size(376, 21)
		self._ComboInfo.TabIndex = 11
		# 
		# CreateButton
		# 
		self._CreateButton.Location = System.Drawing.Point(162, 3)
		self._CreateButton.Name = "CreateButton"
		self._CreateButton.Size = System.Drawing.Size(47, 20)
		self._CreateButton.TabIndex = 3
		self._CreateButton.Text = "Create"
		self._CreateButton.UseVisualStyleBackColor = True
		# 
		# TextAttributes
		# 
		self._TextAttributes.Location = System.Drawing.Point(3, 68)
		self._TextAttributes.Multiline = True
		self._TextAttributes.Name = "TextAttributes"
		self._TextAttributes.Size = System.Drawing.Size(376, 69)
		self._TextAttributes.TabIndex = 12
		# 
		# TextAbilities
		# 
		self._TextAbilities.Location = System.Drawing.Point(3, 184)
		self._TextAbilities.Multiline = True
		self._TextAbilities.Name = "TextAbilities"
		self._TextAbilities.Size = System.Drawing.Size(376, 95)
		self._TextAbilities.TabIndex = 13
		# 
		# TextInfo
		# 
		self._TextInfo.Location = System.Drawing.Point(3, 325)
		self._TextInfo.Multiline = True
		self._TextInfo.Name = "TextInfo"
		self._TextInfo.Size = System.Drawing.Size(376, 133)
		self._TextInfo.TabIndex = 14
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(600, 490)
		self.Controls.Add(self._splitContainer1)
		self.Name = "MainForm"
		self.Text = "Curator"
		self._splitContainer1.Panel1.ResumeLayout(False)
		self._splitContainer1.Panel1.PerformLayout()
		self._splitContainer1.Panel2.ResumeLayout(False)
		self._splitContainer1.Panel2.PerformLayout()
		self._splitContainer1.EndInit()
		self._splitContainer1.ResumeLayout(False)
		self.ResumeLayout(False)