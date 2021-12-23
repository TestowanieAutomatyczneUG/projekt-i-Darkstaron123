import unittest
from parameterized import parameterized
from sample.pangram import *

class PangramParameterizedPackage_MethodLevel(unittest.TestCase):# Poziom Method
    def setUp(self):
        self.tmp = PangramClass()

    @parameterized.expand([
        ("abcdefghijklmnopqrstuvwxyz", True),
        (1, False),
        ("abcdefghijklmnopqrs", False),
        ("dmnopefghijklstuvwxyzabqrc", True),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),
        ("AbCDEFGHIJKLMNOpqRSTUVWXYZ", True),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZqrsA12512BCdefrgw", True),
    ])
    def test_one_parameterized(self,word, expected):
        self.assertEqual(self.tmp.is_pangram(word), expected)