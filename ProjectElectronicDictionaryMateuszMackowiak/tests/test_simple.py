# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from menuClass import MenuClass


class MenuClassTest(unittest.TestCase):
    def setUp(self):
        self.temp = MenuClass
    def test_menu_log_out(self):
        self.assertEqual(self.temp.menu("EN","6"), 0)
    def test_choose_language_english(self):
        try:
            self.temp.chooseLanguage("EN")
        except ExceptionType:
            self.fail("MenuClass.chooseLanguage(\"EN\") didn't redirect to other function")
    def test_choose_language_polish(self):
        try:
            self.temp.chooseLanguage("PL")
        except ExceptionType:
            self.fail("MenuClass.chooseLanguage(\"PL\") didn't redirect to other function")


if __name__ == '__main__':
    unittest.main()
