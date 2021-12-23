import unittest
from assertpy import *
from discipleClass import DiscipleClass
class Assertpy_calculateMarkAverageFromDisciple_Test(unittest.TestCase):

    def setUp(self):
        self.temp = DiscipleClass

    def test_calculateMarkAverageFromSubject_is_float(self):
        assert_that(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks']))).is_equal_to(float)