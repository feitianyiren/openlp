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

import os
import logging
from tempfile import NamedTemporaryFile
import re
from subprocess import check_output,  call
from PyQt4 import QtCore, QtGui

from openlp.core.lib import ScreenList
from presentationcontroller import PresentationController, PresentationDocument


log = logging.getLogger(__name__)


class PdfController(PresentationController):
    """
    Class to control PDF presentations
    """
    log.info(u'PdfController loaded')

    def __init__(self, plugin):
        """
        Initialise the class
        """
        log.debug(u'Initialising')
        self.process = None
        PresentationController.__init__(self, plugin, u'Pdf', PdfDocument)
        self.supports = [u'pdf', u'xps']
        self.mudrawbin = u''
        self.gsbin = u''
        self.viewer = None

    def check_available(self):
        """
        PdfController is able to run on this machine.
        """
        log.debug(u'check_available Pdf')
        return self.check_installed()

    def check_installed(self):
        """
        Check the viewer is installed.
        """
        log.debug(u'check_installed Pdf')
        # First try to find mupdf
        try:
            self.mudrawbin = check_output([u'which', u'mudraw']).rstrip('\n')
        except CalledProcessError:
            self.mudrawbin = u''

        # if mupdf isn't installed, fallback to ghostscript
        if self.mudrawbin == u'':
            try:
                self.gsbin = check_output([u'which', u'gs']).rstrip('\n')
            except CalledProcessError:
                self.gsbin = u''
                
        if self.mudrawbin == u'' and self.gsbin == u'':
            return False
        else:
            return True

    def start_process(self):
        log.debug(u'start_process pdf')
        # Setup viewer
        try:
            size = ScreenList().current[u'size']
            self.viewer = PdfViewer(size)
        except Exception as e: 
            log.debug(e)
            
        
    def kill(self):
        """
        Called at system exit to clean up any running presentations
        """
        log.debug(u'Kill pdfviewer')
        self.viewer.close()
        while self.docs:
            self.docs[0].close_presentation()


class PdfDocument(PresentationDocument):
    """
    Class which holds information and controls a single presentation.
    """
    def __init__(self, controller, presentation):
        """
        Constructor, store information about the file and initialise.
        """
        log.debug(u'Init Presentation Pdf')
        PresentationDocument.__init__(self, controller, presentation)
        self.presentation = None
        self.blanked = False
        self.hidden = False
        self.image_files = []
        self.num_pages = -1

    # Only used when using ghostscript
    # Ghostscript can't scale automaticly while keeping aspect like mupdf, so we need
    # to get the ratio bewteen the screen size and the PDF to scale
    def gs_get_resolution(self,  size):
        # Use a postscript script to get size of the pdf. It is assumed that all pages have same size
        postscript = u'%!PS \n\
() = \n\
File dup (r) file runpdfbegin \n\
1 pdfgetpage dup \n\
/MediaBox pget { \n\
aload pop exch 4 1 roll exch sub 3 1 roll sub \n\
( Size: x: ) print =print (, y: ) print =print (\n) print \n\
} if \n\
flush \n\
quit \n\
'
        # Put postscript into tempfile
        tmpfile = NamedTemporaryFile(delete=False)
        tmpfile.write(postscript)
        tmpfile.close()
        
        # Run the script on the pdf to get the size
        runlog = check_output([self.controller.gsbin, u'-dNOPAUSE', u'-dNODISPLAY', u'-dBATCH', u'-sFile=' + self.filepath, tmpfile.name])
        os.unlink(tmpfile.name)
        
        # Extract the pdf resolution from output, the format is " Size: x: <width>, y: <height>"
        width = 0
        height = 0
        for line in runlog.splitlines():
            try:
                width = re.search(u'.*Size: x: (\d+), y: \d+.*', line).group(1)
                height = re.search(u'.*Size: x: \d+, y: (\d+).*', line).group(1)
                break;
            except AttributeError:
                pass

        # Calculate the ratio from pdf to screen
        if width > 0 and height > 0:
            width_ratio = size.right() / float(width)
            heigth_ratio = size.bottom() / float(height)
            
            # return the resolution that should be used. 72 is default.
            if width_ratio > heigth_ratio:
                return int(heigth_ratio * 72)
            else:
                return int(width_ratio * 72)
        else:
            return 72

    def load_presentation(self):
        """
        Called when a presentation is added to the SlideController. It generates images from the PDF.
        """
        log.debug(u'load_presentation pdf')
        
        # Check if the images has already been created, and if yes load them
        if os.path.isfile(self.get_temp_folder() + u'/mainslide001.png'):
            created_files = sorted(os.listdir(self.get_temp_folder()))
            for fn in created_files:
                if os.path.isfile(self.get_temp_folder() + u'/' + fn):
                    self.image_files.append(self.get_temp_folder()+ u'/' + fn)
            self.num_pages = len(self.image_files)
            return True
        
        size = ScreenList().current[u'size']
        # Generate images from PDF that will fit the frame.
        runlog = u''
        try:
            if not os.path.isdir(self.get_temp_folder()):
                os.makedirs(self.get_temp_folder())
            if self.controller.mudrawbin != u'':
                runlog = check_output([self.controller.mudrawbin, u'-w', str(size.right()), u'-h', str(size.bottom()), u'-o', self.get_temp_folder() + u'/mainslide%03d.png', self.filepath])
            elif self.controller.gsbin != u'':
                resolution = self.gs_get_resolution(size)
                runlog = check_output([self.controller.gsbin, u'-dSAFER', u'-dNOPAUSE', u'-dBATCH', u'-sDEVICE=png16m', u'-r' + str(resolution), u'-dTextAlphaBits=4', u'-dGraphicsAlphaBits=4', u'-sOutputFile=' + self.get_temp_folder() + u'/mainslide%03d.png', self.filepath])
            created_files = sorted(os.listdir(self.get_temp_folder()))
            for fn in created_files:
                if os.path.isfile(self.get_temp_folder() + u'/' + fn):
                    self.image_files.append(self.get_temp_folder()+ u'/' + fn)
        except Exception as e: 
            log.debug(e)
            log.debug(runlog)
            return False 
        self.num_pages = len(self.image_files)
        
        # Create thumbnails
        self.create_thumbnails()
        return True

    def create_thumbnails(self):
        """
        Generates thumbnails
        """
        log.debug(u'create_thumbnails pdf')
        if self.check_thumbnails():
            return
        log.debug(u'create_thumbnails proceeding')
        
        # use builtin function to create thumbnails from generated images
        index = 1
        for image in self.image_files:
            self.convert_thumbnail(image, index)
            index += 1

    def close_presentation(self):
        """
        Close presentation and clean up objects. Triggered by new object being added to SlideController or OpenLP being
        shut down.
        """
        log.debug(u'close_presentation pdf')
        self.controller.remove_doc(self)
        # TODO
        
    def is_loaded(self):
        """
        Returns true if a presentation is loaded.
        """
        log.debug(u'is_loaded pdf')
        if self.num_pages < 0:
            return False
        return True

    def is_active(self):
        """
        Returns true if a presentation is currently active.
        """
        log.debug(u'is_active pdf')
        return self.is_loaded() and not self.hidden

    def blank_screen(self):
        """
        Blanks the screen.
        """
        log.debug(u'blank_screen pdf')
        self.blanked = True
        self.controller.viewer.blank()

    def unblank_screen(self):
        """
        Unblanks (restores) the presentation.
        """
        log.debug(u'unblank_screen pdf')
        self.blanked = False
        self.controller.viewer.unblank()

    def is_blank(self):
        """
        Returns true if screen is blank.
        """
        log.debug(u'is blank pdf')
        return self.blanked

    def stop_presentation(self):
        """
        Stops the current presentation and hides the output.
        """
        log.debug(u'stop_presentation pdf')
        self.hidden = True
        self.controller.viewer.stop()

    def start_presentation(self):
        """
        Starts a presentation from the beginning.
        """
        log.debug(u'start_presentation pdf')
        if self.hidden:
            self.hidden = False
        self.controller.viewer.start(self.image_files)

    def get_slide_number(self):
        """
        Return the current slide number on the screen, from 1.
        """
        log.debug(u'get_slide_number pdf')
        return self.controller.viewer.get_current_page() + 1

    def get_slide_count(self):
        """
        Returns total number of slides.
        """
        log.debug(u'get_slide_count pdf')
        return self.num_pages

    def goto_slide(self, slideno):
        """
        Moves to a specific slide in the presentation.
        """
        log.debug(u'goto_slide pdf' + str(slideno))
        self.controller.viewer.show_page(slideno - 1)
        # TODO

    def next_step(self):
        """
        Triggers the next effect of slide on the running presentation.
        """
        log.debug(u'next_step pdf')
        self.controller.viewer.next_page()

    def previous_step(self):
        """
        Triggers the previous slide on the running presentation.
        """
        log.debug(u'previous_step pdf')
        self.controller.viewer.previous_page()


class PdfViewer(QtGui.QWidget):
    def __init__(self, rect):
        log.debug(u'initialised pdf viewer')
        QtGui.QWidget.__init__(self, None)
        self.setWindowTitle("PDF Viewer")
        p = QtGui.QPalette()
        p.setColor(QtGui.QPalette.Background, QtCore.Qt.black);
        self.setPalette(p)
        self.setGeometry(rect) # QtGui.QApplication.desktop().screenGeometry())
        self.hide() 
        self.num_pages = 0
        self.pdf_images = []
        self.image_files = []
        self.is_blanked = False
        self.current_page = 0

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Down:
            self.next_page()
        elif event.key() == QtCore.Qt.Key_Up:
            self.previous_page()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.stop()

    def paintEvent(self, event):
        if self.is_blanked:
            return
        img = self.get_image(self.current_page)
        if img is None:
            return
        x = (self.frameSize().width() - img.width()) / 2
        y = (self.frameSize().height() - img.height()) / 2
        painter = QtGui.QPainter(self)
        painter.drawImage(x, y, img, 0, 0, 0, 0)

    def display(self):
        self.update()
        self.cache_image(self.current_page + 1)

    def start(self, images):
        log.debug(u'start pdfviewer')
        self.image_files = images
        self.num_pages = len(self.image_files)
        self.pdf_images = [None for i in range(self.num_pages)]
        self.showFullScreen()
        self.show()

    def stop(self):
        log.debug(u'stop pdfviewer')
        self.hide()

    def close(self):
        log.debug(u'close pdfviewer')
        self.stop()
        self.pdf_images = None
        self.image_files = None
    
    def blank(self):
        self.is_blanked = True
        self.update()

    def unblank(self):
        self.is_blanked = False
        self.update()

    def next_page(self):
        if self.current_page + 1 < self.num_pages:
            self.current_page += 1
            self.display()

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display()

    def show_page(self, idx):
        if idx < self.num_pages:
            self.current_page = idx
            self.display()

    def cache_image(self, idx):        
        if idx >= self.num_pages:
            return
        if self.image_files[idx] is None:
            return
        img = QtGui.QImage(self.image_files[idx])
        self.pdf_images[idx] = img
   
    def get_image(self, idx):
        self.cache_image(idx)
        return self.pdf_images[idx]

    def get_current_page(self):
        return self.current_page
