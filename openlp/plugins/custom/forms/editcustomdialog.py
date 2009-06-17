# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editcustomdialog.ui'
#
# Created: Sat Mar  7 09:01:43 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from openlp.core.lib import translate

class Ui_customEditDialog(object):
    def setupUi(self, customEditDialog):
        customEditDialog.setObjectName(u'customEditDialog')
        customEditDialog.resize(590, 541)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(u':/icon/openlp-logo-16x16.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        customEditDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(customEditDialog)
        self.gridLayout.setObjectName(u'gridLayout')
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(u'horizontalLayout')
        self.TitleLabel = QtGui.QLabel(customEditDialog)
        self.TitleLabel.setObjectName(u'TitleLabel')
        self.horizontalLayout.addWidget(self.TitleLabel)
        self.TitleEdit = QtGui.QLineEdit(customEditDialog)
        self.TitleEdit.setObjectName(u'TitleEdit')
        self.horizontalLayout.addWidget(self.TitleEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u'horizontalLayout_4')
        self.VerseListView = QtGui.QListWidget(customEditDialog)
        self.VerseListView.setObjectName(u'VerseListView')
        self.VerseListView.setAlternatingRowColors(True)
        self.horizontalLayout_4.addWidget(self.VerseListView)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(u'verticalLayout')
        self.UpButton = QtGui.QPushButton(customEditDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(u':/services/service_up.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UpButton.setIcon(icon1)
        self.UpButton.setObjectName(u'UpButton')
        self.verticalLayout.addWidget(self.UpButton)
        spacerItem = QtGui.QSpacerItem(20, 128, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.DownButton = QtGui.QPushButton(customEditDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(u':/services/service_down.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DownButton.setIcon(icon2)
        self.DownButton.setObjectName(u'DownButton')
        self.verticalLayout.addWidget(self.DownButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.EditWidget = QtGui.QWidget(customEditDialog)
        self.EditWidget.setObjectName(u'EditWidget')
        self.EditLayout = QtGui.QHBoxLayout(self.EditWidget)
        self.EditLayout.setSpacing(8)
        self.EditLayout.setMargin(0)
        self.EditLayout.setObjectName(u'EditLayout')
        self.VerseTextEdit = QtGui.QTextEdit(self.EditWidget)
        self.VerseTextEdit.setObjectName(u'VerseTextEdit')
        self.EditLayout.addWidget(self.VerseTextEdit)
        self.ButtonWidget = QtGui.QWidget(self.EditWidget)
        self.ButtonWidget.setObjectName(u'ButtonWidget')
        self.ButtonLayout = QtGui.QVBoxLayout(self.ButtonWidget)
        self.ButtonLayout.setSpacing(8)
        self.ButtonLayout.setMargin(0)
        self.ButtonLayout.setObjectName(u'ButtonLayout')
        self.AddButton = QtGui.QPushButton(self.ButtonWidget)
        self.AddButton.setObjectName(u'AddButton')
        self.ButtonLayout.addWidget(self.AddButton)
        self.EditButton = QtGui.QPushButton(self.ButtonWidget)
        self.EditButton.setObjectName(u'EditButton')
        self.ButtonLayout.addWidget(self.EditButton)
        self.SaveButton = QtGui.QPushButton(self.ButtonWidget)
        self.SaveButton.setObjectName(u'SaveButton')
        self.ButtonLayout.addWidget(self.SaveButton)
        self.DeleteButton = QtGui.QPushButton(self.ButtonWidget)
        self.DeleteButton.setObjectName(u'DeleteButton')
        self.ButtonLayout.addWidget(self.DeleteButton)
        self.ClearButton = QtGui.QPushButton(self.ButtonWidget)
        self.ClearButton.setObjectName(u'ClearButton')
        self.ButtonLayout.addWidget(self.ClearButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.ButtonLayout.addItem(spacerItem1)
        self.EditLayout.addWidget(self.ButtonWidget)
        self.gridLayout.addWidget(self.EditWidget, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(u'horizontalLayout')
        self.ThemeLabel = QtGui.QLabel(customEditDialog)
        self.ThemeLabel.setObjectName(u'ThemeLabel')
        self.horizontalLayout.addWidget(self.ThemeLabel)
        self.ThemecomboBox = QtGui.QComboBox(customEditDialog)
        self.ThemecomboBox.setObjectName(u'ThemecomboBox')
        self.horizontalLayout.addWidget(self.ThemecomboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u'horizontalLayout_2')
        self.CreditLabel = QtGui.QLabel(customEditDialog)
        self.CreditLabel.setObjectName(u'CreditLabel')
        self.horizontalLayout_2.addWidget(self.CreditLabel)
        self.CreditEdit = QtGui.QLineEdit(customEditDialog)
        self.CreditEdit.setObjectName(u'CreditEdit')
        self.horizontalLayout_2.addWidget(self.CreditEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(customEditDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(u'buttonBox')
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)
        self.retranslateUi(customEditDialog)
        QtCore.QMetaObject.connectSlotsByName(customEditDialog)
        customEditDialog.setTabOrder(self.TitleEdit, self.VerseTextEdit)
        customEditDialog.setTabOrder(self.VerseTextEdit, self.EditButton)
        customEditDialog.setTabOrder(self.EditButton, self.SaveButton)
        customEditDialog.setTabOrder(self.SaveButton, self.CreditEdit)
        customEditDialog.setTabOrder(self.CreditEdit, self.VerseListView)
        customEditDialog.setTabOrder(self.VerseListView, self.AddButton)
        customEditDialog.setTabOrder(self.AddButton, self.DeleteButton)
        customEditDialog.setTabOrder(self.DeleteButton, self.buttonBox)

    def retranslateUi(self, customEditDialog):
        customEditDialog.setWindowTitle(translate(u'customEditDialog', u'Edit Custom Slides'))
        self.TitleLabel.setText(translate(u'customEditDialog', u'Title:'))
        self.AddButton.setText(translate(u'customEditDialog', u'Add'))
        self.EditButton.setText(translate(u'customEditDialog', u'Edit'))
        self.SaveButton.setText(translate(u'customEditDialog', u'Save'))
        self.DeleteButton.setText(translate(u'customEditDialog', u'Delete'))
        self.ClearButton.setText(translate(u'customEditDialog', u'Clear'))
        self.ThemeLabel.setText(translate(u'customEditDialog', u'Theme:'))
        self.CreditLabel.setText(translate(u'customEditDialog', u'Credits:'))
