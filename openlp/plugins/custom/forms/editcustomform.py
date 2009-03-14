# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4
"""
OpenLP - Open Source Lyrics Projection
Copyright (c) 2008 Raoul Snyman
Portions copyright (c) 2008-2009 Martin Thompson, Tim Bentley,

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; version 2 of the License.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc., 59 Temple
Place, Suite 330, Boston, MA 02111-1307 USA
"""
from PyQt4 import Qt, QtCore, QtGui

from editcustomdialog import Ui_customEditDialog
from openlp.core.lib import SongXMLBuilder, SongXMLParser
from openlp.plugins.custom.lib.models import CustomSlide

class EditCustomForm(QtGui.QDialog, Ui_customEditDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, custommanager, parent = None):
        """
        Constructor
        """
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        # Connecting signals and slots
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.rejected)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        QtCore.QObject.connect(self.AddButton, QtCore.SIGNAL("pressed()"), self.onAddButtonPressed)
        QtCore.QObject.connect(self.EditButton, QtCore.SIGNAL("pressed()"), self.onEditButtonPressed)
        QtCore.QObject.connect(self.SaveButton, QtCore.SIGNAL("pressed()"), self.onSaveButtonPressed)
        QtCore.QObject.connect(self.DeleteButton, QtCore.SIGNAL("pressed()"), self.onDeleteButtonPressed)
        QtCore.QObject.connect(self.ClearButton, QtCore.SIGNAL("pressed()"), self.onClearButtonPressed)
        QtCore.QObject.connect(self.UpButton, QtCore.SIGNAL("pressed()"), self.onUpButtonPressed)
        QtCore.QObject.connect(self.DownButton, QtCore.SIGNAL("pressed()"), self.onDownButtonPressed)        
        QtCore.QObject.connect(self.TitleEdit, QtCore.SIGNAL("lostFocus()"), self.validate)                

        QtCore.QObject.connect(self.VerseListView, 
            QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.onVerseListViewSelected)
        QtCore.QObject.connect(self.VerseListView, 
            QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), self.onVerseListViewPressed)
        # Create other objects and forms
        self.custommanager = custommanager
        self.initialise()
        self.VerseListView.setAlternatingRowColors(True)
        #self.savebutton = self.ButtonBox.button(QtGui.QDialogButtonBox.Save)
        
    def initialise(self):
        self.valid = True
        self.DeleteButton.setEnabled(False)
        self.EditButton.setEnabled(False)
        self.SaveButton.setEnabled(False)
        self.TitleEdit.setText('')
        self.CreditEdit.setText('')
        self.VerseTextEdit.clear()
        self.VerseListView.clear()
        #make sure we have a new item 
        self.customSlide = CustomSlide()    

    def loadCustom(self, id):
        self.customSlide = CustomSlide()
        self.initialise()
        if id != 0:
            self.customSlide = self.custommanager.get_custom(id)
            self.TitleEdit.setText(self.customSlide.title)
            self.CreditEdit.setText(self.customSlide.title)
            
            songXML=SongXMLParser(self.customSlide.text)
            verseList = songXML.get_verses()
            for verse in verseList:
                self.VerseListView.addItem(verse[1])
            self.validate()

    def accept(self):
        self.validate()
        if self.valid:
            sxml=SongXMLBuilder()
            sxml.new_document()
            sxml.add_lyrics_to_song()
            count = 1
            for i in range (0, self.VerseListView.count()):
                sxml.add_verse_to_lyrics(u'custom', str(count),  str(self.VerseListView.item(i).text()))
                count += 1
            self.customSlide.title = unicode(self.TitleEdit.displayText())
            self.customSlide.text = unicode(sxml.extract_xml())
            self.customSlide.credits = unicode(self.CreditEdit.displayText())
            self.custommanager.save_slide(self.customSlide)
            self.close()

    def rejected(self):
        self.close()

    def onUpButtonPressed(self):
        selectedRow = self.VerseListView.currentRow()
        if selectedRow != 0:
            qw = self.VerseListView.takeItem(selectedRow)
            self.VerseListView.insertItem(selectedRow - 1, qw)
            self.VerseListView.setCurrentRow(selectedRow - 1)

    def onDownButtonPressed(self):
        selectedRow = self.VerseListView.currentRow()
        if selectedRow != self.VerseListView.count() - 1: # zero base arrays
            qw = self.VerseListView.takeItem(selectedRow)
            self.VerseListView.insertItem(selectedRow + 1, qw)
            self.VerseListView.setCurrentRow(selectedRow + 1)            

    def onClearButtonPressed(self):
        self.VerseTextEdit.clear()

    def onVerseListViewPressed(self, item):
        self.DeleteButton.setEnabled(True)
        self.EditButton.setEnabled(True)
 
    def onVerseListViewSelected(self, item):
        self.VerseTextEdit.setPlainText(item.text())
        self.DeleteButton.setEnabled(False)
        self.EditButton.setEnabled(False)
        self.SaveButton.setEnabled(True)

    def onAddButtonPressed(self):
        self.VerseListView.addItem(self.VerseTextEdit.toPlainText())
        self.DeleteButton.setEnabled(False)
        self.VerseTextEdit.clear()

    def onEditButtonPressed(self):
        self.VerseTextEdit.setPlainText(self.VerseListView.currentItem().text())
        self.DeleteButton.setEnabled(False)
        self.EditButton.setEnabled(False)
        self.SaveButton.setEnabled(True)

    def onSaveButtonPressed(self):
        self.VerseListView.currentItem().setText(self.VerseTextEdit.toPlainText())
        self.SaveButton.setEnabled(False)
        self.EditButton.setEnabled(False)

    def onDeleteButtonPressed(self):
        self.VerseListView.takeItem(self.VerseListView.currentRow())
        self.EditButton.setEnabled(False)

    def validate(self):
        invalid = 0
        self.valid = True
        if len(self.TitleEdit.displayText()) == 0:
            invalid += 1
            self.TitleLabel.setStyleSheet('color: red')
        else:
            self.TitleLabel.setStyleSheet('color: black')
        if invalid == 1:
            self.valid = False
