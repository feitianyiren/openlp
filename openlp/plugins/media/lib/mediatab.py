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

from openlp.core.lib import SettingsTab, translate, Receiver

class MediaTab(SettingsTab):
    """
    MediaTab is the Media settings tab in the settings dialog.
    """
    def __init__(self, title):
        SettingsTab.__init__(self, title)

    def setupUi(self):
        self.setObjectName(u'MediaTab')
        self.tabTitleVisible = translate('MediaPlugin.MediaTab', 'Media')
        self.mediaLayout = QtGui.QFormLayout(self)
        self.mediaLayout.setSpacing(8)
        self.mediaLayout.setMargin(8)
        self.mediaLayout.setObjectName(u'mediaLayout')
        self.mediaModeGroupBox = QtGui.QGroupBox(self)
        self.mediaModeGroupBox.setObjectName(u'mediaModeGroupBox')
        self.mediaModeLayout = QtGui.QVBoxLayout(self.mediaModeGroupBox)
        self.mediaModeLayout.setSpacing(8)
        self.mediaModeLayout.setMargin(8)
        self.mediaModeLayout.setObjectName(u'mediaModeLayout')
        self.usePhononCheckBox = QtGui.QCheckBox(self.mediaModeGroupBox)
        self.usePhononCheckBox.setObjectName(u'usePhononCheckBox')
        self.mediaModeLayout.addWidget(self.usePhononCheckBox)
        self.mediaLayout.setWidget(
            0, QtGui.QFormLayout.LabelRole, self.mediaModeGroupBox)
        QtCore.QObject.connect(self.usePhononCheckBox,
            QtCore.SIGNAL(u'stateChanged(int)'),
            self.onUsePhononCheckBoxChanged)

    def retranslateUi(self):
        self.mediaModeGroupBox.setTitle(translate('MediaPlugin.MediaTab',
            'Media Display'))
        self.usePhononCheckBox.setText(
            translate('MediaPlugin.MediaTab', 'Use Phonon for video playback'))

    def onUsePhononCheckBoxChanged(self, check_state):
        self.usePhonon = (check_state == QtCore.Qt.Checked)
        self.usePhononChanged = True

    def load(self):
        self.usePhonon = QtCore.QSettings().value(
            self.settingsSection + u'/use phonon',
            QtCore.QVariant(True)).toBool()
        self.usePhononCheckBox.setChecked(self.usePhonon)

    def save(self):
        oldUsePhonon = QtCore.QSettings().value(
            u'media/use phonon', QtCore.QVariant(True)).toBool()
        if oldUsePhonon != self.usePhonon:
            QtCore.QSettings().setValue(self.settingsSection + u'/use phonon',
                QtCore.QVariant(self.usePhonon))
            Receiver.send_message(u'config_screen_changed')