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

import os, os.path
import sys

from bibleOSISimpl import BibleOSISImpl
from bibleCSVimpl import BibleCSVImpl
from bibleDBimpl import BibleDBImpl
from bibleHTTPimpl import BibleHTTPImpl

import logging

class BibleManager():
    global log
    log=logging.getLogger("BibleMgr")
    log.info("Bible manager loaded")
    def __init__(self, config):
        """
        Finds all the bibles defined for the system
        Creates an Interface Object for each bible containing connection information
        Throws Exception if no Bibles are found.

        Init confirms the bible exists and stores the database path.
        """
        self.config = config
        log.debug( "Bible Initialising")
        self.bibleDBCache = {}   # dict of bible database classes
        self.bibleHTTPCache = {} # dict of bible http readers
        self.biblePath = self.config.get_data_path()
        self.proxyname = self.config.get_config("proxy name") #get proxy name for screen
        self.bibleSuffix = self.config.get_config("suffix name", u'bible3')
        self.dialogobject = None
        
        files = self.config.get_files()
        log.debug("Bible Files %s",  files )

        for f in files:
            nme = f.split('.')
            bname = nme[0]
            self.bibleDBCache[bname] = BibleDBImpl(self.biblePath, bname, self.bibleSuffix)
            biblesource = self.bibleDBCache[bname].get_meta("WEB") # look to see if lazy load bible exists and get create getter.
            if biblesource:
                print biblesource
                nhttp = BibleHTTPImpl()
                nhttp.setBibleSource(biblesource)  # tell The Server where to get the verses from.
                self.bibleHTTPCache[bname] = nhttp
                proxy = self.bibleDBCache[bname].get_meta("proxy") # look to see if lazy load bible exists and get create getter.
                nhttp.setProxy(proxy)  # tell The Server where to get the verses from.
        #

        log.debug( "Bible Initialised")

    def process_dialog(self, dialogobject):
        self.dialogobject = dialogobject

    def register_HTTP_bible(self, biblename, biblesource, mode="lazy", proxyurl=None, proxyid=None, proxypass=None):
        """
        Return a list of bibles from a given URL.
        The selected Bible can then be registered and LazyLoaded into a database
        """
        log.debug( "register_HTTP_bible %s,%s,%s,%s,%s", biblename, biblesource, proxyurl,  proxyid, proxypass, mode)
        if self._is_new_bible(biblename):
            nbible = BibleDBImpl(self.biblePath, biblename, self.bibleSuffix) # Create new Bible
            nbible.createTables() # Create Database
            self.bibleDBCache[biblename] = nbible

            nhttp = BibleHTTPImpl()
            nhttp.setBibleSource(biblesource)
            self.bibleHTTPCache[biblename] = nhttp
            nbible.save_meta("WEB", biblesource) # register a lazy loading interest
            if proxyurl != None:
                nbible.save_meta("proxy", proxyurl) # store the proxy URL
                nhttp.setProxy(proxyurl)
            if proxyid != None:
                nbible.save_meta("proxyid", proxyid) # store the proxy userid
            if proxypass != None:
                nbible.save_meta("proxypass", proxypass) # store the proxy password


    def register_CVS_file_bible(self, biblename, booksfile, versefile):
        """
        Method to load a bible from a set of files into a database.
        If the database exists it is deleted and the database is reloaded
        from scratch.
        """
        if self._is_new_bible(biblename):
            nbible = BibleDBImpl(self.biblePath, biblename, self.bibleSuffix) # Create new Bible
            nbible.createTables() # Create Database
            self.bibleDBCache[biblename] = nbible # cache the database for use later
            bcsv = BibleCSVImpl(nbible) # create the loader and pass in the database
            bcsv.load_data(booksfile, versefile)

    def register_OSIS_file_bible(self, biblename, osisfile):
        """
        Method to load a bible from a osis xml file extracted from Sword bible viewer.
        If the database exists it is deleted and the database is reloaded
        from scratch.
        """
        log.debug( "register_OSIS_file_bible %s , %s", biblename, osisfile)        
        if self._is_new_bible(biblename):
            nbible = BibleDBImpl(self.biblePath, biblename, self.bibleSuffix) # Create new Bible
            nbible.createTables() # Create Database
            self.bibleDBCache[biblename] = nbible # cache the database for use later
            bcsv = BibleOSISImpl(self.biblePath, nbible) # create the loader and pass in the database
            bcsv.loadData(osisfile, self.dialogobject)


#    def loadBible(self,biblename):
#        """
#        Downloads all the books of the bible
#        and loads it into the database
#        """
#        log.debug( "loadBible %s", biblename)
#        bookabbrev = ""
#        for bookname in self.listOfBooks:
#            cptrs = self.booksChapters[ self.booksOfBible[bookname]]
#            log.debug( "book and chapter %s %s", bookname , self.booksChapters[ self.booksOfBible[bookname]] )
#            for chptr in range(1 , int(cptrs)):  # loop through all the chapters in book
#                c = self.bibleDBCache[biblename].getBibleChapter(bookname, chptr) # check to see if book/chapter exists
#                log.debug( "got chapter %s", c)
#                if not c:
#                    bookid = self.booksOfBible[bookname] # convert to id  ie Genesis --> 1  Revelation --> 73
#                    log.debug( "missing %s,%s", bookname, chptr)
#                    self._loadBook(biblename,bookid, bookname, bookabbrev)
#                    self._loadChapter(biblename,bookid,  bookname, chptr)

    def get_bibles(self, mode="full"):
        """
        Returns a list of Books of the bible
        """
        r=[]
        for b ,  o in self.bibleDBCache.iteritems():
            r.append(b)
        return r

    def get_bible_books(self,bible):
        """
        Returns a list of the books of the bible from the database
        """
        log.debug("get_bible_books %s", bible)
        return self.bibleDBCache[bible].get_bible_books()

    def get_book_chapter_count(self, bible,  book):
        """
        Returns the number of Chapters for a given book
        """
        log.debug( "get_book_chapter_count %s,%s", bible, book)
        return self.bibleDBCache[bible].get_max_bible_book_chapter(book)

    def get_book_verse_count(self, bible, book, chapter):
        """
        Returns all the number of verses for a given
        book and chapterMaxBibleBookVerses
        """
        log.debug( "get_book_verse_count %s,%s,%s", bible, book,  chapter)
        return self.bibleDBCache[bible].get_max_bible_book_verses(book, chapter)

    def get_verse_from_text(self, bible, versetext):
        """
        Returns all the number of verses for a given
        book and chapterMaxBibleBookVerses
        """
        log.debug( "get_verses_from_text %s,%s", bible, versetext)
        return self.bibleDBCache[bible].get_verses_from_text(versetext)

    def save_meta_data(self, bible, version, copyright, permissions):
        """
        Saves the bibles meta data
        """
        log.debug( "save_meta %s,%s, %s,%s", bible,  version, copyright, permissions)
        self.bibleDBCache[bible].save_meta("Version", version)
        self.bibleDBCache[bible].save_meta("Copyright", copyright)
        self.bibleDBCache[bible].save_meta("Permissins", permissions)

    def get_meta_data(self, bible, key):
        """
        Returns the meta data for a given key
        """
        log.debug( "get_meta %s,%s", bible,  key)
        self.bibleDBCache[bible].get_meta(key)

    def get_verse_text(self, bible, bookname, schapter, echapter, sverse, everse = 0 ):
        """
        Returns a list of verses for a given Book, Chapter and ranges of verses.
        If the end verse(everse) is less then the start verse(sverse)
        then only one verse is returned
        bible        - Which bible to use.
        Rest can be guessed at !
        """
        text  = []
        #log.debug( self.bibleDBCache)
        #log.debug( self.bibleHTTPCache)
        log.debug( "get_verse_text %s,%s,%s,%s,%s,%s",  bible,bookname,  schapter,echapter, sverse, everse)
#        bookid = self.booksOfBible[bookname] # convert to id  ie Genesis --> 1  Revelation --> 73
#        # SORT OUT BOOKNAME BOOK ID.
#        # NAME COMES IN TO ID AND BACK TO NAME ?
#        c = self.bibleDBCache[bible].getBibleChapter(bookname, chapter) # check to see if book/chapter exists
#        bookabbrev = ""
#        log.debug( "Bible Chapter %s", c )
#        if not c:
#            self._loadBook(bible,bookid, bookname, bookabbrev)
#            self._loadChapter(bible, bookid,bookname, chapter)
        if schapter == echapter:
            text = self.bibleDBCache[bible].get_bible_text(bookname, schapter, sverse, everse)
        else:
            for i in range (schapter, echapter + 1):
                if i == schapter:
                    start = sverse
                    end = self.get_book_verse_count(bible, bookname,i )[0]
                elif i == echapter:
                    start = 1
                    end = everse
                else:
                    start = 1
                    end = self.get_book_verse_count(bible, bookname,i )[0]

                txt = self.bibleDBCache[bible].get_bible_text(bookname, i, start, end)
                text.extend(txt)
        return text

    def _load_book(self, bible, bookid, bookname, bookabbrev):
        log.debug( "load_book %s,%s,%s,%s", bible, bookid, bookname, bookabbrev)
        cl = self.bibleDBCache[bible].get_bible_book(bookname)
        log.debug( "get bible book %s" , cl)
        if not cl :
            self.bibleDBCache[bible].create_book(bookid, bookname, bookabbrev)

    def _loadChapter(self, bible, bookid, bookname, chapter):
        log.debug( "load_chapter %s,%s,%s,%s", bible, bookid,bookname, chapter)
        try :
            chaptlist = self.bibleHTTPCache[bible].get_bible_chapter(bible, bookid,bookname, chapter)
            self.bibleDBCache[bible].create_chapter(bookname, chapter, chaptlist)
        except :
            log.error("Errow thrown %s", sys.exc_info()[1])

    def _is_new_bible(self, name):
        """
        Check cache to see if new bible
        """
        for b ,  o in self.bibleDBCache.iteritems():
            log.debug( b )
            if b == name :
                return False
        return True
