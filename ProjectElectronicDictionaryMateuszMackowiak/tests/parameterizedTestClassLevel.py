import unittest
from parameterized import parameterized_class
from menuClass import MenuClass

@parameterized_class(('choose', 'expected'), [
    ("EN","EN"),
    ("PL","EN"),
    ("SomethingThatWillCauseException",Exception("Wrong language inputed."))
])
class MenuClass_chooseLanguage_ClassLevel(unittest.TestCase):#Poziom klasy
    def setUp(self):
        self.tmp = MenuClass()

    def test_chooseLanguage_parameterized(self):
        self.assertEqual(self.tmp.chooseLanguage(self.choose), self.expected)
