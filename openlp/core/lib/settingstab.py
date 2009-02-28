# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4
"""
OpenLP - Open Source Lyrics Projection
Copyright (c) 2008 Raoul Snyman
Portions copyright (c) 2008 Martin Thompson, Tim Bentley

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
from openlp.core.resources import *

class SettingsTab(QtGui.QWidget):
    """
    SettingsTab is a helper widget for plugins to define Tabs for the settings dialog.
    """
    def __init__(self):
        """
        Constructor to create the Steetings tab item.
        """
        QtGui.QWidget.__init__(self)
        self.TabLayout = QtGui.QVBoxLayout(self)
        self.TabLayout.setSpacing(0)
        self.TabLayout.setMargin(0)
        self.tabText = None

    def setTabText(self, text):
        self.tabText = text
        
    def add_items(self, items):
        if type(items).__name__ == "QWidget":
            self.TabLayout.addWidget(items)
        else:
            for item in items:
                self.TabLayout.addWidget(item)
