# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=120 tabstop=4 softtabstop=4

###############################################################################
# OpenLP - Open Source Lyrics Projection                                      #
# --------------------------------------------------------------------------- #
# Copyright (c) 2008-2013 Raoul Snyman                                        #
# Portions copyright (c) 2008-2013 Tim Bentley, Gerald Britton, Jonathan      #
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
The :mod:`http` module contains the API web server. This is a lightweight web
server used by remotes to interact with OpenLP. It uses JSON to communicate with
the remotes.
"""

import ssl
import socket
import os
import logging

from PyQt4 import QtCore

from openlp.core.common.applocation import AppLocation
from openlp.core.lib import Settings

from openlp.plugins.remotes.lib import HttpRouter

from socketserver import BaseServer, ThreadingMixIn
from http.server import BaseHTTPRequestHandler, HTTPServer

log = logging.getLogger(__name__)


class CustomHandler(BaseHTTPRequestHandler, HttpRouter):
    """
    Stateless session handler to handle the HTTP request and process it.
    This class handles just the overrides to the base methods and the logic to invoke the
    methods within the HttpRouter class.
    DO not try change the structure as this is as per the documentation.
    """

    def do_POST(self):
        """
        Present pages / data and invoke URL level user authentication.
        """
        self.do_post_processor()

    def do_GET(self):
        """
        Present pages / data and invoke URL level user authentication.
        """
        self.do_post_processor()


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass


class HttpThread(QtCore.QThread):
    """
    A special Qt thread class to allow the HTTP server to run at the same time as the UI.
    """
    def __init__(self, server):
        """
        Constructor for the thread class.

        ``server``
            The http server class.
        """
        super(HttpThread, self).__init__(None)
        self.http_server = server

    def run(self):
        """
        Run the thread.
        """
        self.http_server.start_server()


class OpenLPServer():
    def __init__(self):
        """
        Initialise the http server, and start the server of the correct type http / https
        """
        log.debug('Initialise httpserver')
        self.settings_section = 'remotes'
        self.http_thread = HttpThread(self)
        self.http_thread.start()

    def start_server(self):
        """
        Start the correct server and save the handler
        """
        address = Settings().value(self.settings_section + '/ip address')
        if Settings().value(self.settings_section + '/https enabled'):
            port = Settings().value(self.settings_section + '/https port')
            self.httpd = HTTPSServer((address, port), CustomHandler)
            log.debug('Started ssl httpd...')
        else:
            port = Settings().value(self.settings_section + '/port')
            self.httpd = ThreadingHTTPServer((address, port), CustomHandler)
            log.debug('Started non ssl httpd...')
        self.httpd.serve_forever()

    def stop_server(self):
        """
        Stop the server
        """
        self.http_thread.exit(0)
        self.httpd = None
        log.debug('Stopped the server.')


class HTTPSServer(HTTPServer):
    def __init__(self, address, handler):
        """
        Initialise the secure handlers for the SSL server if required.s
        """
        BaseServer.__init__(self, address, handler)
        local_data = AppLocation.get_directory(AppLocation.DataDir)
        self.socket = ssl.SSLSocket(
            sock=socket.socket(self.address_family, self.socket_type),
            ssl_version=ssl.PROTOCOL_TLSv1,
            certfile=os.path.join(local_data, 'remotes', 'openlp.crt'),
            keyfile=os.path.join(local_data, 'remotes', 'openlp.key'),
            server_side=True)
        self.server_bind()
        self.server_activate()



