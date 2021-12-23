# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
from unittest.mock import Mock
from unittest.mock import patch

from menuClass import MenuClass
from discipleClass import DiscipleClass
from subjectClass import SubjectClass
from markClass import MarkClass


class MenuClassTest(unittest.TestCase):
    def setUp(self):
        self.temp = MenuClass
    #testing menu() function
    #0
    @patch('discipleClass.DiscipleClass.chooseAndDisplayDisciple')
    def test_menu_chooseAndDisplayDisciple(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.chooseAndDisplayDisciple("EN")
        self.assertTrue(mock_function.called)
    #1
    @patch('discipleClass.DiscipleClass.addDisciple')
    def test_menu_addDisciple(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.addDisciple("EN")
        self.assertTrue(mock_function.called)
    #2
    @patch('discipleClass.DiscipleClass.editDisciple')
    def test_menu_editDisciple(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.editDisciple("EN")
        self.assertTrue(mock_function.called)
    #3
    @patch('discipleClass.DiscipleClass.removeDisciple')
    def test_menu_removeDisciple(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.removeDisciple("EN")
        self.assertTrue(mock_function.called)
    #4
    @patch('menuClass.MenuClass.importDatabaseFromCSV')
    def test_menu_importDatabaseFromCSV(self, mock_function):
        mockClass = MenuClass()
        mockClass.importDatabaseFromCSV("EN")
        self.assertTrue(mock_function.called)
    #5
    @patch('menuClass.MenuClass.exportDatabaseToCSV')
    def test_menu_exportDatabaseFromCSV(self, mock_function):
        mockClass = MenuClass()
        mockClass.exportDatabaseToCSV("EN")
        self.assertTrue(mock_function.called)
    #6
    @patch('menuClass.MenuClass.menu')
    def test_menu_log_out(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN","6")
        self.assertTrue(mock_function.called)
    #testing choose_language() function
    def test_choose_language_english(self):
        try:
            self.temp.chooseLanguage("EN")
        except ExceptionType:
            self.fail("MenuClass.chooseLanguage(\"EN\") didn't redirect to menu")
    def test_choose_language_polish(self):
        try:
            self.temp.chooseLanguage("PL")
        except ExceptionType:
            self.fail("MenuClass.chooseLanguage(\"PL\") didn't redirect to menu")
    def exception_choose_language_other(self):
        self.assertRaises(Exception("Wrong language inputed."),self.temp.chooseLanguage("Uga Booga"))



if __name__ == '__main__':
    unittest.main()