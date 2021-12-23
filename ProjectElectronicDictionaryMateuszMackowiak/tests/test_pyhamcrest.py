from hamcrest import *
import unittest
from hamcrest.core.base_matcher import BaseMatcher

class IsEnglishLanguageMatcher(BaseMatcher):# custom matcher

    def __init__(self, word):
        self.word = word

    def _matches(self, item):
        return "EN" == self.word

from discipleClass import DiscipleClass
from menuClass import MenuClass
class PyHamcrest_calculateMarkAverageFromDisciple_Test(unittest.TestCase):

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
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(int))
    def test_calculateMarkAverageFromDisciple_is_not_complex(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(complex))
    def test_calculateMarkAverageFromDisciple_is_not_list(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(list))
    def test_calculateMarkAverageFromDisciple_is_not_tuple(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(tuple))
    def test_calculateMarkAverageFromDisciple_is_not_range(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(range))
    def test_calculateMarkAverageFromDisciple_is_not_dict(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(dict))
    def test_calculateMarkAverageFromDisciple_is_not_set(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(set))
    def test_calculateMarkAverageFromDisciple_is_not_frozenset(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(frozenset))
    def test_calculateMarkAverageFromDisciple_is_not_bool(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(bool))
    def test_calculateMarkAverageFromDisciple_is_not_bytes(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(bytes))
    def test_calculateMarkAverageFromDisciple_is_not_bytearray(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(bytearray))
    def test_calculateMarkAverageFromDisciple_is_not_memoryview(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            assert_that(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),is_not(memoryview))
    def test_choose_language(self):
        assert_that(MenuClass.chooseLanguage("EN"),IsEnglishLanguageMatcher("EN"))#usage of custom matcher