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
    @patch('discipleClass.DiscipleClass.chooseAndDisplayDisciple')
    def test_menu_chooseAndDisplayDisciple(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.chooseAndDisplayDisciple("EN")
        self.assertTrue(mock_function.called)

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
