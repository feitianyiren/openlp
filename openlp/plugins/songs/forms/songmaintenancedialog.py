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
from PyQt4 import QtCore, QtGui
from openlp.core.lib import translate

class Ui_SongMaintenanceDialog(object):
    def setupUi(self, SongMaintenanceDialog):
        SongMaintenanceDialog.setObjectName(u'SongMaintenanceDialog')
        SongMaintenanceDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        SongMaintenanceDialog.resize(486, 361)
        self.DialogLayout = QtGui.QVBoxLayout(SongMaintenanceDialog)
        self.DialogLayout.setSpacing(8)
        self.DialogLayout.setMargin(8)
        self.DialogLayout.setObjectName(u'DialogLayout')
        self.ContentWidget = QtGui.QWidget(SongMaintenanceDialog)
        self.ContentWidget.setObjectName(u'ContentWidget')
        self.ContentLayout = QtGui.QHBoxLayout(self.ContentWidget)
        self.ContentLayout.setSpacing(8)
        self.ContentLayout.setMargin(0)
        self.ContentLayout.setObjectName(u'ContentLayout')
        self.TypeListWidget = QtGui.QListWidget(self.ContentWidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.TypeListWidget.sizePolicy().hasHeightForWidth())
        self.TypeListWidget.setSizePolicy(sizePolicy)
        self.TypeListWidget.setViewMode(QtGui.QListView.IconMode)
        self.TypeListWidget.setIconSize(QtCore.QSize(112, 100));
        self.TypeListWidget.setMovement(QtGui.QListView.Static);
        self.TypeListWidget.setMaximumWidth(118);
        self.TypeListWidget.setSpacing(3);
        self.TypeListWidget.setSortingEnabled(False)
        self.TypeListWidget.setUniformItemSizes(True)
        self.TypeListWidget.setObjectName(u'TypeListWidget')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(u':/songs/author_maintenance.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtGui.QListWidgetItem(self.TypeListWidget)
        item.setIcon(icon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(u':/songs/topic_maintenance.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtGui.QListWidgetItem(self.TypeListWidget)
        item.setIcon(icon1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(u':/songs/book_maintenance.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtGui.QListWidgetItem(self.TypeListWidget)
        item.setIcon(icon2)
        self.ContentLayout.addWidget(self.TypeListWidget)
        self.TypeStackedWidget = QtGui.QStackedWidget(self.ContentWidget)
        self.TypeStackedWidget.setObjectName(u'TypeStackedWidget')
        self.AuthorsPage = QtGui.QWidget()
        self.AuthorsPage.setObjectName(u'AuthorsPage')
        self.AuthorsLayout = QtGui.QVBoxLayout(self.AuthorsPage)
        self.AuthorsLayout.setSpacing(4)
        self.AuthorsLayout.setMargin(0)
        self.AuthorsLayout.setObjectName(u'AuthorsLayout')
        self.AuthorsListWidget = QtGui.QListWidget(self.AuthorsPage)
        self.AuthorsListWidget.setObjectName(u'AuthorsListWidget')
        self.AuthorsLayout.addWidget(self.AuthorsListWidget)
        self.AuthorButtonWidget = QtGui.QWidget(self.AuthorsPage)
        self.AuthorButtonWidget.setObjectName(u'AuthorButtonWidget')
        self.AuthorButtonsLayout = QtGui.QHBoxLayout(self.AuthorButtonWidget)
        self.AuthorButtonsLayout.setSpacing(8)
        self.AuthorButtonsLayout.setMargin(0)
        self.AuthorButtonsLayout.setObjectName(u'AuthorButtonsLayout')
        spacerItem = QtGui.QSpacerItem(40, 20,
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.AuthorButtonsLayout.addItem(spacerItem)
        self.AuthorAddButton = QtGui.QPushButton(self.AuthorButtonWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(u':/songs/author_add.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AuthorAddButton.setIcon(icon3)
        self.AuthorAddButton.setObjectName(u'AuthorAddButton')
        self.AuthorButtonsLayout.addWidget(self.AuthorAddButton)
        self.AuthorEditButton = QtGui.QPushButton(self.AuthorButtonWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(u':/songs/author_edit.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AuthorEditButton.setIcon(icon4)
        self.AuthorEditButton.setObjectName(u'AuthorEditButton')
        self.AuthorButtonsLayout.addWidget(self.AuthorEditButton)
        self.AuthorDeleteButton = QtGui.QPushButton(self.AuthorButtonWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(u':/songs/author_delete.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AuthorDeleteButton.setIcon(icon5)
        self.AuthorDeleteButton.setObjectName(u'AuthorDeleteButton')
        self.AuthorButtonsLayout.addWidget(self.AuthorDeleteButton)
        self.AuthorsLayout.addWidget(self.AuthorButtonWidget)
        self.AuthorsLine = QtGui.QFrame(self.AuthorsPage)
        self.AuthorsLine.setFrameShape(QtGui.QFrame.HLine)
        self.AuthorsLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.AuthorsLine.setObjectName(u'AuthorsLine')
        self.AuthorsLayout.addWidget(self.AuthorsLine)
        self.TypeStackedWidget.addWidget(self.AuthorsPage)
        self.TopicsPage = QtGui.QWidget()
        self.TopicsPage.setObjectName(u'TopicsPage')
        self.TopicLayout = QtGui.QVBoxLayout(self.TopicsPage)
        self.TopicLayout.setSpacing(4)
        self.TopicLayout.setMargin(0)
        self.TopicLayout.setObjectName(u'TopicLayout')
        self.TopicsListWidget = QtGui.QListWidget(self.TopicsPage)
        self.TopicsListWidget.setObjectName(u'TopicsListWidget')
        self.TopicLayout.addWidget(self.TopicsListWidget)
        self.TopicButtonWidget = QtGui.QWidget(self.TopicsPage)
        self.TopicButtonWidget.setObjectName(u'TopicButtonWidget')
        self.TopicButtonLayout = QtGui.QHBoxLayout(self.TopicButtonWidget)
        self.TopicButtonLayout.setSpacing(8)
        self.TopicButtonLayout.setMargin(0)
        self.TopicButtonLayout.setObjectName(u'TopicButtonLayout')
        TopicSpacerItem = QtGui.QSpacerItem(54, 20,
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.TopicButtonLayout.addItem(TopicSpacerItem)
        self.TopicAddButton = QtGui.QPushButton(self.TopicButtonWidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(u':/songs/topic_add.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TopicAddButton.setIcon(icon6)
        self.TopicAddButton.setObjectName(u'TopicAddButton')
        self.TopicButtonLayout.addWidget(self.TopicAddButton)
        self.TopicEditButton = QtGui.QPushButton(self.TopicButtonWidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(u':/songs/topic_edit.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TopicEditButton.setIcon(icon7)
        self.TopicEditButton.setObjectName(u'TopicEditButton')
        self.TopicButtonLayout.addWidget(self.TopicEditButton)
        self.TopicDeleteButton = QtGui.QPushButton(self.TopicButtonWidget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(u':/songs/topic_delete.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TopicDeleteButton.setIcon(icon8)
        self.TopicDeleteButton.setObjectName(u'TopicDeleteButton')
        self.TopicButtonLayout.addWidget(self.TopicDeleteButton)
        self.TopicLayout.addWidget(self.TopicButtonWidget)
        self.TopicsLine = QtGui.QFrame(self.TopicsPage)
        self.TopicsLine.setFrameShape(QtGui.QFrame.HLine)
        self.TopicsLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.TopicsLine.setObjectName(u'TopicsLine')
        self.TopicLayout.addWidget(self.TopicsLine)
        self.TypeStackedWidget.addWidget(self.TopicsPage)
        self.BooksPage = QtGui.QWidget()
        self.BooksPage.setObjectName(u'BooksPage')
        self.BookLayout = QtGui.QVBoxLayout(self.BooksPage)
        self.BookLayout.setSpacing(4)
        self.BookLayout.setMargin(0)
        self.BookLayout.setObjectName(u'BookLayout')
        self.BooksListWidget = QtGui.QListWidget(self.BooksPage)
        self.BooksListWidget.setObjectName(u'BooksListWidget')
        self.BookLayout.addWidget(self.BooksListWidget)
        self.BookButtonWidget = QtGui.QWidget(self.BooksPage)
        self.BookButtonWidget.setObjectName(u'BookButtonWidget')
        self.BookButtonLayout = QtGui.QHBoxLayout(self.BookButtonWidget)
        self.BookButtonLayout.setSpacing(8)
        self.BookButtonLayout.setMargin(0)
        self.BookButtonLayout.setObjectName(u'BookButtonLayout')
        spacerItem2 = QtGui.QSpacerItem(54, 20,
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.BookButtonLayout.addItem(spacerItem2)
        self.BookAddButton = QtGui.QPushButton(self.BookButtonWidget)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(u':/songs/book_add.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BookAddButton.setIcon(icon9)
        self.BookAddButton.setObjectName(u'BookAddButton')
        self.BookButtonLayout.addWidget(self.BookAddButton)
        self.BookEditButton = QtGui.QPushButton(self.BookButtonWidget)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(u':/songs/book_edit.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BookEditButton.setIcon(icon10)
        self.BookEditButton.setObjectName(u'BookEditButton')
        self.BookButtonLayout.addWidget(self.BookEditButton)
        self.BookDeleteButton = QtGui.QPushButton(self.BookButtonWidget)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(u':/songs/book_delete.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BookDeleteButton.setIcon(icon11)
        self.BookDeleteButton.setObjectName(u'BookDeleteButton')
        self.BookButtonLayout.addWidget(self.BookDeleteButton)
        self.BookLayout.addWidget(self.BookButtonWidget)
        self.BooksLine = QtGui.QFrame(self.BooksPage)
        self.BooksLine.setFrameShape(QtGui.QFrame.HLine)
        self.BooksLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.BooksLine.setObjectName(u'BooksLine')
        self.BookLayout.addWidget(self.BooksLine)
        self.TypeStackedWidget.addWidget(self.BooksPage)
        self.ContentLayout.addWidget(self.TypeStackedWidget)
        self.DialogLayout.addWidget(self.ContentWidget)
        self.MaintenanceButtonBox = QtGui.QDialogButtonBox(SongMaintenanceDialog)
        self.MaintenanceButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.MaintenanceButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.MaintenanceButtonBox.setObjectName(u'MaintenanceButtonBox')
        self.DialogLayout.addWidget(self.MaintenanceButtonBox)

        self.retranslateUi(SongMaintenanceDialog)
        self.TypeStackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.MaintenanceButtonBox,
            QtCore.SIGNAL(u'rejected()'), SongMaintenanceDialog.accept)
        QtCore.QObject.connect(self.TypeListWidget,
            QtCore.SIGNAL(u'currentRowChanged(int)'),
            self.TypeStackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(SongMaintenanceDialog)

    def retranslateUi(self, SongMaintenanceDialog):
        SongMaintenanceDialog.setWindowTitle(
            translate(u'SongMaintenanceDialog', u'Song Maintenance'))
        self.TypeListWidget.item(0).setText(
            translate(u'SongMaintenanceDialog', u'Authors'))
        self.TypeListWidget.item(1).setText(
            translate(u'SongMaintenanceDialog', u'Topics'))
        self.TypeListWidget.item(2).setText(
            translate(u'SongMaintenanceDialog', u'Books/Hymnals'))
        self.AuthorAddButton.setText(
            translate(u'SongMaintenanceDialog', u'Add'))
        self.AuthorEditButton.setText(
            translate(u'SongMaintenanceDialog', u'Edit'))
        self.AuthorDeleteButton.setText(
            translate(u'SongMaintenanceDialog', u'Delete'))
        self.TopicAddButton.setText(
            translate(u'SongMaintenanceDialog', u'Add'))
        self.TopicEditButton.setText(
            translate(u'SongMaintenanceDialog', u'Edit'))
        self.TopicDeleteButton.setText(
            translate(u'SongMaintenanceDialog', u'Delete'))
        self.BookAddButton.setText(
            translate(u'SongMaintenanceDialog', u'Add'))
        self.BookEditButton.setText(
            translate(u'SongMaintenanceDialog', u'Edit'))
        self.BookDeleteButton.setText(
            translate(u'SongMaintenanceDialog', u'Delete'))
