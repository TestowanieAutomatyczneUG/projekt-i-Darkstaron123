import unittest
from parameterized import parameterized
from menuClass import MenuClass

class MenuClass_chooseLanguage_MethodLevel(unittest.TestCase):# Poziom Method
    def setUp(self):
        self.tmp = MenuClass()

    @parameterized.expand([
        ("EN", "EN"),
        ("EN", "EN"),
        ("SomethingThatWillCauseException", Exception("Wrong language inputed.")),
    ])
    def test_chooseLanguage_parameterized(self,choose, expected):
        self.assertEqual(self.tmp.chooseLanguage(choose), expected)