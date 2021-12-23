import unittest
from parameterized import parameterized_class
from menuClass import MenuClass

@parameterized_class(('language', 'expected'), [
    ("EN","EN"),
    ("PL","EN"),
    ("SomethingThatWillCauseException",Exception("Wrong language inputed."))
])
class MenuClass_chooseLanguage_ClassLevel(unittest.TestCase):#Poziom klasy
    def setUp(self):
        self.tmp = MenuClass()

    def test_class_parameterized(self):
        self.assertEqual(self.tmp.chooseLanguage(self.language), self.expected)
