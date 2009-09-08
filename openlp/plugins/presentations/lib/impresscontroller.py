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
# OOo API documentation:
# http://api.openoffice.org/docs/common/ref/com/sun/star/presentation/XSlideShowController.html
# http://docs.go-oo.org/sd/html/classsd_1_1SlideShow.html
# http://www.oooforum.org/forum/viewtopic.phtml?t=5252
# http://wiki.services.openoffice.org/wiki/Documentation/DevGuide/Working_with_Presentations
# http://mail.python.org/pipermail/python-win32/2008-January/006676.html
#http://www.linuxjournal.com/content/starting-stopping-and-connecting-openoffice-python
#http://nxsy.org/comparing-documents-with-openoffice-and-python

import logging
import os ,  subprocess
import time
import uno
import sys

from PyQt4 import QtCore

class ImpressController(object):
    """
    Class to control interactions with Impress Presentations
    It creates the runtime Environment , Loads the and Closes the Presentation
    As well as trigggering the correct activities based on the users input
    """
    global log
    log = logging.getLogger(u'ImpressController')

    def __init__(self):
        log.debug(u'Initialising')
        self.process = None
        self.document = None
        self.presentation = None
        self.startOpenoffice()

    def startOpenoffice(self):
        """
        Loads a running version of OpenOffice inthe background.
        It is not displayed to the user but is available to the Uno interface
        when required.
        """
        log.debug(u'start Openoffice')
        cmd = u'openoffice.org -nologo -norestore -minimized -headless ' + u'"' + u'-accept=socket,host=localhost,port=2002;urp;'+ u'"'
        self.process = QtCore.QProcess()
        self.process.startDetached(cmd)
        self.process.waitForStarted()

    def kill(self):
        """
        Called at system exit to clean up any running presentations
        """
        log.debug(u'Kill')
        self.closePresentation()

    def loadPresentation(self, presentation):
        """
        Called when a presentation is added to the SlideController.
        It builds the environment, starts communcations with the background
        OpenOffice task started earlier.  If OpenOffice is not present is ts started.
        Once the environment is available the presentation is loaded and started.

        ``presentation``
        The file name of the presentatios to the run.
        """
        log.debug(u'LoadPresentation')
        ctx = None
        loop = 0
        context = uno.getComponentContext()
        resolver = context.ServiceManager.createInstanceWithContext(u'com.sun.star.bridge.UnoUrlResolver', context)
        while ctx == None and loop < 3:
            try:
                ctx = resolver.resolve(u'uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext')
            except:
                self.startOpenoffice()
                loop += 1
        try:
            smgr = ctx.ServiceManager
            desktop = smgr.createInstanceWithContext( "com.sun.star.frame.Desktop", ctx )
            url = uno.systemPathToFileUrl(presentation)
            properties = []
            properties = tuple(properties)
            self.document = desktop.loadComponentFromURL(url, "_blank", 0, properties)
            self.presentation = self.document.getPresentation()
            self.presentation.start()
            self.xSlideShowController =  desktop.getCurrentComponent().Presentation.getController()
        except:
            log.error(u'Failed reason %s' % sys.exc_info())

    def closePresentation(self):
        """
        Close presentation and clean up objects
        Triggerent by new object being added to SlideController orOpenLP
        being shut down
        """
        if self.document is not None:
            if self.presentation is not None:
                self.presentation.end()
                self.presentation = None
            self.document.dispose()
            self.document = None

    def isActive(self):
        return self.presentation.isRunning() and self.presentation.isActive()

    def resume(self):
        return self.presentation.resume()

    def pause(self):
        return self.presentation.pause()

    def blankScreen(self):
        self.presentation.blankScreen(0)

    def stop(self):
        self.presentation.deactivate()
        # self.presdoc.end()

    def go(self):
        self.presentation.activate()
        # self.presdoc.start()

    def getSlideNumber(self):
        return self.presentation.getCurrentSlideIndex

    def setSlideNumber(self, slideno):
        self.presentation.gotoSlideIndex(slideno)

    slideNumber = property(getSlideNumber, setSlideNumber)

    def nextStep(self):
       """
       Triggers the next effect of slide on the running presentation
       """
       self.xSlideShowController.gotoNextEffect()

    def previousStep(self):
        """
        Triggers the previous slide on the running presentation
        """
        self.xSlideShowController.gotoPreviousSlide()
