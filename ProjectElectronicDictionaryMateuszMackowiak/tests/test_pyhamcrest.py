import unittest
from hamcrest import *
import unittest
from unittest.mock import patch

from menuClass import MenuClass
from discipleClass import DiscipleClass
from subjectClass import SubjectClass
from markClass import MarkClass
class PyHamcrestAverageCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.temp = DiscipleClass

    def test_calculateMarkAverageFromDisciple_is_float(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),equal_to(float))
    def test_calculateMarkAverageFromDisciple_is_correct(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]),equal_to(2.625))
    def test_calculateMarkAverageFromDisciple_is_not_string(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(str))
    def test_calculateMarkAverageFromDisciple_is_not_int(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(str))