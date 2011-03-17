# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4

###############################################################################
# OpenLP - Open Source Lyrics Projection                                      #
# --------------------------------------------------------------------------- #
# Copyright (c) 2008-2011 Raoul Snyman                                        #
# Portions copyright (c) 2008-2011 Tim Bentley, Jonathan Corwin, Michael      #
# Gorven, Scott Guerrieri, Meinert Jordan, Armin Köhler, Andreas Preikschat,  #
# Christian Richter, Philip Ridout, Maikel Stuivenberg, Martin Thompson, Jon  #
# Tibble, Carsten Tinggaard, Frode Woldsund                                   #
# --------------------------------------------------------------------------- #
# This program is free software; you can redistribute it and/or modify it     #
# under the terms of the GNU General Public License as published by the Free  #
# Software Foundation; version 2 of the License.                              #
#                                                                             #
# This program is distributed in the hope that it will be useful, but WITHOUT #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or       #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for    #
# more details.                                                               #
#                                                                             #
# You should have received a copy of the GNU General Public License along     #
# with this program; if not, write to the Free Software Foundation, Inc., 59  #
# Temple Place, Suite 330, Boston, MA 02111-1307 USA                          #
###############################################################################

from PyQt4 import QtCore, QtGui

from openlp.core.lib import translate
from openlp.core.lib.ui import create_accept_reject_button_box

class Ui_BibleImportRequest(object):
    def setupUi(self, bibleImportRequest):
        bibleImportRequest.setObjectName("BibleImportRequest")
        bibleImportRequest.resize(400, 175)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, 
            QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bibleImportRequest.sizePolicy()
            .hasHeightForWidth())
        bibleImportRequest.setSizePolicy(sizePolicy)
        self.widget = QtGui.QWidget(bibleImportRequest)
        self.widget.setGeometry(QtCore.QRect(10, 15, 381, 151))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headlineLabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.headlineLabel.setFont(font)
        self.headlineLabel.setObjectName("HeadlineLabel")
        self.verticalLayout.addWidget(self.headlineLabel)
        self.infoLabel = QtGui.QLabel(self.widget)
        self.infoLabel.setObjectName("InfoLabel")
        self.verticalLayout.addWidget(self.infoLabel)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.requestLabel = QtGui.QLabel(self.widget)
        self.requestLabel.setObjectName("RequestLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, 
            self.requestLabel)
        self.requestComboBox = QtGui.QComboBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, 
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requestComboBox.sizePolicy()
            .hasHeightForWidth())
        self.requestComboBox.setSizePolicy(sizePolicy)
        self.requestComboBox.setObjectName("RequestComboBox")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, 
            self.requestComboBox)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, 
            QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout.addWidget(
            create_accept_reject_button_box(bibleImportRequest))
        self.retranslateUi(bibleImportRequest)
        QtCore.QMetaObject.connectSlotsByName(bibleImportRequest)

    def retranslateUi(self, bibleImportRequest):
        bibleImportRequest.setWindowTitle(
            translate("BiblesPlugin.bibleImportRequest", "Dialog"))
        self.headlineLabel.setText(
            translate("BiblesPlugin.bibleImportRequest", "Choose Book:"))
        self.infoLabel.setText(translate("BiblesPlugin.bibleImportRequest", 
            "The following books cannot be clearly attributed. \n"
            "Please choose the book it is."))
        self.requestLabel.setText(translate("BiblesPlugin.bibleImportRequest", 
            "Book:"))
