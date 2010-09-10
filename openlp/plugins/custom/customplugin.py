# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4

###############################################################################
# OpenLP - Open Source Lyrics Projection                                      #
# --------------------------------------------------------------------------- #
# Copyright (c) 2008-2010 Raoul Snyman                                        #
# Portions copyright (c) 2008-2010 Tim Bentley, Jonathan Corwin, Michael      #
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

import logging

from forms import EditCustomForm

from openlp.core.lib import Plugin, StringType, build_icon, translate
from openlp.core.lib.db import Manager
from openlp.plugins.custom.lib import CustomMediaItem, CustomTab
from openlp.plugins.custom.lib.db import CustomSlide, init_schema

log = logging.getLogger(__name__)

class CustomPlugin(Plugin):
    """
    This plugin enables the user to create, edit and display
    custom slide shows. Custom shows are divided into slides.
    Each show is able to have it's own theme.
    Custom shows are designed to replace the use of Customs where
    the Customs plugin has become restrictive. Examples could be
    Welcome slides, Bible Reading information, Orders of service.
    """
    log.info(u'Custom Plugin loaded')

    def __init__(self, plugin_helpers):
        self.set_plugin_strings()
        Plugin.__init__(self, u'Custom', u'1.9.2', plugin_helpers)
        self.weight = -5
        self.custommanager = Manager(u'custom', init_schema)
        self.edit_custom_form = EditCustomForm(self.custommanager)
        self.icon_path = u':/plugins/plugin_custom.png'
        self.icon = build_icon(self.icon_path)

    def getSettingsTab(self):
        return CustomTab(self.name)

    def getMediaManagerItem(self):
        # Create the CustomManagerItem object
        return CustomMediaItem(self, self.icon, self.name)

    def about(self):
        about_text = translate('CustomPlugin', '<strong>Custom Plugin</strong>'
            '<br />The custom plugin provides the ability to set up custom '
            'text slides that can be displayed on the screen the same way '
            'Customs are. This plugin provides greater freedom over the Customs '
            'plugin.')
        return about_text

    def usesTheme(self, theme):
        """
        Called to find out if the custom plugin is currently using a theme.

        Returns True if the theme is being used, otherwise returns False.
        """
        if self.custommanager.get_all_objects(CustomSlide,
            CustomSlide.theme_name == theme):
            return True
        return False

    def renameTheme(self, oldTheme, newTheme):
        """
        Renames a theme the custom plugin is using making the plugin use the
        new name.

        ``oldTheme``
            The name of the theme the plugin should stop using.

        ``newTheme``
            The new name the plugin should now use.
        """
        customsUsingTheme = self.custommanager.get_all_objects(CustomSlide,
            CustomSlide.theme_name == oldTheme)
        for custom in customsUsingTheme:
            custom.theme_name = newTheme
            self.custommanager.save_object(custom)
    def set_plugin_strings(self):
        """
        Called to define all translatable texts of the plugin
        """
        self.name = u'Custom'
        self.name_lower = u'custom'

        self.strings = {}
        # for names in mediamanagerdock and pluginlist
        self.strings[StringType.Name] = {
            u'singular': translate('CustomsPlugin', 'Custom'),
            u'plural': translate('CustomsPlugin', 'Customs')
        }

        # Middle Header Bar
        ## Import Button ##
        self.strings[StringType.Import] = {
            u'title': translate('CustomsPlugin', 'Import'),
            u'tooltip': translate('CustomsPlugin', 'Import a Custom')
        }
        ## Load Button ##
        self.strings[StringType.Load] = {
            u'title': translate('CustomsPlugin', 'Load'),
            u'tooltip': translate('CustomsPlugin', 'Load a new Custom')
        }
        ## New Button ##
        self.strings[StringType.New] = {
            u'title': translate('CustomsPlugin', 'Add'),
            u'tooltip': translate('CustomsPlugin', 'Add a new Custom')
        }
        ## Edit Button ##
        self.strings[StringType.Edit] = {
            u'title': translate('CustomsPlugin', 'Edit'),
            u'tooltip': translate('CustomsPlugin', 'Edit the selected Custom')
        }
        ## Delete Button ##
        self.strings[StringType.Delete] = {
            u'title': translate('CustomsPlugin', 'Delete'),
            u'tooltip': translate('CustomsPlugin', 'Delete the selected Custom')
        }
        ## Preview ##
        self.strings[StringType.Preview] = {
            u'title': translate('CustomsPlugin', 'Preview'),
            u'tooltip': translate('CustomsPlugin', 'Preview the selected Custom')
        }
        ## Live  Button ##
        self.strings[StringType.Live] = {
            u'title': translate('CustomsPlugin', 'Live'),
            u'tooltip': translate('CustomsPlugin', 'Send the selected Custom live')
        }
        ## Add to service Button ##
        self.strings[StringType.Service] = {
            u'title': translate('CustomsPlugin', 'Service'),
            u'tooltip': translate('CustomsPlugin', 'Add the selected Custom to the service')
        }
