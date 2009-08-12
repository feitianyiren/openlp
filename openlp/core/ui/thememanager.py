# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4
"""
OpenLP - Open Source Lyrics Projection
Copyright (c) 2009 Raoul Snyman
Portions copyright (c) 2009 Martin Thompson, Tim Bentley,

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
import os
import sys
import zipfile
import shutil
import logging

from xml.etree.ElementTree import ElementTree, XML
from PyQt4 import QtCore, QtGui

from openlp.core.ui import AmendThemeForm, ServiceManager
from openlp.core.theme import Theme
from openlp.core.lib import PluginConfig, Event, EventType, \
    EventManager, OpenLPToolbar, ThemeXML, Renderer, translate, \
    file_to_xml, buildIcon
from openlp.core.utils import ConfigHelper

class ThemeManager(QtGui.QWidget):
    """
    Manages the orders of Theme.
    """
    global log
    log = logging.getLogger(u'ThemeManager')

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.parent = parent
        self.Layout = QtGui.QVBoxLayout(self)
        self.Layout.setSpacing(0)
        self.Layout.setMargin(0)
        self.amendThemeForm = AmendThemeForm(self)
        self.Toolbar = OpenLPToolbar(self)
        self.Toolbar.addToolbarButton(
            translate(u'ThemeManager', u'New Theme'), u':/themes/theme_new.png',
            translate(u'ThemeManager', u'Create a new theme'), self.onAddTheme)
        self.Toolbar.addToolbarButton(
            translate(u'ThemeManager', u'Edit Theme'), u':/themes/theme_edit.png',
            translate(u'ThemeManager', u'Edit a theme'), self.onEditTheme)
        self.Toolbar.addToolbarButton(
            translate(u'ThemeManager', u'Delete Theme'), u':/themes/theme_delete.png',
            translate(u'ThemeManager', u'Delete a theme'), self.onDeleteTheme)
        self.Toolbar.addSeparator()
        self.Toolbar.addToolbarButton(
            translate(u'ThemeManager', u'Import Theme'), u':/themes/theme_import.png',
            translate(u'ThemeManager', u'Import a theme'), self.onImportTheme)
        self.Toolbar.addToolbarButton(
            translate(u'ThemeManager', u'Export Theme'), u':/themes/theme_export.png',
            translate(u'ThemeManager', u'Export a theme'), self.onExportTheme)
        self.ThemeWidget = QtGui.QWidgetAction(self.Toolbar)
        self.Layout.addWidget(self.Toolbar)
        self.ThemeListWidget = QtGui.QListWidget(self)
        self.ThemeListWidget.setAlternatingRowColors(True)
        self.ThemeListWidget.setIconSize(QtCore.QSize(88,50))
        self.Layout.addWidget(self.ThemeListWidget)
        #Signals
        QtCore.QObject.connect(self.ThemeListWidget,
           QtCore.SIGNAL(u'doubleClicked(QModelIndex)'), self.changeGlobal)
        #Variables
        self.themelist = []
        self.path = os.path.join(ConfigHelper.get_data_path(), u'themes')
        self.checkThemesExists(self.path)
        self.amendThemeForm.path = self.path
        # Last little bits of setting up
        self.config = PluginConfig(u'themes')
        self.servicePath = self.config.get_data_path()
        self.global_theme = unicode(self.config.get_config(u'theme global theme', u''))

    def getDefault(self):
        return self.global_theme

    def changeGlobal(self, index):
        for count in range (0,  self.ThemeListWidget.count()):
            item = self.ThemeListWidget.item(count)
            oldName =  item.text()
            #reset the old name
            if oldName != unicode(item.data(QtCore.Qt.UserRole).toString()):
                self.ThemeListWidget.item(count).setText(unicode(item.data(QtCore.Qt.UserRole).toString()))
            #Set the new name
            if count  == index.row():
                self.global_theme = unicode(self.ThemeListWidget.item(count).text())
                name = u'%s (%s)' % (self.global_theme, translate(u'ThemeManager', u'default'))
                self.ThemeListWidget.item(count).setText(name)
                self.config.set_config(u'theme global theme', self.global_theme)
                self.pushThemes()

    def onAddTheme(self):
        self.amendThemeForm.loadTheme(None)
        self.amendThemeForm.exec_()

    def onEditTheme(self):
        item = self.ThemeListWidget.currentItem()
        if item is not None:
            self.amendThemeForm.loadTheme(unicode(item.data(QtCore.Qt.UserRole).toString()))
            self.amendThemeForm.exec_()

    def onDeleteTheme(self):
        self.global_theme = unicode(self.config.get_config(u'theme global theme', u''))
        item = self.ThemeListWidget.currentItem()
        if item is not None:
            theme = unicode(item.text())
            # should be the same unless default
            if theme != unicode(item.data(QtCore.Qt.UserRole).toString()):
                QtGui.QMessageBox.critical(self,
                    translate(u'ThemeManager', u'Error'),
                    translate(u'ThemeManager', u'You are unable to delete the default theme!'),
                    QtGui.QMessageBox.StandardButtons(QtGui.QMessageBox.Ok))
            else:
                self.themelist.remove(theme)
                th = theme +  u'.png'
                row = self.ThemeListWidget.row(item)
                self.ThemeListWidget.takeItem(row)
                try:
                    os.remove(os.path.join(self.path, th))
                except:
                    #if not present do not worry
                    pass
                try:
                    shutil.rmtree(os.path.join(self.path, theme))
                except:
                    #if not present do not worry
                    pass
                #As we do not reload the themes push out the change
                #Reaload the list as the internal lists and events need to be triggered
                self.pushThemes()

    def onExportTheme(self):
        pass

    def onImportTheme(self):
        files = QtGui.QFileDialog.getOpenFileNames(None,
            translate(u'ThemeManager', u'Select Theme Import File'),
            self.path, u'Theme (*.*)')
        log.info(u'New Themes %s', unicode(files))
        if len(files) > 0:
            for file in files:
                self.unzipTheme(file, self.path)
        self.loadThemes()

    def loadThemes(self):
        """
        Loads the theme lists and triggers updates accross
        the whole system using direct calls or core functions
        and events for the plugins.
        The plugins will call back in to get the real list if they want it.
        """
        log.debug(u'Load themes from dir')
        self.themelist = []
        self.ThemeListWidget.clear()
        for root, dirs, files in os.walk(self.path):
            for name in files:
                if name.endswith(u'.png'):
                    #check to see file is in theme root directory
                    theme =  os.path.join(self.path, name)
                    if os.path.exists(theme):
                        (path, filename) = os.path.split(unicode(file))
                        textName = os.path.splitext(name)[0]
                        if textName == self.global_theme:
                            name = u'%s (%s)' % (textName, translate(u'ThemeManager', u'default'))
                        else:
                            name = textName
                        item_name = QtGui.QListWidgetItem(name)
                        item_name.setIcon(buildIcon(theme))
                        item_name.setData(QtCore.Qt.UserRole, QtCore.QVariant(textName))
                        self.ThemeListWidget.addItem(item_name)
                        self.themelist.append(textName)
        self.pushThemes()

    def pushThemes(self):
        self.parent.EventManager.post_event(Event(EventType.ThemeListChanged,u'ThemeManager'))

    def getThemes(self):
        return self.themelist

    def getThemeData(self, themename):
        log.debug(u'getthemedata for theme %s', themename)
        xml_file = os.path.join(self.path, unicode(themename), unicode(themename) + u'.xml')
        try:
            xml = file_to_xml(xml_file)
            #print xml
        except:
            newtheme = ThemeXML()
            newtheme.new_document(u'New Theme')
            newtheme.add_background_solid(unicode(u'#000000'))
            newtheme.add_font(unicode(QtGui.QFont().family()), unicode(u'#FFFFFF'), unicode(30), u'False')
            newtheme.add_font(unicode(QtGui.QFont().family()), unicode(u'#FFFFFF'), unicode(12), u'False', u'footer')
            newtheme.add_display(u'False', unicode(u'#FFFFFF'), u'False', unicode(u'#FFFFFF'),
                unicode(0), unicode(0), unicode(0))
            xml = newtheme.extract_xml()
        theme = ThemeXML()
        #print theme
        theme.parse(xml)
        #print "A ", theme
        theme.extend_image_filename(self.path)
        return theme

    def checkThemesExists(self, dir):
        log.debug(u'check themes')
        if os.path.exists(dir) == False:
            os.mkdir(dir)

    def unzipTheme(self, filename, dir):
        """
        Unzip the theme, remove the preview file if stored
        Generate a new preview fileCheck the XML theme version and upgrade if
        necessary.
        """
        log.debug(u'Unzipping theme %s', filename)
        zip = zipfile.ZipFile(unicode(filename))
        filexml = None
        themename = None
        for file in zip.namelist():
            if file.endswith(os.path.sep):
                theme_dir = os.path.join(dir, file)
                if os.path.exists(theme_dir) == False:
                    os.mkdir(os.path.join(dir, file))
            else:
                fullpath = os.path.join(dir, file)
                names = file.split(os.path.sep)
                if len(names) > 1:
                    # not preview file
                    if themename is None:
                        themename = names[0]
                    xml_data = zip.read(file)
                    if os.path.splitext(file)[1].lower() in [u'.xml']:
                        if self.checkVersion1(xml_data):
                            # upgrade theme xml
                            filexml = self.migrateVersion122(filename, fullpath, xml_data)
                        else:
                            filexml = xml_data
                        outfile = open(fullpath, u'w')
                        outfile.write(filexml)
                        outfile.close()
                    else:
                        outfile = open(fullpath, u'w')
                        outfile.write(zip.read(file))
                        outfile.close()
        self.generateAndSaveImage(dir, themename, filexml)

    def checkVersion1(self, xmlfile):
        """
        Am I a version 1 theme
        """
        log.debug(u'checkVersion1 ')
        theme = xmlfile
        tree = ElementTree(element=XML(theme)).getroot()
        if tree.find(u'BackgroundType') is None:
            return False
        else:
            return True

    def migrateVersion122(self, filename, fullpath, xml_data):
        """
        Called by convert the xml data from version 1 format
        to the current format.
        New fields are defaulted but the new theme is useable
        """
        log.debug(u'migrateVersion122 %s %s', filename, fullpath)
        theme = Theme(xml_data)
        newtheme = ThemeXML()
        newtheme.new_document(theme.Name)
        if theme.BackgroundType == 0:
            newtheme.add_background_solid(unicode(theme.BackgroundParameter1.name()))
        elif theme.BackgroundType == 1:
            direction = u'vertical'
            if theme.BackgroundParameter3.name() == 1:
                direction = u'horizontal'
            newtheme.add_background_gradient(
                unicode(theme.BackgroundParameter1.name()),
                unicode(theme.BackgroundParameter2.name()), direction)
        else:
            newtheme.add_background_image(unicode(theme.BackgroundParameter1))

        newtheme.add_font(unicode(theme.FontName), unicode(theme.FontColor.name()),
            unicode(theme.FontProportion * 2), u'False')
        newtheme.add_font(unicode(theme.FontName), unicode(theme.FontColor.name()),
            unicode(12), u'False', u'footer')
        outline = False
        shadow = False
        if theme.Shadow == 1:
            shadow = True
        if theme.Outline == 1:
            outline = True
        newtheme.add_display(unicode(shadow), unicode(theme.ShadowColor.name()),
            unicode(outline), unicode(theme.OutlineColor.name()),
            unicode(theme.HorizontalAlign), unicode(theme.VerticalAlign),
            unicode(theme.WrapStyle))
        return newtheme.extract_xml()

    def saveTheme(self, name, theme_xml, image_from, image_to) :
        """
        Called by thememaintenance Dialog to save the theme
        and to trigger the reload of the theme list
        """
        log.debug(u'saveTheme %s %s', name, theme_xml)
        theme_dir = os.path.join(self.path, name)
        if os.path.exists(theme_dir) == False:
            os.mkdir(os.path.join(self.path, name))
        theme_file = os.path.join(theme_dir, name + u'.xml')
        outfile = open(theme_file, u'w')
        outfile.write(theme_xml)
        outfile.close()
        if image_from is not None and image_from != image_to:
            shutil.copyfile(image_from,  image_to)
        self.generateAndSaveImage(self.path, name, theme_xml)
        self.loadThemes()

    def generateAndSaveImage(self, dir, name, theme_xml):
        log.debug(u'generateAndSaveImage %s %s %s', dir, name, theme_xml)
        theme = ThemeXML()
        theme.parse(theme_xml)
        theme.extend_image_filename(dir)
        frame = self.generateImage(theme)
        samplepathname = os.path.join(self.path, name + u'.png')
        if os.path.exists(samplepathname):
            os.unlink(samplepathname)
        frame.save(samplepathname, u'png')
        log.debug(u'Theme image written to %s', samplepathname)

    def generateImage(self, themedata):
        """
        Call the RenderManager to build a Sample Image
        """
        log.debug(u'generateImage %s ', themedata)
        frame = self.parent.RenderManager.generate_preview(themedata)
        return frame

    def getPreviewImage(self, theme):
        log.debug(u'getPreviewImage %s ', theme)
        image = os.path.join(self.path, theme + u'.png')
        return image
