import unittest
from assertpy import *
from src.discipleClass import DiscipleClass
class Assertpy_calculateMarkAverageFromDisciple_Test(unittest.TestCase):

    def setUp(self):
        self.temp = DiscipleClass()

    def test_calculateMarkAverageFromSubject_is_float(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks']))).is_equal_to(float)