# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4

###############################################################################
# OpenLP - Open Source Lyrics Projection                                      #
# --------------------------------------------------------------------------- #
# Copyright (c) 2008-2011 Raoul Snyman                                        #
# Portions copyright (c) 2008-2011 Tim Bentley, Jonathan Corwin, Michael      #
# Gorven, Scott Guerrieri, Meinert Jordan, Andreas Preikschat, Christian      #
# Richter, Philip Ridout, Maikel Stuivenberg, Martin Thompson, Jon Tibble,    #
# Carsten Tinggaard, Frode Woldsund                                           #
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

class Ui_FileRenameDialog(object):
    def setupUi(self, FileRenameDialog):
        FileRenameDialog.setObjectName(u'FileRenameDialog')
        self.dialogLayout = QtGui.QGridLayout(FileRenameDialog)
        self.dialogLayout.setObjectName(u'dialogLayout')
        self.fileNameLabel = QtGui.QLabel(FileRenameDialog)
        self.fileNameLabel.setObjectName(u'fileNameLabel')
        self.dialogLayout.addWidget(self.fileNameLabel, 0, 0)
        self.fileNameEdit = QtGui.QLineEdit(FileRenameDialog)
        self.fileNameEdit.resize(self.fileNameEdit.sizeHint().width() * 2,
            self.fileNameEdit.sizeHint().height())
        self.fileNameEdit.setObjectName(u'fileNameEdit')
        self.dialogLayout.addWidget(self.fileNameEdit, 0, 1)
        self.buttonBox = QtGui.QDialogButtonBox(FileRenameDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel |
            QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(u'buttonBox')
        self.dialogLayout.addWidget(self.buttonBox, 1, 0, 1, 2)
        self.retranslateUi(FileRenameDialog)
        self.setMaximumHeight(self.sizeHint().height())
        QtCore.QMetaObject.connectSlotsByName(FileRenameDialog)

    def retranslateUi(self, FileRenameDialog):
        self.fileNameLabel.setText(translate('OpenLP.FileRenameForm',
            'New File Name:'))
