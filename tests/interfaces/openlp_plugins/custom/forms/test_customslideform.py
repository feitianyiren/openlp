"""
Module to test the EditCustomSlideForm.
"""
from unittest import TestCase

from PyQt4 import QtGui, QtCore

from openlp.core.common import Registry
from openlp.plugins.custom.forms.editcustomslideform import EditCustomSlideForm
from tests.interfaces import MagicMock, patch


class TestEditCustomSlideForm(TestCase):
    """
    Test the EditCustomSlideForm.
    """
    def setUp(self):
        """
        Create the UI
        """
        Registry.create()
        old_app_instance = QtCore.QCoreApplication.instance()
        if old_app_instance is None:
            self.app = QtGui.QApplication([])
        else:
            self.app = old_app_instance
        self.main_window = QtGui.QMainWindow()
        Registry().register('main_window', self.main_window)
        self.form = EditCustomSlideForm()

    def tearDown(self):
        """
        Delete all the C++ objects at the end so that we don't have a segfault
        """
        del self.form
        del self.main_window

    def basic_test(self):
        """
        Test if the dialog is correctly set up.
        """
        # GIVEN: A mocked QDialog.exec_() method
        with patch('PyQt4.QtGui.QDialog.exec_') as mocked_exec:
            # WHEN: Show the dialog.
            self.form.exec_()

            # THEN: The dialog should be empty.
            assert self.form.slide_text_edit.toPlainText() == '', 'There should not be any text in the text editor.'

    def set_text_test(self):
        """
        Test the set_text() method.
        """
        # GIVEN: A mocked QDialog.exec_() method
        with patch('PyQt4.QtGui.QDialog.exec_') as mocked_exec:
            mocked_set_focus = MagicMock()
            self.form.slide_text_edit.setFocus = mocked_set_focus
            wanted_text = 'THIS TEXT SHOULD BE SHOWN.'

            # WHEN: Show the dialog and set the text.
            self.form.exec_()
            self.form.set_text(wanted_text)

            # THEN: The dialog should show the text.
            assert self.form.slide_text_edit.toPlainText() == wanted_text, \
                'The text editor should show the correct text.'

            # THEN: The dialog should have focus.
            mocked_set_focus.assert_called_with()

