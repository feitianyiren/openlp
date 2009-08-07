# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4
"""
OpenLP - Open Source Lyrics Projection
Copyright (c) 2008 Raoul Snyman
Portions copyright (c) 2008-2009 Martin Thompson, Tim Bentley

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

class SettingsManager(object):
    """
    Class to control the size of the UI components so they size correctly
    This class is created by the main window and then calculates the size of individual components
    """
    def __init__(self, screen):
        self.screen = screen[0]
        self.width = self.screen[u'size'].width()
        self.height = self.screen[u'size'].height()
        self.mainwindow_width = self.width * 0.8
        self.mainwindow_height = self.height * 0.8
        self.mainwindow_docbars = self.width / 3
        self.mainwindow_slidecontroller = self.width / 6