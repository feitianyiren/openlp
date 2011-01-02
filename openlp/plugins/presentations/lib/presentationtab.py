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

from openlp.core.lib import Receiver, SettingsTab, translate

class PresentationTab(SettingsTab):
    """
    PresentationsTab is the Presentations settings tab in the settings dialog.
    """
    def __init__(self, title, visible_title, controllers):
        """
        Constructor
        """
        self.controllers = controllers
        SettingsTab.__init__(self, title, visible_title)

    def setupUi(self):
        """
        Create the controls for the settings tab
        """
        self.setObjectName(u'PresentationTab')
        self.PresentationLayout = QtGui.QHBoxLayout(self)
        self.PresentationLayout.setObjectName(u'PresentationLayout')
        self.LeftWidget = QtGui.QWidget(self)
        self.LeftWidget.setObjectName(u'LeftWidget')
        self.LeftLayout = QtGui.QVBoxLayout(self.LeftWidget)
        self.LeftLayout.setMargin(0)
        self.LeftLayout.setObjectName(u'LeftLayout')
        self.ControllersGroupBox = QtGui.QGroupBox(self.LeftWidget)
        self.ControllersGroupBox.setObjectName(u'ControllersGroupBox')
        self.ControllersLayout = QtGui.QVBoxLayout(self.ControllersGroupBox)
        self.ControllersLayout.setObjectName(u'ControllersLayout')
        self.PresenterCheckboxes = {}
        for key in self.controllers:
            controller = self.controllers[key]
            checkbox = QtGui.QCheckBox(self.ControllersGroupBox)
            checkbox.setEnabled(controller.available)
            checkbox.setObjectName(controller.name + u'CheckBox')
            self.PresenterCheckboxes[controller.name] = checkbox
            self.ControllersLayout.addWidget(checkbox)
        self.LeftLayout.addWidget(self.ControllersGroupBox)
        self.AdvancedGroupBox = QtGui.QGroupBox(self.LeftWidget)
        self.AdvancedGroupBox.setObjectName(u'AdvancedGroupBox')
        self.AdvancedLayout = QtGui.QVBoxLayout(self.AdvancedGroupBox)
        self.AdvancedLayout.setObjectName(u'AdvancedLayout')
        self.OverrideAppCheckBox = QtGui.QCheckBox(self.AdvancedGroupBox)
        self.OverrideAppCheckBox.setObjectName(u'OverrideAppCheckBox')
        self.AdvancedLayout.addWidget(self.OverrideAppCheckBox)
        self.LeftLayout.addWidget(self.AdvancedGroupBox)
        self.LeftLayout.addStretch()
        self.PresentationLayout.addWidget(self.LeftWidget)
        self.RightWidget = QtGui.QWidget(self)
        self.RightWidget.setObjectName(u'RightWidget')
        self.RightLayout = QtGui.QVBoxLayout(self.RightWidget)
        self.RightLayout.setMargin(0)
        self.RightLayout.setObjectName(u'RightLayout')
        self.RightLayout.addStretch()
        self.PresentationLayout.addWidget(self.RightWidget)

    def retranslateUi(self):
        """
        Make any translation changes
        """
        self.ControllersGroupBox.setTitle(
            translate('PresentationPlugin.PresentationTab',
            'Available Controllers'))
        for key in self.controllers:
            controller = self.controllers[key]
            checkbox = self.PresenterCheckboxes[controller.name]
            checkbox.setText(controller.name)
        self.AdvancedGroupBox.setTitle(
            translate('PresentationPlugin.PresentationTab',
            'Advanced'))
        self.OverrideAppCheckBox.setText(
            translate('PresentationPlugin.PresentationTab',
            'Allow presentation application to be overriden'))

    def resizeEvent(self, event=None):
        """
        Resize the sides in two equal halves if the layout allows this.
        """
        if event:
            SettingsTab.resizeEvent(self, event)
        width = self.width() - self.PresentationLayout.spacing() - \
            self.PresentationLayout.contentsMargins().left() - \
            self.PresentationLayout.contentsMargins().right()
        left_width = min(width - self.RightWidget.minimumSizeHint().width(),
            width / 2)
        left_width = max(left_width, self.LeftWidget.minimumSizeHint().width())
        self.LeftWidget.setMinimumWidth(left_width)

    def load(self):
        """
        Load the settings.
        """
        for key in self.controllers:
            controller = self.controllers[key]
            if controller.available:
                checkbox = self.PresenterCheckboxes[controller.name]
                checkbox.setChecked(QtCore.QSettings().value(
                    self.settingsSection + u'/' + controller.name,
                    QtCore.QVariant(QtCore.Qt.Checked)).toInt()[0])
        self.OverrideAppCheckBox.setChecked(QtCore.QSettings().value(
            self.settingsSection + u'/override app',
            QtCore.QVariant(QtCore.Qt.Unchecked)).toInt()[0])

    def save(self):
        """
        Save the settings.
        """
        changed = False
        for key in self.controllers:
            controller = self.controllers[key]
            checkbox = self.PresenterCheckboxes[controller.name]
            setting_key = self.settingsSection + u'/' + controller.name
            if QtCore.QSettings().value(setting_key) != checkbox.checkState():
                changed = True
                QtCore.QSettings().setValue(setting_key,
                    QtCore.QVariant(checkbox.checkState()))
                if checkbox.checkState() == QtCore.Qt.Checked:
                    controller.start_process()
                else:
                    controller.kill()
        setting_key = self.settingsSection + u'/override app'
        if QtCore.QSettings().value(setting_key) != \
            self.OverrideAppCheckBox.checkState():
            QtCore.QSettings().setValue(setting_key,
                QtCore.QVariant(self.OverrideAppCheckBox.checkState()))
            changed = True
        if changed:
            Receiver.send_message(u'mediaitem_presentation_rebuild')
