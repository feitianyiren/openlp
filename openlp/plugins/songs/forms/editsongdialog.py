# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/raoul/Projects/openlp/songmaintenance/resources/forms/editsongdialog.ui'
#
# Created: Mon Jul 27 22:18:20 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditSongDialog(object):
    def setupUi(self, EditSongDialog):
        EditSongDialog.setObjectName("EditSongDialog")
        EditSongDialog.resize(645, 417)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/openlp.org-icon-32.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditSongDialog.setWindowIcon(icon)
        EditSongDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(EditSongDialog)
        self.verticalLayout.setMargin(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SongTabWidget = QtGui.QTabWidget(EditSongDialog)
        self.SongTabWidget.setObjectName("SongTabWidget")
        self.LyricsTab = QtGui.QWidget()
        self.LyricsTab.setObjectName("LyricsTab")
        self.LyricsTabLayout = QtGui.QGridLayout(self.LyricsTab)
        self.LyricsTabLayout.setMargin(8)
        self.LyricsTabLayout.setSpacing(8)
        self.LyricsTabLayout.setObjectName("LyricsTabLayout")
        self.TitleLabel = QtGui.QLabel(self.LyricsTab)
        self.TitleLabel.setObjectName("TitleLabel")
        self.LyricsTabLayout.addWidget(self.TitleLabel, 0, 0, 1, 1)
        self.TitleEditItem = QtGui.QLineEdit(self.LyricsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleEditItem.sizePolicy().hasHeightForWidth())
        self.TitleEditItem.setSizePolicy(sizePolicy)
        self.TitleEditItem.setObjectName("TitleEditItem")
        self.LyricsTabLayout.addWidget(self.TitleEditItem, 0, 1, 1, 2)
        self.AlternativeTitleLabel = QtGui.QLabel(self.LyricsTab)
        self.AlternativeTitleLabel.setObjectName("AlternativeTitleLabel")
        self.LyricsTabLayout.addWidget(self.AlternativeTitleLabel, 1, 0, 1, 1)
        self.AlternativeEdit = QtGui.QLineEdit(self.LyricsTab)
        self.AlternativeEdit.setObjectName("AlternativeEdit")
        self.LyricsTabLayout.addWidget(self.AlternativeEdit, 1, 1, 1, 2)
        self.LyricsLabel = QtGui.QLabel(self.LyricsTab)
        self.LyricsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.LyricsLabel.setObjectName("LyricsLabel")
        self.LyricsTabLayout.addWidget(self.LyricsLabel, 2, 0, 1, 1)
        self.VerseListWidget = QtGui.QListWidget(self.LyricsTab)
        self.VerseListWidget.setSpacing(2)
        self.VerseListWidget.setAlternatingRowColors(True)
        self.VerseListWidget.setObjectName("VerseListWidget")
        self.LyricsTabLayout.addWidget(self.VerseListWidget, 2, 1, 1, 1)
        self.VerseOrderLabel = QtGui.QLabel(self.LyricsTab)
        self.VerseOrderLabel.setObjectName("VerseOrderLabel")
        self.LyricsTabLayout.addWidget(self.VerseOrderLabel, 4, 0, 1, 1)
        self.VerseOrderEdit = QtGui.QLineEdit(self.LyricsTab)
        self.VerseOrderEdit.setObjectName("VerseOrderEdit")
        self.LyricsTabLayout.addWidget(self.VerseOrderEdit, 4, 1, 1, 2)
        self.VerseButtonWidget = QtGui.QWidget(self.LyricsTab)
        self.VerseButtonWidget.setObjectName("VerseButtonWidget")
        self.VerseButtonsLayout = QtGui.QVBoxLayout(self.VerseButtonWidget)
        self.VerseButtonsLayout.setSpacing(8)
        self.VerseButtonsLayout.setMargin(0)
        self.VerseButtonsLayout.setObjectName("VerseButtonsLayout")
        self.VerseAddButton = QtGui.QPushButton(self.VerseButtonWidget)
        self.VerseAddButton.setObjectName("VerseAddButton")
        self.VerseButtonsLayout.addWidget(self.VerseAddButton)
        self.VerseEditButton = QtGui.QPushButton(self.VerseButtonWidget)
        self.VerseEditButton.setObjectName("VerseEditButton")
        self.VerseButtonsLayout.addWidget(self.VerseEditButton)
        self.VerseEditAllButton = QtGui.QPushButton(self.VerseButtonWidget)
        self.VerseEditAllButton.setObjectName("VerseEditAllButton")
        self.VerseButtonsLayout.addWidget(self.VerseEditAllButton)
        self.VerseDeleteButton = QtGui.QPushButton(self.VerseButtonWidget)
        self.VerseDeleteButton.setObjectName("VerseDeleteButton")
        self.VerseButtonsLayout.addWidget(self.VerseDeleteButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.VerseButtonsLayout.addItem(spacerItem)
        self.LyricsTabLayout.addWidget(self.VerseButtonWidget, 2, 2, 1, 1)
        self.SongTabWidget.addTab(self.LyricsTab, "")
        self.AuthorsTab = QtGui.QWidget()
        self.AuthorsTab.setObjectName("AuthorsTab")
        self.AuthorsTabLayout = QtGui.QHBoxLayout(self.AuthorsTab)
        self.AuthorsTabLayout.setSpacing(8)
        self.AuthorsTabLayout.setMargin(8)
        self.AuthorsTabLayout.setObjectName("AuthorsTabLayout")
        self.AuthorsMaintenanceWidget = QtGui.QWidget(self.AuthorsTab)
        self.AuthorsMaintenanceWidget.setObjectName("AuthorsMaintenanceWidget")
        self.AuthorsMaintenanceLayout = QtGui.QVBoxLayout(self.AuthorsMaintenanceWidget)
        self.AuthorsMaintenanceLayout.setSpacing(8)
        self.AuthorsMaintenanceLayout.setMargin(0)
        self.AuthorsMaintenanceLayout.setObjectName("AuthorsMaintenanceLayout")
        self.AuthorsGroupBox = QtGui.QGroupBox(self.AuthorsMaintenanceWidget)
        self.AuthorsGroupBox.setObjectName("AuthorsGroupBox")
        self.AuthorsLayout = QtGui.QVBoxLayout(self.AuthorsGroupBox)
        self.AuthorsLayout.setSpacing(8)
        self.AuthorsLayout.setMargin(8)
        self.AuthorsLayout.setObjectName("AuthorsLayout")
        self.AuthorAddWidget = QtGui.QWidget(self.AuthorsGroupBox)
        self.AuthorAddWidget.setObjectName("AuthorAddWidget")
        self.AuthorAddLayout = QtGui.QHBoxLayout(self.AuthorAddWidget)
        self.AuthorAddLayout.setSpacing(8)
        self.AuthorAddLayout.setMargin(0)
        self.AuthorAddLayout.setObjectName("AuthorAddLayout")
        self.AuthorsSelectionComboItem = QtGui.QComboBox(self.AuthorAddWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AuthorsSelectionComboItem.sizePolicy().hasHeightForWidth())
        self.AuthorsSelectionComboItem.setSizePolicy(sizePolicy)
        self.AuthorsSelectionComboItem.setEditable(False)
        self.AuthorsSelectionComboItem.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.AuthorsSelectionComboItem.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.AuthorsSelectionComboItem.setMinimumContentsLength(8)
        self.AuthorsSelectionComboItem.setObjectName("AuthorsSelectionComboItem")
        self.AuthorAddLayout.addWidget(self.AuthorsSelectionComboItem)
        self.AuthorAddButton = QtGui.QPushButton(self.AuthorAddWidget)
        self.AuthorAddButton.setMaximumSize(QtCore.QSize(110, 16777215))
        self.AuthorAddButton.setObjectName("AuthorAddButton")
        self.AuthorAddLayout.addWidget(self.AuthorAddButton)
        self.AuthorsLayout.addWidget(self.AuthorAddWidget)
        self.AuthorsListView = QtGui.QListWidget(self.AuthorsGroupBox)
        self.AuthorsListView.setAlternatingRowColors(True)
        self.AuthorsListView.setObjectName("AuthorsListView")
        self.AuthorsLayout.addWidget(self.AuthorsListView)
        self.AuthorRemoveWidget = QtGui.QWidget(self.AuthorsGroupBox)
        self.AuthorRemoveWidget.setObjectName("AuthorRemoveWidget")
        self.AuthorRemoveLayout = QtGui.QHBoxLayout(self.AuthorRemoveWidget)
        self.AuthorRemoveLayout.setSpacing(8)
        self.AuthorRemoveLayout.setMargin(0)
        self.AuthorRemoveLayout.setObjectName("AuthorRemoveLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.AuthorRemoveLayout.addItem(spacerItem1)
        self.AuthorRemoveButton = QtGui.QPushButton(self.AuthorRemoveWidget)
        self.AuthorRemoveButton.setObjectName("AuthorRemoveButton")
        self.AuthorRemoveLayout.addWidget(self.AuthorRemoveButton)
        self.AuthorsLayout.addWidget(self.AuthorRemoveWidget)
        self.AuthorsMaintenanceLayout.addWidget(self.AuthorsGroupBox)
        self.MaintenanceWidget = QtGui.QWidget(self.AuthorsMaintenanceWidget)
        self.MaintenanceWidget.setObjectName("MaintenanceWidget")
        self.MaintenanceLayout = QtGui.QHBoxLayout(self.MaintenanceWidget)
        self.MaintenanceLayout.setSpacing(0)
        self.MaintenanceLayout.setMargin(0)
        self.MaintenanceLayout.setObjectName("MaintenanceLayout")
        self.MaintenanceButton = QtGui.QPushButton(self.MaintenanceWidget)
        self.MaintenanceButton.setObjectName("MaintenanceButton")
        self.MaintenanceLayout.addWidget(self.MaintenanceButton)
        spacerItem2 = QtGui.QSpacerItem(66, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.MaintenanceLayout.addItem(spacerItem2)
        self.AuthorsMaintenanceLayout.addWidget(self.MaintenanceWidget)
        self.AuthorsTabLayout.addWidget(self.AuthorsMaintenanceWidget)
        self.TopicBookWidget = QtGui.QWidget(self.AuthorsTab)
        self.TopicBookWidget.setObjectName("TopicBookWidget")
        self.TopicBookLayout = QtGui.QVBoxLayout(self.TopicBookWidget)
        self.TopicBookLayout.setSpacing(8)
        self.TopicBookLayout.setMargin(0)
        self.TopicBookLayout.setObjectName("TopicBookLayout")
        self.TopicGroupBox = QtGui.QGroupBox(self.TopicBookWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TopicGroupBox.sizePolicy().hasHeightForWidth())
        self.TopicGroupBox.setSizePolicy(sizePolicy)
        self.TopicGroupBox.setObjectName("TopicGroupBox")
        self.TopicLayout = QtGui.QVBoxLayout(self.TopicGroupBox)
        self.TopicLayout.setSpacing(8)
        self.TopicLayout.setMargin(8)
        self.TopicLayout.setObjectName("TopicLayout")
        self.TopicAddWidget = QtGui.QWidget(self.TopicGroupBox)
        self.TopicAddWidget.setObjectName("TopicAddWidget")
        self.TopicAddLayout = QtGui.QHBoxLayout(self.TopicAddWidget)
        self.TopicAddLayout.setSpacing(8)
        self.TopicAddLayout.setMargin(0)
        self.TopicAddLayout.setObjectName("TopicAddLayout")
        self.SongTopicCombo = QtGui.QComboBox(self.TopicAddWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SongTopicCombo.sizePolicy().hasHeightForWidth())
        self.SongTopicCombo.setSizePolicy(sizePolicy)
        self.SongTopicCombo.setObjectName("SongTopicCombo")
        self.TopicAddLayout.addWidget(self.SongTopicCombo)
        self.TopicAddButton = QtGui.QPushButton(self.TopicAddWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TopicAddButton.sizePolicy().hasHeightForWidth())
        self.TopicAddButton.setSizePolicy(sizePolicy)
        self.TopicAddButton.setObjectName("TopicAddButton")
        self.TopicAddLayout.addWidget(self.TopicAddButton)
        self.TopicLayout.addWidget(self.TopicAddWidget)
        self.TopicsListView = QtGui.QListWidget(self.TopicGroupBox)
        self.TopicsListView.setAlternatingRowColors(True)
        self.TopicsListView.setObjectName("TopicsListView")
        self.TopicLayout.addWidget(self.TopicsListView)
        self.TopicRemoveWidget = QtGui.QWidget(self.TopicGroupBox)
        self.TopicRemoveWidget.setObjectName("TopicRemoveWidget")
        self.TopicRemoveLayout = QtGui.QHBoxLayout(self.TopicRemoveWidget)
        self.TopicRemoveLayout.setSpacing(8)
        self.TopicRemoveLayout.setMargin(0)
        self.TopicRemoveLayout.setObjectName("TopicRemoveLayout")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.TopicRemoveLayout.addItem(spacerItem3)
        self.TopicRemoveButton = QtGui.QPushButton(self.TopicRemoveWidget)
        self.TopicRemoveButton.setObjectName("TopicRemoveButton")
        self.TopicRemoveLayout.addWidget(self.TopicRemoveButton)
        self.TopicLayout.addWidget(self.TopicRemoveWidget)
        self.TopicBookLayout.addWidget(self.TopicGroupBox)
        self.SongBookGroup = QtGui.QGroupBox(self.TopicBookWidget)
        self.SongBookGroup.setObjectName("SongBookGroup")
        self.SongbookLayout = QtGui.QGridLayout(self.SongBookGroup)
        self.SongbookLayout.setMargin(8)
        self.SongbookLayout.setSpacing(8)
        self.SongbookLayout.setObjectName("SongbookLayout")
        self.SongbookCombo = QtGui.QComboBox(self.SongBookGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SongbookCombo.sizePolicy().hasHeightForWidth())
        self.SongbookCombo.setSizePolicy(sizePolicy)
        self.SongbookCombo.setObjectName("SongbookCombo")
        self.SongbookLayout.addWidget(self.SongbookCombo, 0, 0, 1, 1)
        self.TopicBookLayout.addWidget(self.SongBookGroup)
        self.AuthorsTabLayout.addWidget(self.TopicBookWidget)
        self.SongTabWidget.addTab(self.AuthorsTab, "")
        self.ThemeTab = QtGui.QWidget()
        self.ThemeTab.setObjectName("ThemeTab")
        self.ThemeTabLayout = QtGui.QVBoxLayout(self.ThemeTab)
        self.ThemeTabLayout.setSpacing(8)
        self.ThemeTabLayout.setMargin(8)
        self.ThemeTabLayout.setObjectName("ThemeTabLayout")
        self.ThemeCopyCommentsWidget = QtGui.QWidget(self.ThemeTab)
        self.ThemeCopyCommentsWidget.setObjectName("ThemeCopyCommentsWidget")
        self.ThemeCopyCommentsLayout = QtGui.QHBoxLayout(self.ThemeCopyCommentsWidget)
        self.ThemeCopyCommentsLayout.setSpacing(8)
        self.ThemeCopyCommentsLayout.setMargin(0)
        self.ThemeCopyCommentsLayout.setObjectName("ThemeCopyCommentsLayout")
        self.TextWidget = QtGui.QWidget(self.ThemeCopyCommentsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextWidget.sizePolicy().hasHeightForWidth())
        self.TextWidget.setSizePolicy(sizePolicy)
        self.TextWidget.setObjectName("TextWidget")
        self.DetailsLayout = QtGui.QVBoxLayout(self.TextWidget)
        self.DetailsLayout.setSpacing(8)
        self.DetailsLayout.setMargin(0)
        self.DetailsLayout.setObjectName("DetailsLayout")
        self.ThemeGroupBox = QtGui.QGroupBox(self.TextWidget)
        self.ThemeGroupBox.setObjectName("ThemeGroupBox")
        self.ThemeLayout = QtGui.QHBoxLayout(self.ThemeGroupBox)
        self.ThemeLayout.setSpacing(8)
        self.ThemeLayout.setMargin(8)
        self.ThemeLayout.setObjectName("ThemeLayout")
        self.ThemeSelectionComboItem = QtGui.QComboBox(self.ThemeGroupBox)
        self.ThemeSelectionComboItem.setObjectName("ThemeSelectionComboItem")
        self.ThemeLayout.addWidget(self.ThemeSelectionComboItem)
        self.ThemeAddButton = QtGui.QPushButton(self.ThemeGroupBox)
        self.ThemeAddButton.setMaximumSize(QtCore.QSize(110, 16777215))
        self.ThemeAddButton.setObjectName("ThemeAddButton")
        self.ThemeLayout.addWidget(self.ThemeAddButton)
        self.DetailsLayout.addWidget(self.ThemeGroupBox)
        self.CopyrightGroupBox = QtGui.QGroupBox(self.TextWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CopyrightGroupBox.sizePolicy().hasHeightForWidth())
        self.CopyrightGroupBox.setSizePolicy(sizePolicy)
        self.CopyrightGroupBox.setObjectName("CopyrightGroupBox")
        self.CopyrightLayout = QtGui.QVBoxLayout(self.CopyrightGroupBox)
        self.CopyrightLayout.setSpacing(8)
        self.CopyrightLayout.setMargin(8)
        self.CopyrightLayout.setObjectName("CopyrightLayout")
        self.CopyrightWidget = QtGui.QWidget(self.CopyrightGroupBox)
        self.CopyrightWidget.setObjectName("CopyrightWidget")
        self.CopyLayout = QtGui.QHBoxLayout(self.CopyrightWidget)
        self.CopyLayout.setSpacing(8)
        self.CopyLayout.setMargin(0)
        self.CopyLayout.setObjectName("CopyLayout")
        self.CopyrightEditItem = QtGui.QLineEdit(self.CopyrightWidget)
        self.CopyrightEditItem.setObjectName("CopyrightEditItem")
        self.CopyLayout.addWidget(self.CopyrightEditItem)
        self.CopyrightInsertButton = QtGui.QPushButton(self.CopyrightWidget)
        self.CopyrightInsertButton.setMaximumSize(QtCore.QSize(29, 16777215))
        self.CopyrightInsertButton.setObjectName("CopyrightInsertButton")
        self.CopyLayout.addWidget(self.CopyrightInsertButton)
        self.CopyrightLayout.addWidget(self.CopyrightWidget)
        self.CcliWidget = QtGui.QWidget(self.CopyrightGroupBox)
        self.CcliWidget.setObjectName("CcliWidget")
        self.CCLILayout = QtGui.QHBoxLayout(self.CcliWidget)
        self.CCLILayout.setSpacing(8)
        self.CCLILayout.setMargin(0)
        self.CCLILayout.setObjectName("CCLILayout")
        self.CCLILabel = QtGui.QLabel(self.CcliWidget)
        self.CCLILabel.setObjectName("CCLILabel")
        self.CCLILayout.addWidget(self.CCLILabel)
        self.CCLNumberEdit = QtGui.QLineEdit(self.CcliWidget)
        self.CCLNumberEdit.setObjectName("CCLNumberEdit")
        self.CCLILayout.addWidget(self.CCLNumberEdit)
        self.CopyrightLayout.addWidget(self.CcliWidget)
        self.DetailsLayout.addWidget(self.CopyrightGroupBox)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.DetailsLayout.addItem(spacerItem4)
        self.ThemeCopyCommentsLayout.addWidget(self.TextWidget)
        self.CommentsGroupBox = QtGui.QGroupBox(self.ThemeCopyCommentsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CommentsGroupBox.sizePolicy().hasHeightForWidth())
        self.CommentsGroupBox.setSizePolicy(sizePolicy)
        self.CommentsGroupBox.setObjectName("CommentsGroupBox")
        self.CommentsLayout = QtGui.QVBoxLayout(self.CommentsGroupBox)
        self.CommentsLayout.setSpacing(0)
        self.CommentsLayout.setMargin(8)
        self.CommentsLayout.setObjectName("CommentsLayout")
        self.CommentsEdit = QtGui.QTextEdit(self.CommentsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CommentsEdit.sizePolicy().hasHeightForWidth())
        self.CommentsEdit.setSizePolicy(sizePolicy)
        self.CommentsEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CommentsEdit.setObjectName("CommentsEdit")
        self.CommentsLayout.addWidget(self.CommentsEdit)
        self.ThemeCopyCommentsLayout.addWidget(self.CommentsGroupBox)
        self.ThemeTabLayout.addWidget(self.ThemeCopyCommentsWidget)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.ThemeTabLayout.addItem(spacerItem5)
        self.SongTabWidget.addTab(self.ThemeTab, "")
        self.verticalLayout.addWidget(self.SongTabWidget)
        self.ButtonBox = QtGui.QDialogButtonBox(EditSongDialog)
        self.ButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.ButtonBox.setObjectName("ButtonBox")
        self.verticalLayout.addWidget(self.ButtonBox)

        self.retranslateUi(EditSongDialog)
        self.SongTabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.ButtonBox, QtCore.SIGNAL("rejected()"), EditSongDialog.close)
        QtCore.QObject.connect(self.ButtonBox, QtCore.SIGNAL("accepted()"), EditSongDialog.close)
        QtCore.QMetaObject.connectSlotsByName(EditSongDialog)
        EditSongDialog.setTabOrder(self.SongTabWidget, self.TitleEditItem)
        EditSongDialog.setTabOrder(self.TitleEditItem, self.AlternativeEdit)
        EditSongDialog.setTabOrder(self.AlternativeEdit, self.VerseListWidget)
        EditSongDialog.setTabOrder(self.VerseListWidget, self.VerseAddButton)
        EditSongDialog.setTabOrder(self.VerseAddButton, self.VerseEditButton)
        EditSongDialog.setTabOrder(self.VerseEditButton, self.VerseEditAllButton)
        EditSongDialog.setTabOrder(self.VerseEditAllButton, self.VerseDeleteButton)
        EditSongDialog.setTabOrder(self.VerseDeleteButton, self.VerseOrderEdit)
        EditSongDialog.setTabOrder(self.VerseOrderEdit, self.AuthorsSelectionComboItem)
        EditSongDialog.setTabOrder(self.AuthorsSelectionComboItem, self.AuthorAddButton)
        EditSongDialog.setTabOrder(self.AuthorAddButton, self.AuthorsListView)
        EditSongDialog.setTabOrder(self.AuthorsListView, self.AuthorRemoveButton)
        EditSongDialog.setTabOrder(self.AuthorRemoveButton, self.MaintenanceButton)
        EditSongDialog.setTabOrder(self.MaintenanceButton, self.SongTopicCombo)
        EditSongDialog.setTabOrder(self.SongTopicCombo, self.TopicAddButton)
        EditSongDialog.setTabOrder(self.TopicAddButton, self.TopicsListView)
        EditSongDialog.setTabOrder(self.TopicsListView, self.TopicRemoveButton)
        EditSongDialog.setTabOrder(self.TopicRemoveButton, self.SongbookCombo)
        EditSongDialog.setTabOrder(self.SongbookCombo, self.ThemeSelectionComboItem)
        EditSongDialog.setTabOrder(self.ThemeSelectionComboItem, self.ThemeAddButton)
        EditSongDialog.setTabOrder(self.ThemeAddButton, self.CopyrightEditItem)
        EditSongDialog.setTabOrder(self.CopyrightEditItem, self.CopyrightInsertButton)
        EditSongDialog.setTabOrder(self.CopyrightInsertButton, self.CCLNumberEdit)
        EditSongDialog.setTabOrder(self.CCLNumberEdit, self.CommentsEdit)
        EditSongDialog.setTabOrder(self.CommentsEdit, self.ButtonBox)

    def retranslateUi(self, EditSongDialog):
        EditSongDialog.setWindowTitle(QtGui.QApplication.translate("EditSongDialog", "Song Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.TitleLabel.setText(QtGui.QApplication.translate("EditSongDialog", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.AlternativeTitleLabel.setText(QtGui.QApplication.translate("EditSongDialog", "Alternative Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.LyricsLabel.setText(QtGui.QApplication.translate("EditSongDialog", "Lyrics:", None, QtGui.QApplication.UnicodeUTF8))
        self.VerseOrderLabel.setText(QtGui.QApplication.translate("EditSongDialog", "Verse Order:", None, QtGui.QApplication.UnicodeUTF8))
        self.VerseAddButton.setText(QtGui.QApplication.translate("EditSongDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.VerseEditButton.setText(QtGui.QApplication.translate("EditSongDialog", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.VerseEditAllButton.setText(QtGui.QApplication.translate("EditSongDialog", "Edit All", None, QtGui.QApplication.UnicodeUTF8))
        self.VerseDeleteButton.setText(QtGui.QApplication.translate("EditSongDialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.SongTabWidget.setTabText(self.SongTabWidget.indexOf(self.LyricsTab), QtGui.QApplication.translate("EditSongDialog", "Title && Lyrics", None, QtGui.QApplication.UnicodeUTF8))
        self.AuthorsGroupBox.setTitle(QtGui.QApplication.translate("EditSongDialog", "Authors", None, QtGui.QApplication.UnicodeUTF8))
        self.AuthorAddButton.setText(QtGui.QApplication.translate("EditSongDialog", "&Add to Song", None, QtGui.QApplication.UnicodeUTF8))
        self.AuthorRemoveButton.setText(QtGui.QApplication.translate("EditSongDialog", "&Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.MaintenanceButton.setText(QtGui.QApplication.translate("EditSongDialog", "&Manage Authors, Topics, Books", None, QtGui.QApplication.UnicodeUTF8))
        self.TopicGroupBox.setTitle(QtGui.QApplication.translate("EditSongDialog", "Topic", None, QtGui.QApplication.UnicodeUTF8))
        self.TopicAddButton.setText(QtGui.QApplication.translate("EditSongDialog", "A&dd to Song", None, QtGui.QApplication.UnicodeUTF8))
        self.TopicRemoveButton.setText(QtGui.QApplication.translate("EditSongDialog", "R&emove", None, QtGui.QApplication.UnicodeUTF8))
        self.SongBookGroup.setTitle(QtGui.QApplication.translate("EditSongDialog", "Song Book", None, QtGui.QApplication.UnicodeUTF8))
        self.SongTabWidget.setTabText(self.SongTabWidget.indexOf(self.AuthorsTab), QtGui.QApplication.translate("EditSongDialog", "Authors, Topics && Book", None, QtGui.QApplication.UnicodeUTF8))
        self.ThemeGroupBox.setTitle(QtGui.QApplication.translate("EditSongDialog", "Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.ThemeAddButton.setText(QtGui.QApplication.translate("EditSongDialog", "Add a Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.CopyrightGroupBox.setTitle(QtGui.QApplication.translate("EditSongDialog", "Copyright Information", None, QtGui.QApplication.UnicodeUTF8))
        self.CopyrightInsertButton.setText(QtGui.QApplication.translate("EditSongDialog", "©", None, QtGui.QApplication.UnicodeUTF8))
        self.CCLILabel.setText(QtGui.QApplication.translate("EditSongDialog", "CCLI Number:", None, QtGui.QApplication.UnicodeUTF8))
        self.CommentsGroupBox.setTitle(QtGui.QApplication.translate("EditSongDialog", "Comments", None, QtGui.QApplication.UnicodeUTF8))
        self.SongTabWidget.setTabText(self.SongTabWidget.indexOf(self.ThemeTab), QtGui.QApplication.translate("EditSongDialog", "Theme, Copyright Info && Comments", None, QtGui.QApplication.UnicodeUTF8))

