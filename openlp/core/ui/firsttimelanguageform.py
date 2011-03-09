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

from PyQt4 import QtGui

from firsttimelanguagedialog import Ui_FirstTimeLanguageDialog

from openlp.core.lib import translate
from openlp.core.utils import LanguageManager

class FirstTimeLanguageForm(QtGui.QDialog, Ui_FirstTimeLanguageDialog):
    """
    The exception dialog
    """
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.qmList = LanguageManager.get_qm_list()
        self.LanguageComboBox.addItem(u'Automatic')
        for key in sorted(self.qmList.keys()):
            self.LanguageComboBox.addItem(key)

    def exec_(self):
        """
        Run the Dialog with correct heading.
        """
        return QtGui.QDialog.exec_(self)

    def accept(self):
        # It's the first row so must be Automatic
        if self.LanguageComboBox.currentIndex() == 0:
            LanguageManager.auto_language = True
            LanguageManager.set_language(False, False)
        else:
            LanguageManager.auto_language = False
            action = QtGui.QAction(None)
            action.setObjectName(unicode(self.LanguageComboBox.currentText()))
            LanguageManager.set_language(action, False)
        return QtGui.QDialog.accept(self)

    def reject(self):
        LanguageManager.auto_language = True
        LanguageManager.set_language(False, False)
        return QtGui.QDialog.reject(self)