# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=120 tabstop=4 softtabstop=4

###############################################################################
# OpenLP - Open Source Lyrics Projection                                      #
# --------------------------------------------------------------------------- #
# Copyright (c) 2008-2014 Raoul Snyman                                        #
# Portions copyright (c) 2008-2014 Tim Bentley, Gerald Britton, Jonathan      #
# Corwin, Samuel Findlay, Michael Gorven, Scott Guerrieri, Matthias Hub,      #
# Meinert Jordan, Armin Köhler, Erik Lundin, Edwin Lunando, Brian T. Meyer.   #
# Joshua Miller, Stevan Pettit, Andreas Preikschat, Mattias Põldaru,          #
# Christian Richter, Philip Ridout, Simon Scudder, Jeffrey Smith,             #
# Maikel Stuivenberg, Martin Thompson, Jon Tibble, Dave Warnock,              #
# Frode Woldsund, Martin Zibricky, Patrick Zimmermann                         #
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
"""
Package to test the openlp.core.ui.firsttimeform package.
"""
from unittest import TestCase

from tests.functional import MagicMock

from tests.helpers.testmixin import TestMixin
from openlp.core.common import Registry
from openlp.core.ui.firsttimeform import FirstTimeForm


class TestFirstTimeForm(TestCase, TestMixin):

    def setUp(self):
        screens = MagicMock()
        self.get_application()
        Registry.create()
        Registry().register('application', self.app)
        self.first_time_form = FirstTimeForm(screens)

    def test_access_to_config(self):
        """
        Test if we can access the First Time Form's config file
        """
        # GIVEN A new First Time Form instance.

        # WHEN The default First Time Form is built.

        # THEN The First Time Form web configuration file should be accessable.
        self.assertTrue(self.first_time_form.web_access,
                        'First Time Wizard\'s web configuration file should be available')

    def test_parsable_config(self):
        """
        Test if the First Time Form's config file is parsable
        """
        # GIVEN A new First Time Form instance.

        # WHEN The default First Time Form is built.

        # THEN The First Time Form web configuration file should be parsable
        self.assertTrue(self.first_time_form.songs_url,
                        'First Time Wizard\'s web configuration file should be parsable')
