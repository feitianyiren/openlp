# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4

###############################################################################
# OpenLP - Open Source Lyrics Projection                                      #
# --------------------------------------------------------------------------- #
# Copyright (c) 2008-2011 Raoul Snyman                                        #
# Portions copyright (c) 2008-2011 Tim Bentley, Jonathan Corwin, Michael      #
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
import os

from PyQt4 import QtCore, QtGui

from openlp.core.lib import translate, BackgroundType, BackgroundGradientType, \
    Receiver
from openlp.core.utils import get_images_filter
from themewizard import Ui_ThemeWizard

log = logging.getLogger(__name__)

class ThemeForm(QtGui.QWizard, Ui_ThemeWizard):
    """
    This is the Bible Import Wizard, which allows easy importing of Bibles
    into OpenLP from other formats like OSIS, CSV and OpenSong.
    """
    log.info(u'ThemeWizardForm loaded')

    def __init__(self, parent):
        """
        Instantiate the wizard, and run any extra setup we need to.

        ``parent``
            The QWidget-derived parent of the wizard.
        """
        QtGui.QWizard.__init__(self, parent)
        self.thememanager = parent
        self.setupUi(self)
        self.registerFields()
        self.accepted = False
        self.updateThemeAllowed = True
        QtCore.QObject.connect(self.backgroundComboBox,
            QtCore.SIGNAL(u'currentIndexChanged(int)'),
            self.onBackgroundComboBoxCurrentIndexChanged)
        QtCore.QObject.connect(self.gradientComboBox,
            QtCore.SIGNAL(u'currentIndexChanged(int)'),
            self.onGradientComboBoxCurrentIndexChanged)
        QtCore.QObject.connect(self.colorButton,
            QtCore.SIGNAL(u'clicked()'),
            self.onColorButtonClicked)
        QtCore.QObject.connect(self.gradientStartButton,
            QtCore.SIGNAL(u'clicked()'),
            self.onGradientStartButtonClicked)
        QtCore.QObject.connect(self.gradientEndButton,
            QtCore.SIGNAL(u'clicked()'),
            self.onGradientEndButtonClicked)
        QtCore.QObject.connect(self.imageBrowseButton,
            QtCore.SIGNAL(u'clicked()'),
            self.onImageBrowseButtonClicked)
        QtCore.QObject.connect(self.mainColorButton,
            QtCore.SIGNAL(u'clicked()'),
            self.onMainColorButtonClicked)
        QtCore.QObject.connect(self.outlineColorButton,
            QtCore.SIGNAL(u'clicked()'),
            self.onOutlineColorButtonClicked)
        QtCore.QObject.connect(self.shadowColorButton,
            QtCore.SIGNAL(u'clicked()'),
            self.onShadowColorButtonClicked)
        QtCore.QObject.connect(self.outlineCheckBox,
            QtCore.SIGNAL(u'stateChanged(int)'),
            self.onOutlineCheckCheckBoxStateChanged)
        QtCore.QObject.connect(self.shadowCheckBox,
            QtCore.SIGNAL(u'stateChanged(int)'),
            self.onShadowCheckCheckBoxStateChanged)
        QtCore.QObject.connect(self.footerColorButton,
            QtCore.SIGNAL(u'clicked()'),
            self.onFooterColorButtonClicked)
        QtCore.QObject.connect(self.mainPositionCheckBox,
            QtCore.SIGNAL(u'stateChanged(int)'),
            self.onMainPositionCheckBoxStateChanged)
        QtCore.QObject.connect(self.footerPositionCheckBox,
            QtCore.SIGNAL(u'stateChanged(int)'),
            self.onFooterPositionCheckBoxStateChanged)
        QtCore.QObject.connect(self,
            QtCore.SIGNAL(u'currentIdChanged(int)'),
            self.onCurrentIdChanged)
        QtCore.QObject.connect(Receiver.get_receiver(),
            QtCore.SIGNAL(u'theme_line_count'),
            self.updateLinesText)
        QtCore.QObject.connect(self.mainSizeSpinBox,
            QtCore.SIGNAL(u'valueChanged(int)'),
            self.calculateLines)
        QtCore.QObject.connect(self.lineSpacingSpinBox,
            QtCore.SIGNAL(u'valueChanged(int)'),
            self.calculateLines)
        QtCore.QObject.connect(self.outlineSizeSpinBox,
            QtCore.SIGNAL(u'valueChanged(int)'),
            self.calculateLines)
        QtCore.QObject.connect(self.shadowSizeSpinBox,
            QtCore.SIGNAL(u'valueChanged(int)'),
            self.calculateLines)
        QtCore.QObject.connect(self.mainFontComboBox,
            QtCore.SIGNAL(u'activated(int)'),
            self.calculateLines)
        QtCore.QObject.connect(self, QtCore.SIGNAL(u'accepted()'), self.accept)

    def setDefaults(self):
        """
        Set up display at start of theme edit.
        """
        self.restart()
        self.accepted = False
        self.setBackgroundPageValues()
        self.setMainAreaPageValues()
        self.setFooterAreaPageValues()
        self.setAlignmentPageValues()
        self.setPositionPageValues()
        self.setPreviewPageValues()

    def registerFields(self):
        """
        Map field names to screen names,
        """
        self.backgroundPage.registerField(
            u'background_type', self.backgroundComboBox)
        self.backgroundPage.registerField(
            u'color', self.colorButton)
        self.backgroundPage.registerField(
            u'grandient_start', self.gradientStartButton)
        self.backgroundPage.registerField(
            u'grandient_end', self.gradientEndButton)
        self.backgroundPage.registerField(
            u'background_image', self.imageFileEdit)
        self.backgroundPage.registerField(
            u'gradient', self.gradientComboBox)
        self.mainAreaPage.registerField(
            u'mainColorButton', self.mainColorButton)
        self.mainAreaPage.registerField(
            u'mainSizeSpinBox', self.mainSizeSpinBox)
        self.mainAreaPage.registerField(
            u'lineSpacingSpinBox', self.lineSpacingSpinBox)
        self.mainAreaPage.registerField(
            u'outlineCheckBox', self.outlineCheckBox)
        self.mainAreaPage.registerField(
            u'outlineColorButton', self.outlineColorButton)
        self.mainAreaPage.registerField(
            u'outlineSizeSpinBox', self.outlineSizeSpinBox)
        self.mainAreaPage.registerField(
            u'shadowCheckBox', self.shadowCheckBox)
        self.mainAreaPage.registerField(
            u'mainBoldCheckBox', self.mainBoldCheckBox)
        self.mainAreaPage.registerField(
            u'mainItalicsCheckBox', self.mainItalicsCheckBox)
        self.mainAreaPage.registerField(
            u'shadowColorButton', self.shadowColorButton)
        self.mainAreaPage.registerField(
            u'shadowSizeSpinBox', self.shadowSizeSpinBox)
        self.mainAreaPage.registerField(
            u'footerSizeSpinBox', self.footerSizeSpinBox)
        self.areaPositionPage.registerField(
            u'mainPositionX', self.mainXSpinBox)
        self.areaPositionPage.registerField(
            u'mainPositionY', self.mainYSpinBox)
        self.areaPositionPage.registerField(
            u'mainPositionWidth', self.mainWidthSpinBox)
        self.areaPositionPage.registerField(
            u'mainPositionHeight', self.mainHeightSpinBox)
        self.areaPositionPage.registerField(
            u'footerPositionX', self.footerXSpinBox)
        self.areaPositionPage.registerField(
            u'footerPositionY', self.footerYSpinBox)
        self.areaPositionPage.registerField(
            u'footerPositionWidth', self.footerWidthSpinBox)
        self.areaPositionPage.registerField(
            u'footerPositionHeight', self.footerHeightSpinBox)
        self.backgroundPage.registerField(
            u'horizontal', self.horizontalComboBox)
        self.backgroundPage.registerField(
            u'vertical', self.verticalComboBox)
        self.backgroundPage.registerField(
            u'slideTransition', self.transitionsCheckBox)
        self.backgroundPage.registerField(
            u'name', self.themeNameEdit)

    def calculateLines(self):
        """
        Calculate the number of lines on a page by rendering text
        """
        # Do not trigger on start up
        if self.currentPage != self.welcomePage:
            self.updateTheme()
            frame = self.thememanager.generateImage(self.theme, True)

    def updateLinesText(self, lines):
        """
        Updates the lines on a page on the wizard
        """
        self.mainLineCountLabel.setText(unicode(translate('OpenLP.ThemeForm', \
            '(%d lines per slide)' % int(lines))))

    def resizeEvent(self, event=None):
        """
        Rescale the theme preview thumbnail on resize events.
        """
        if not event:
            event = QtGui.QResizeEvent(self.size(), self.size())
        QtGui.QWizard.resizeEvent(self, event)
        if self.currentPage() == self.previewPage:
            frameWidth = self.previewBoxLabel.lineWidth()
            pixmapWidth = self.previewArea.width() - 2 * frameWidth
            pixmapHeight = self.previewArea.height() - 2 * frameWidth
            aspectRatio = float(pixmapWidth) / pixmapHeight
            if aspectRatio < self.displayAspectRatio:
                pixmapHeight = int(pixmapWidth / self.displayAspectRatio + 0.5)
            else:
                pixmapWidth = int(pixmapHeight * self.displayAspectRatio + 0.5)
            self.previewBoxLabel.setFixedSize(pixmapWidth + 2 * frameWidth,
                pixmapHeight + 2 * frameWidth)

    def onCurrentIdChanged(self, pageId):
        """
        Detects Page changes and updates as approprate.
        """
        if self.page(pageId) == self.previewPage:
            self.updateTheme()
            frame = self.thememanager.generateImage(self.theme)
            self.previewBoxLabel.setPixmap(QtGui.QPixmap.fromImage(frame))
            self.displayAspectRatio = float(frame.width()) / frame.height()
            self.resizeEvent()

    def onOutlineCheckCheckBoxStateChanged(self, state):
        """
        Change state as Outline check box changed
        """
        if state == QtCore.Qt.Checked:
            self.theme.font_main_outline = True
        else:
            self.theme.font_main_outline = False
        self.outlineColorButton.setEnabled(self.theme.font_main_outline)
        self.outlineSizeSpinBox.setEnabled(self.theme.font_main_outline)
        self.calculateLines()

    def onShadowCheckCheckBoxStateChanged(self, state):
        """
        Change state as Shadow check box changed
        """
        if state == QtCore.Qt.Checked:
            self.theme.font_main_shadow = True
        else:
            self.theme.font_main_shadow = False
        self.shadowColorButton.setEnabled(self.theme.font_main_shadow)
        self.shadowSizeSpinBox.setEnabled(self.theme.font_main_shadow)
        self.calculateLines()

    def onMainPositionCheckBoxStateChanged(self, value):
        """
        Change state as Main Area Position check box changed
        """
        self.theme.font_main_override = (value == QtCore.Qt.Checked)

    def onFooterPositionCheckBoxStateChanged(self, value):
        """
        Change state as Footer Area Position check box changed
        """
        self.theme.font_footer_override = (value == QtCore.Qt.Checked)

    def exec_(self, edit=False):
        """
        Run the wizard.
        """
        log.debug(u'Editing theme %s' % self.theme.theme_name)
        self.updateThemeAllowed = False
        self.setDefaults()
        self.updateThemeAllowed = True
        self.themeNameLabel.setVisible(not edit)
        self.themeNameEdit.setVisible(not edit)
        if edit:
            self.setWindowTitle(unicode(translate('OpenLP.ThemeWizard',
                'Edit Theme %s')) % self.theme.theme_name)
            self.next()
        else:
            self.setWindowTitle(translate('OpenLP.ThemeWizard', 'New Theme'))
        return QtGui.QWizard.exec_(self)

    def initializePage(self, id):
        """
        Set up the pages for Initial run through dialog
        """
        log.debug(u'initializePage %s' % id)
        wizardPage = self.page(id)
        if wizardPage == self.backgroundPage:
            self.setBackgroundPageValues()
        elif wizardPage == self.mainAreaPage:
            self.setMainAreaPageValues()
        elif wizardPage == self.footerAreaPage:
            self.setFooterAreaPageValues()
        elif wizardPage == self.alignmentPage:
            self.setAlignmentPageValues()
        elif wizardPage == self.areaPositionPage:
            self.setPositionPageValues()

    def setBackgroundPageValues(self):
        """
        Handle the display and state of the Background page.
        """
        if self.theme.background_type == \
            BackgroundType.to_string(BackgroundType.Solid):
            self.colorButton.setStyleSheet(u'background-color: %s' %
                    self.theme.background_color)
            self.setField(u'background_type', QtCore.QVariant(0))
        elif self.theme.background_type == \
            BackgroundType.to_string(BackgroundType.Gradient):
            self.gradientStartButton.setStyleSheet(u'background-color: %s' %
                    self.theme.background_start_color)
            self.gradientEndButton.setStyleSheet(u'background-color: %s' %
                    self.theme.background_end_color)
            self.setField(u'background_type', QtCore.QVariant(1))
        else:
            self.imageFileEdit.setText(self.theme.background_filename)
            self.setField(u'background_type', QtCore.QVariant(2))
        if self.theme.background_direction == \
            BackgroundGradientType.to_string(BackgroundGradientType.Horizontal):
            self.setField(u'gradient', QtCore.QVariant(0))
        elif self.theme.background_direction == \
            BackgroundGradientType.to_string(BackgroundGradientType.Vertical):
            self.setField(u'gradient', QtCore.QVariant(1))
        elif self.theme.background_direction == \
            BackgroundGradientType.to_string(BackgroundGradientType.Circular):
            self.setField(u'gradient', QtCore.QVariant(2))
        elif self.theme.background_direction == \
            BackgroundGradientType.to_string(BackgroundGradientType.LeftTop):
            self.setField(u'gradient', QtCore.QVariant(3))
        else:
            self.setField(u'gradient', QtCore.QVariant(4))

    def setMainAreaPageValues(self):
        """
        Handle the display and state of the Main Area page.
        """
        self.mainFontComboBox.setCurrentFont(
            QtGui.QFont(self.theme.font_main_name))
        self.mainColorButton.setStyleSheet(u'background-color: %s' %
            self.theme.font_main_color)
        self.setField(u'mainSizeSpinBox',
            QtCore.QVariant(self.theme.font_main_size))
        self.setField(u'lineSpacingSpinBox',
            QtCore.QVariant(self.theme.font_main_line_adjustment))
        self.setField(u'outlineCheckBox',
            QtCore.QVariant(self.theme.font_main_outline))
        self.outlineColorButton.setStyleSheet(u'background-color: %s' %
            self.theme.font_main_outline_color)
        self.setField(u'outlineSizeSpinBox',
            QtCore.QVariant(self.theme.font_main_outline_size))
        self.setField(u'shadowCheckBox',
            QtCore.QVariant(self.theme.font_main_shadow))
        self.shadowColorButton.setStyleSheet(u'background-color: %s' %
            self.theme.font_main_shadow_color)
        self.setField(u'shadowSizeSpinBox',
            QtCore.QVariant(self.theme.font_main_shadow_size))
        self.setField(u'mainBoldCheckBox',
            QtCore.QVariant(self.theme.font_main_bold))
        self.setField(u'mainItalicsCheckBox',
            QtCore.QVariant(self.theme.font_main_italics))

    def setFooterAreaPageValues(self):
        """
        Handle the display and state of the Footer Area page.
        """
        self.footerFontComboBox.setCurrentFont(
            QtGui.QFont(self.theme.font_main_name))
        self.footerColorButton.setStyleSheet(u'background-color: %s' %
            self.theme.font_footer_color)
        self.setField(u'footerSizeSpinBox',
            QtCore.QVariant(self.theme.font_footer_size))

    def setPositionPageValues(self):
        """
        Handle the display and state of the Position page.
        """
        # Main Area
        self.mainPositionCheckBox.setChecked(not self.theme.font_main_override)
        self.setField(u'mainPositionX', QtCore.QVariant(self.theme.font_main_x))
        self.setField(u'mainPositionY', QtCore.QVariant(self.theme.font_main_y))
        self.setField(u'mainPositionHeight',
            QtCore.QVariant(self.theme.font_main_height))
        self.setField(u'mainPositionWidth',
            QtCore.QVariant(self.theme.font_main_width))
        # Footer
        self.footerPositionCheckBox.setChecked(
            not self.theme.font_footer_override)
        self.setField(u'footerPositionX',
            QtCore.QVariant(self.theme.font_footer_x))
        self.setField(u'footerPositionY',
            QtCore.QVariant(self.theme.font_footer_y))
        self.setField(u'footerPositionHeight',
            QtCore.QVariant(self.theme.font_footer_height))
        self.setField(u'footerPositionWidth',
            QtCore.QVariant(self.theme.font_footer_width))

    def setAlignmentPageValues(self):
        """
        Handle the display and state of the Alignments page.
        """
        self.setField(u'horizontal',
            QtCore.QVariant(self.theme.display_horizontal_align))
        self.setField(u'vertical',
            QtCore.QVariant(self.theme.display_vertical_align))
        self.setField(u'slideTransition',
            QtCore.QVariant(self.theme.display_slide_transition))

    def setPreviewPageValues(self):
        """
        Handle the display and state of the Preview page.
        """
        self.setField(u'name', QtCore.QVariant(self.theme.theme_name))

    def onBackgroundComboBoxCurrentIndexChanged(self, index):
        """
        Background style Combo box has changed.
        """
        self.theme.background_type = BackgroundType.to_string(index)
        self.setBackgroundPageValues()

    def onGradientComboBoxCurrentIndexChanged(self, index):
        """
        Background gradient Combo box has changed.
        """
        self.theme.background_direction = \
            BackgroundGradientType.to_string(index)
        self.setBackgroundPageValues()

    def onColorButtonClicked(self):
        """
        Background / Gradient 1 Color button pushed.
        """
        self.theme.background_color = \
            self._colorButton(self.theme.background_color)
        self.setBackgroundPageValues()

    def onGradientStartButtonClicked(self):
        """
        Gradient 2 Color button pushed.
        """
        self.theme.background_start_color = \
            self._colorButton(self.theme.background_start_color)
        self.setBackgroundPageValues()

    def onGradientEndButtonClicked(self):
        """
        Gradient 2 Color button pushed.
        """
        self.theme.background_end_color = \
            self._colorButton(self.theme.background_end_color)
        self.setBackgroundPageValues()

    def onImageBrowseButtonClicked(self):
        """
        Background Image button pushed.
        """
        images_filter = get_images_filter()
        images_filter = '%s;;%s (*.*) (*)' % (images_filter,
            translate('OpenLP.ThemeForm', 'All Files'))
        filename = QtGui.QFileDialog.getOpenFileName(self,
            translate('OpenLP.ThemeForm', 'Select Image'), u'',
            images_filter)
        if filename:
            self.theme.background_filename = unicode(filename)
        self.setBackgroundPageValues()

    def onMainColorButtonClicked(self):
        self.theme.font_main_color = \
            self._colorButton(self.theme.font_main_color)
        self.setMainAreaPageValues()

    def onOutlineColorButtonClicked(self):
        self.theme.font_main_outline_color = \
            self._colorButton(self.theme.font_main_outline_color)
        self.setMainAreaPageValues()

    def onShadowColorButtonClicked(self):
        self.theme.font_main_shadow_color = \
            self._colorButton(self.theme.font_main_shadow_color)
        self.setMainAreaPageValues()

    def onFooterColorButtonClicked(self):
        self.theme.font_footer_color = \
            self._colorButton(self.theme.font_footer_color)
        self.setFooterAreaPageValues()

    def updateTheme(self):
        """
        Update the theme object from the UI for fields not already updated
        when the are changed.
        """
        if not self.updateThemeAllowed:
            return
        log.debug(u'updateTheme')
        # main page
        self.theme.font_main_name = \
            unicode(self.mainFontComboBox.currentFont().family())
        self.theme.font_main_size = \
            self.field(u'mainSizeSpinBox').toInt()[0]
        self.theme.font_main_line_adjustment = \
            self.field(u'lineSpacingSpinBox').toInt()[0]
        self.theme.font_main_outline_size = \
            self.field(u'outlineSizeSpinBox').toInt()[0]
        self.theme.font_main_shadow_size = \
            self.field(u'shadowSizeSpinBox').toInt()[0]
        self.theme.font_main_bold = \
            self.field(u'mainBoldCheckBox').toBool()
        self.theme.font_main_italics = \
            self.field(u'mainItalicsCheckBox').toBool()
        # footer page
        self.theme.font_footer_name = \
            unicode(self.footerFontComboBox.currentFont().family())
        self.theme.font_footer_size = \
            self.field(u'footerSizeSpinBox').toInt()[0]
        # position page
        self.theme.font_main_x = self.field(u'mainPositionX').toInt()[0]
        self.theme.font_main_y = self.field(u'mainPositionY').toInt()[0]
        self.theme.font_main_height = \
            self.field(u'mainPositionHeight').toInt()[0]
        self.theme.font_main_width = self.field(u'mainPositionWidth').toInt()[0]
        self.theme.font_footer_x = self.field(u'footerPositionX').toInt()[0]
        self.theme.font_footer_y = self.field(u'footerPositionY').toInt()[0]
        self.theme.font_footer_height = \
            self.field(u'footerPositionHeight').toInt()[0]
        self.theme.font_footer_width = \
            self.field(u'footerPositionWidth').toInt()[0]
        # position page
        self.theme.display_horizontal_align = \
            self.horizontalComboBox.currentIndex()
        self.theme.display_vertical_align = \
            self.verticalComboBox.currentIndex()
        self.theme.display_slide_transition = \
            self.field(u'slideTransition').toBool()

    def accept(self):
        """
        Lets save the them as Finish has been pressed
        """
        # Some reason getting double submission.
        # Hack to stop it for now.
        if self.accepted:
            return
        # Save the theme name
        self.theme.theme_name = \
            unicode(self.field(u'name').toString())
        if not self.theme.theme_name:
            QtGui.QMessageBox.critical(self,
                translate('OpenLP.ThemeForm', 'Theme Name Missing'),
                translate('OpenLP.ThemeForm',
                    'There is no name for this theme. '
                    'Please enter one.'),
                (QtGui.QMessageBox.Ok),
                QtGui.QMessageBox.Ok)
            return
        if self.theme.theme_name == u'-1' or self.theme.theme_name == u'None':
            QtGui.QMessageBox.critical(self,
                translate('OpenLP.ThemeForm', 'Theme Name Invalid'),
                translate('OpenLP.ThemeForm',
                    'Invalid theme name. '
                    'Please enter one.'),
                (QtGui.QMessageBox.Ok),
                QtGui.QMessageBox.Ok)
            return
        self.accepted = True
        saveFrom = None
        saveTo = None
        if self.theme.background_type == \
            BackgroundType.to_string(BackgroundType.Image):
            filename = \
                os.path.split(unicode(self.theme.background_filename))[1]
            saveTo = os.path.join(self.path, self.theme.theme_name, filename)
            saveFrom = self.theme.background_filename
        if self.thememanager.saveTheme(self.theme, saveFrom, saveTo):
            return QtGui.QDialog.accept(self)

    def _colorButton(self, field):
        """
        Handle Color buttons
        """
        new_color = QtGui.QColorDialog.getColor(
            QtGui.QColor(field), self)
        if new_color.isValid():
            field = new_color.name()
        return field
