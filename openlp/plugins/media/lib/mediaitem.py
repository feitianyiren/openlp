# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4

###############################################################################
# OpenLP - Open Source Lyrics Projection                                      #
# --------------------------------------------------------------------------- #
# Copyright (c) 2008-2009 Raoul Snyman                                        #
# Portions copyright (c) 2008-2009 Martin Thompson, Tim Bentley, Carsten      #
# Tinggaard, Jon Tibble, Jonathan Corwin, Maikel Stuivenberg, Scott Guerrieri #
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

import logging
import os

from PyQt4 import QtCore, QtGui

from openlp.core.lib import MediaManagerItem, BaseListWithDnD, buildIcon

class MediaListView(BaseListWithDnD):
    def __init__(self, parent=None):
        self.PluginName = u'Media'
        BaseListWithDnD.__init__(self, parent)

class MediaMediaItem(MediaManagerItem):
    """
    This is the custom media manager item for Media Slides.
    """
    global log
    log = logging.getLogger(u'MediaMediaItem')
    log.info(u'Media Media Item loaded')

    def __init__(self, parent, icon, title):
        self.PluginNameShort = u'Media'
        self.IconPath = u'images/image'
        self.ConfigSection = u'media'
        self.ConfigSection = title
        # this next is a class, not an instance of a class - it will
        # be instanced by the base MediaManagerItem
        self.ListViewWithDnD_class = MediaListView
        self.PreviewFunction = self.video_get_preview
        MediaManagerItem.__init__(self, parent, icon, title)
        self.ServiceItemIconName = u':/media/media_video.png'
        self.MainDisplay = self.parent.live_controller.parent.mainDisplay

    def initPluginNameVisible(self):
        self.PluginNameVisible = self.trUtf8(u'Media')

    def retranslateUi(self):
        self.OnNewPrompt = self.trUtf8(u'Select Media')
        self.OnNewFileMasks = self.trUtf8(u'Videos (*.avi *.mpeg *.mpg'
            '*.mp4);;Audio (*.ogg *.mp3 *.wma);;All files (*)')

    def requiredIcons(self):
        MediaManagerItem.requiredIcons(self)
        self.hasFileIcon = True
        self.hasNewIcon = False
        self.hasEditIcon = False

    def video_get_preview(self):
        # For now cross platform is an icon.  Phonon does not support
        # individual frame access (yet?) and GStreamer is not available
        # on Windows
        return QtGui.QPixmap(u':/media/media_video.png').toImage()

    def generateSlideData(self, service_item):
        items = self.ListView.selectedIndexes()
        if len(items) > 1:
            return False
        service_item.title = unicode(self.trUtf8(u'Media'))
        for item in items:
            bitem = self.ListView.item(item.row())
            filename = unicode((bitem.data(QtCore.Qt.UserRole)).toString())
            frame = u':/media/media_video.png'
            (path, name) = os.path.split(filename)
            service_item.add_from_command(path, name, frame)
        return True

    def initialise(self):
        self.ListView.setSelectionMode(
            QtGui.QAbstractItemView.ExtendedSelection)
        self.ListView.setIconSize(QtCore.QSize(88,50))
        self.loadList(self.parent.config.load_list(self.ConfigSection))

    def onDeleteClick(self):
        item = self.ListView.currentItem()
        if item:
            row = self.ListView.row(item)
            self.ListView.takeItem(row)
            self.parent.config.set_list(
                self.ConfigSection, self.getFileList())

    def loadList(self, list):
        for file in list:
            (path, filename) = os.path.split(unicode(file))
            item_name = QtGui.QListWidgetItem(filename)
            img = self.video_get_preview()
            item_name.setIcon(buildIcon(img))
            item_name.setData(QtCore.Qt.UserRole, QtCore.QVariant(file))
            self.ListView.addItem(item_name)
