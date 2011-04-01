# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4

###############################################################################
# OpenLP - Open Source Lyrics Projection                                      #
# --------------------------------------------------------------------------- #
# Copyright (c) 2008-2011 Raoul Snyman                                        #
# Portions copyright (c) 2008-2011 Tim Bentley, Jonathan Corwin, Michael      #
# Gorven, Scott Guerrieri, Matthias Hub, Meinert Jordan, Armin Köhler,        #
# Andreas Preikschat, Mattias Põldaru, Christian Richter, Philip Ridout,      #
# Maikel Stuivenberg, Martin Thompson, Jon Tibble, Frode Woldsund             #
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
The :mod:`cvsbible` modules provides a facility to import bibles from a set of
CSV files.

The module expects two mandatory files containing the books and the verses and
will accept an optional third file containing the testaments.

The format of the testament file is:

    <testament_id>,<testament_name>

    For example:

        1,Old Testament
        2,New Testament

The format of the books file is:

    <book_id>,<testament_id>,<book_name>,<book_abbreviation>

    For example

        1,1,Genesis,Gen
        2,1,Exodus,Exod
        ...
        40,2,Matthew,Matt

There are two acceptable formats of the verses file.  They are:

    <book_id>,<chapter_number>,<verse_number>,<verse_text>
    or
    <book_name>,<chapter_number>,<verse_number>,<verse_text>

    For example:

        1,1,1,"In the beginning God created the heaven and the earth."
        or
        "Genesis",1,2,"And the earth was without form, and void; and...."

All CSV files are expected to use a comma (',') as the delimeter and double
quotes ('"') as the quote symbol.
"""
import logging
import chardet
import csv

from openlp.core.lib import Receiver, translate
from openlp.plugins.bibles.lib.db import BibleDB, BiblesResourcesDB#, Testament

log = logging.getLogger(__name__)

class CSVBible(BibleDB):
    """
    This class provides a specialisation for importing of CSV Bibles.
    """
    def __init__(self, parent, **kwargs):
        """
        Loads a Bible from a set of CVS files.
        This class assumes the files contain all the information and
        a clean bible is being loaded.
        """
        log.info(self.__class__.__name__)
        BibleDB.__init__(self, parent, **kwargs)
        self.parent = parent
        #TODO: Delete unused code
        '''
        try:
            self.testamentsfile = kwargs[u'testamentsfile']
        except KeyError:
            self.testamentsfile = None
        '''
        self.booksfile = kwargs[u'booksfile']
        self.versesfile = kwargs[u'versefile']
    '''
    def setup_testaments(self):
        """
        Overrides parent method so we can handle importing a testament file.
        """
        if self.testamentsfile:
            self.wizard.progressBar.setMinimum(0)
            self.wizard.progressBar.setMaximum(2)
            self.wizard.progressBar.setValue(0)
            testaments_file = None
            try:
                details = get_file_encoding(self.testamentsfile)
                testaments_file = open(self.testamentsfile, 'rb')
                testaments_reader = csv.reader(testaments_file, delimiter=',',
                    quotechar='"')
                for line in testaments_reader:
                    if self.stop_import_flag:
                        break
                    self.wizard.incrementProgressBar(unicode(
                        translate('BibleDB.Wizard',
                        'Importing testaments... %s')) %
                        unicode(line[1], details['encoding']), 0)
                    self.save_object(Testament.populate(
                        name=unicode(line[1], details['encoding'])))
                Receiver.send_message(u'openlp_process_events')
            except (IOError, IndexError):
                log.exception(u'Loading testaments from file failed')
            finally:
                if testaments_file:
                    testaments_file.close()
            self.wizard.incrementProgressBar(unicode(translate(
                'BibleDB.Wizard', 'Importing testaments... done.')), 2)
        else:
            BibleDB.setup_testaments(self)
    '''
    def do_import(self):
        """
        Import the bible books and verses.
        """
        self.wizard.progressBar.setValue(0)
        self.wizard.progressBar.setMinimum(0)
        self.wizard.progressBar.setMaximum(66)
        success = True
        language = self.parent.mediaItem.languageDialog()
        if not language:
            log.exception(u'Importing books from %s " '\
                'failed' % self.booksfile)
            return False
        language = BiblesResourcesDB.get_language(language)
        language_id = language[u'id']
        self.create_meta(u'language_id', language_id)
        books_file = None
        book_list = {}
        # Populate the Tables
        try:
            details = get_file_encoding(self.booksfile)
            books_file = open(self.booksfile, 'r')
            books_reader = csv.reader(books_file, delimiter=',', quotechar='"')
            for line in books_reader:
                if self.stop_import_flag:
                    break
                self.wizard.incrementProgressBar(unicode(
                    translate('BibleDB.Wizard', 'Importing books... %s')) %
                    unicode(line[2], details['encoding']))
                book_ref_id = self.parent.manager.get_book_ref_id_by_name(
                    unicode(line[2], details['encoding']), language_id)
                if not book_ref_id:
                    log.exception(u'Importing books from %s " '\
                        'failed' % self.booksfile)
                    return False
                book_details = BiblesResourcesDB.get_book_by_id(book_ref_id)
                self.create_book(unicode(line[2], details['encoding']),
                    book_ref_id, book_details[u'testament_id'])
                book_list[int(line[0])] = unicode(line[2], details['encoding'])
            Receiver.send_message(u'openlp_process_events')
        except (IOError, IndexError):
            log.exception(u'Loading books from file failed')
            success = False
        finally:
            if books_file:
                books_file.close()
        if self.stop_import_flag or not success:
            return False
        self.wizard.progressBar.setValue(0)
        self.wizard.progressBar.setMaximum(67)
        verse_file = None
        try:
            book_ptr = None
            details = get_file_encoding(self.versesfile)
            verse_file = open(self.versesfile, 'rb')
            verse_reader = csv.reader(verse_file, delimiter=',', quotechar='"')
            for line in verse_reader:
                if self.stop_import_flag:
                    break
                try:
                    line_book = book_list[int(line[0])]
                except ValueError:
                    line_book = unicode(line[0], details['encoding'])
                if book_ptr != line_book:
                    book = self.get_book(line_book)
                    book_ptr = book.name
                    self.wizard.incrementProgressBar(unicode(translate(
                        'BibleDB.Wizard', 'Importing verses from %s...',
                        'Importing verses from <book name>...')) % book.name)
                    self.session.commit()
                try:
                    verse_text = unicode(line[3], details['encoding'])
                except UnicodeError:
                    verse_text = unicode(line[3], u'cp1252')
                self.create_verse(book.id, line[1], line[2], verse_text)
            self.wizard.incrementProgressBar(translate('BibleDB.Wizard',
                'Importing verses... done.'))
            Receiver.send_message(u'openlp_process_events')
            self.session.commit()
        except IOError:
            log.exception(u'Loading verses from file failed')
            success = False
        finally:
            if verse_file:
                verse_file.close()
        if self.stop_import_flag:
            return False
        else:
            return success

def get_file_encoding(filename):
    """
    Utility function to get the file encoding.
    """
    detect_file = None
    try:
        detect_file = open(filename, 'r')
        details = chardet.detect(detect_file.read(1024))
    except IOError:
        log.exception(u'Error detecting file encoding')
    finally:
        if detect_file:
            detect_file.close()
    return details
