﻿__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

from librarian.library import Library
from librarian.card import Card
import os


class MainForm(Form):
	def __init__(self, dbname):
		self.InitializeComponent()
		if dbname is None:
			self.dbname = "library.lbr"
		else:
			self.dbname = dbname
		self.library = Library(self.dbname)
		if not os.path.exists(self.dbname):
			self.library.create_db()
		self.card = None
		self.UpdateCodeList()
	
	def InitializeComponent(self):
		self._splitContainer1 = System.Windows.Forms.SplitContainer()
		self._SearchText = System.Windows.Forms.TextBox()
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
		self._CodeList = System.Windows.Forms.ListView()
		self._Codes = System.Windows.Forms.ColumnHeader()
		self._Names = System.Windows.Forms.ColumnHeader()
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
		self._splitContainer1.Panel1.Controls.Add(self._CodeList)
		self._splitContainer1.Panel1.Controls.Add(self._CreateButton)
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
		self._SearchText.TextChanged += self.SearchTextTextChanged
		# 
		# ButtonSave
		# 
		self._ButtonSave.Location = System.Drawing.Point(3, 464)
		self._ButtonSave.Name = "ButtonSave"
		self._ButtonSave.Size = System.Drawing.Size(376, 23)
		self._ButtonSave.TabIndex = 0
		self._ButtonSave.Text = "Save"
		self._ButtonSave.UseVisualStyleBackColor = True
		self._ButtonSave.Click += self.ButtonSaveClick
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
		# CodeList
		# 
		self._CodeList.Columns.AddRange(System.Array[System.Windows.Forms.ColumnHeader](
			[self._Codes,
			self._Names]))
		self._CodeList.Location = System.Drawing.Point(3, 29)
		self._CodeList.Name = "CodeList"
		self._CodeList.Size = System.Drawing.Size(206, 458)
		self._CodeList.TabIndex = 4
		self._CodeList.UseCompatibleStateImageBehavior = False
		self._CodeList.View = System.Windows.Forms.View.Details
		self._CodeList.SelectedIndexChanged += self.CodeListSelectedIndexChanged
		# 
		# Codes
		# 
		self._Codes.Text = "Code"
		self._Codes.Width = 62
		# 
		# Names
		# 
		self._Names.Text = "Name"
		self._Names.Width = 140
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
		
	def UpdateCodeList(self):
		"""Update the CodeList display taking SearchText into account."""
		codes = []
		with self.library.connection() as libdb:
			if self._SearchText.Text:
				codes = libdb.execute(
					"SELECT code FROM CARDS WHERE code like ?",
					(self._SearchText.Text + '%',)).fetchall()
			else:
				codes = libdb.execute("SELECT code FROM CARDS").fetchall()
				
		self._CodeList.Items.Clear()
		self._CodeList.BeginUpdate()
		for code in codes:
			card = self.library.load_card(code, False)
			pos = len(self._CodeList.Items)
			self._CodeList.Items.Add(str(card.code))
			self._CodeList.Items[pos].SubItems.Add(card.name)
		self._CodeList.EndUpdate()
		
	def LoadCard(self, code):
		"""Load a card."""
		with self.library.connection() as libdb:
			codes = libdb.execute("SELECT code FROM CARDS").fetchall()
		codes = [fetched[0] for fetched in codes]
		
		loadstring = None
		if code in codes:
			with self.library.connection() as libdb:
			    loadstring = libdb.execute(
			        "SELECT card FROM CARDS WHERE code = {0}".format(
			    		str(code))).fetchone()
			    loadstring = loadstring[0] if loadstring else None
		self.card = Card(code=code, loadstring=loadstring)
		self._TextCode.Text = str(self.card.code)
		self._TextName.Text = self.card.name
		
	def SaveCard(self):
		self.card = Card(int(self._TextCode.Text), self._TextName.Text)
		with self.library.connection() as libdb:
			codes = libdb.execute("SELECT code FROM CARDS").fetchall()
		codes = [fetched[0] for fetched in codes]
		
		if self.card.code in codes:
			with self.library.connection() as libdb:
				libdb.execute("DELETE from CARDS where code = {0}".format(
					self.card.code))
		self.library.save_card(self.card)
		self.UpdateCodeList()

	def SearchTextTextChanged(self, sender, e):
		self.UpdateCodeList()

	def CodeListSelectedIndexChanged(self, sender, e):
		if self._CodeList.SelectedItems:
			code = int(self._CodeList.SelectedItems[0].Text)
			self.LoadCard(code)

	def ButtonSaveClick(self, sender, e):
		self.SaveCard()