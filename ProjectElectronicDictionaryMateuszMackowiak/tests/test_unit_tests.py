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
    @patch('menuClass.MenuClass.menu')
    def test_menu_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN", 0)#i had to give in any choose so tests go on
        self.assertTrue(mock_function.called)
    #0
    @patch('discipleClass.DiscipleClass.chooseAndDisplayDisciple')
    def test_menu_chooseAndDisplayDisciple_worked(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.chooseAndDisplayDisciple("EN")
        self.assertTrue(mock_function.called)

    @patch('menuClass.MenuClass.menu')
    def test_menu_chooseAndDisplayDisciple_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN", 0)
        self.assertTrue(mock_function.called)
    #1
    @patch('discipleClass.DiscipleClass.addDisciple')
    def test_menu_addDisciple_worked(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.addDisciple("EN")
        self.assertTrue(mock_function.called)

    @patch('menuClass.MenuClass.menu')
    def test_menu_addDisciple_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN", 1)
        self.assertTrue(mock_function.called)
    #2
    @patch('discipleClass.DiscipleClass.editDisciple')
    def test_menu_editDisciple_worked(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.editDisciple("EN")
        self.assertTrue(mock_function.called)

    @patch('menuClass.MenuClass.menu')
    def test_menu_editDisciple_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN", 2)
        self.assertTrue(mock_function.called)
    #3
    @patch('discipleClass.DiscipleClass.removeDisciple')
    def test_menu_removeDisciple_worked(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.removeDisciple("EN")
        self.assertTrue(mock_function.called)

    @patch('menuClass.MenuClass.menu')
    def test_menu_removeDisciple_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN", 3)
        self.assertTrue(mock_function.called)
    #4
    @patch('menuClass.MenuClass.importDatabaseFromCSV')
    def test_menu_importDatabaseFromCSV_worked(self, mock_function):
        mockClass = MenuClass()
        mockClass.importDatabaseFromCSV("EN")
        self.assertTrue(mock_function.called)

    @patch('menuClass.MenuClass.menu')
    def test_menu_importDatabaseFromCSV_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN", 4)
        self.assertTrue(mock_function.called)
    #5
    @patch('menuClass.MenuClass.exportDatabaseToCSV')
    def test_menu_exportDatabaseToCSV_worked(self, mock_function):
        mockClass = MenuClass()
        mockClass.exportDatabaseToCSV("EN")
        self.assertTrue(mock_function.called)

    @patch('menuClass.MenuClass.menu')
    def test_menu_exportDatabaseToCSV_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN",5)
        self.assertTrue(mock_function.called)
    #6
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
    def test_choose_language_is_str(self):
        self.assertEqual(type(self.temp.chooseLanguage("EN")),str)
    def test_choose_language_is_not_int(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),int)
    def test_choose_language_is_not_float(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),float)
    def test_choose_language_is_not_complex(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),complex)
    def test_choose_language_is_not_list(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),list)
    def test_choose_language_is_not_tuple(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),tuple)
    def test_choose_language_is_not_range(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),range)
    def test_choose_language_is_not_dict(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),dict)
    def exception_choose_language_other(self):
        self.assertRaises(Exception("Wrong language inputed."),self.temp.chooseLanguage("Uga Booga"))
class DiscipleClassTest(unittest.TestCase):
    def setUp(self):
        self.temp = DiscipleClass
# mark average from disciple=============================================================================================
    def test_calculateMarkAverageFromDisciple_is_result_float(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertTrue(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==float)
    def test_calculateMarkAverageFromDisciple_result_is_not_string(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==str)
    def test_calculateMarkAverageFromDisciple_result_is_not_int(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==int)
    def test_calculateMarkAverageFromDisciple_result_is_not_list(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==list)
    def test_calculateMarkAverageFromDisciple_result_is_not_dict(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==dict)
    def test_calculateMarkAverageFromDisciple_result_is_not_tuple(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==tuple)
    def test_calculateMarkAverageFromDisciple_result_is_not_range(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==range)
    def test_calculateMarkAverageFromDisciple_result_is_not_complex(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==complex)
    def test_calculateMarkAverageFromDisciple_result_is_not_set(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==set)
    def test_calculateMarkAverageFromDisciple_result_is_not_frozenset(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==frozenset)
    def test_calculateMarkAverageFromDisciple_result_is_not_bool(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==bool)
    def test_calculateMarkAverageFromDisciple_result_is_not_bytes(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==bytes)
    def test_calculateMarkAverageFromDisciple_result_is_not_bytearray(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==bytearray)
    def test_calculateMarkAverageFromDisciple_result_is_not_memoryview(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==memoryview)
    def test_calculateMarkAverageFromDisciple_result_is_not_none(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNotNone(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])))
    def test_calculateMarkAverageFromDisciple_result_is_not_empty_string(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),'')
    def test_calculateMarkAverageFromDisciple_result_is_not_equal(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),'')
    def test_calculateMarkAverageFromDisciple_result_is_correct(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertEqual(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]),2.625)

# mark average from disciple=============================================================================================
# mark average from subject=============================================================================================
    def test_calculateMarkAverageFromSubject_is_result_float(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertTrue(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==float)
    def test_calculateMarkAverageFromSubject_result_is_not_string(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),str)
    def test_calculateMarkAverageFromSubject_result_is_not_int(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),int)
    def test_calculateMarkAverageFromSubject_result_is_not_complex(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),complex)
    def test_calculateMarkAverageFromSubject_result_is_not_list(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),list)
    def test_calculateMarkAverageFromSubject_result_is_not_tuple(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),tuple)
    def test_calculateMarkAverageFromSubject_result_is_not_range(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),range)
    def test_calculateMarkAverageFromSubject_result_is_not_dict(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),dict)
    def test_calculateMarkAverageFromSubject_result_is_not_set(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),set)
    def test_calculateMarkAverageFromSubject_result_is_not_frozenset(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),frozenset)
    def test_calculateMarkAverageFromSubject_result_is_not_bool(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),bool)
    def test_calculateMarkAverageFromSubject_result_is_not_bytes(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),bytes)
    def test_calculateMarkAverageFromSubject_result_is_not_bytearray(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),bytearray)
    def test_calculateMarkAverageFromSubject_result_is_not_memoryview(self):
        import json
        with open('../data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),memoryview)

    # mark average from subject=============================================================================================
    @patch('discipleClass.DiscipleClass.displayAllDisciples')
    def test_displayAllDisciples_called(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.displayAllDisciples("EN")
        self.assertTrue(mock_function.called)

    @patch('discipleClass.DiscipleClass.chooseAndDisplayDisciple')
    def test_chooseAndDisplayDisciple_called(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.chooseAndDisplayDisciple("EN")
        self.assertTrue(mock_function.called)


    @patch('discipleClass.DiscipleClass.addDisciple')
    def test_addDisciple_called(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.addDisciple("EN")
        self.assertTrue(mock_function.called)

    @patch('discipleClass.DiscipleClass.editDisciple')
    def test_editDisciple_called(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.editDisciple("EN")
        self.assertTrue(mock_function.called)

    @patch('discipleClass.DiscipleClass.removeDisciple')
    def test_removeDisciple_called(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.removeDisciple("EN")
        self.assertTrue(mock_function.called)

class SubjectClassTest(unittest.TestCase):
    def setUp(self):
        self.temp = SubjectClass

    @patch('subjectClass.SubjectClass.addSubject')
    def test_addSubject_called(self, mock_function):
        mockClass = SubjectClass()
        mockClass.addSubject("EN")
        self.assertTrue(mock_function.called)

    @patch('subjectClass.SubjectClass.editSubject')
    def test_editSubject_called(self, mock_function):
        mockClass = SubjectClass()
        mockClass.editSubject("EN")
        self.assertTrue(mock_function.called)

    @patch('subjectClass.SubjectClass.removeSubject')
    def test_removeSubject_called(self, mock_function):
        mockClass = SubjectClass()
        mockClass.removeSubject("EN")
        self.assertTrue(mock_function.called)
class MarkClassTest(unittest.TestCase):
    def setUp(self):
        self.temp = MarkClass

    @patch('markClass.MarkClass.addMark')
    def test_addMark_called(self, mock_function):
        mockClass = MarkClass()
        mockClass.addMark("EN")
        self.assertTrue(mock_function.called)

    @patch('markClass.MarkClass.editMark')
    def test_editMark_called(self, mock_function):
        mockClass = MarkClass()
        mockClass.editMark("EN")
        self.assertTrue(mock_function.called)

    @patch('markClass.MarkClass.removeMark')
    def test_removeMark_called(self, mock_function):
        mockClass = MarkClass()
        mockClass.removeMark("EN")
        self.assertTrue(mock_function.called)






if __name__ == '__main__':
    unittest.main()
    #nosetests

#to check with ctrl + f
#used assert types: 1. assertTrue, 2. assertFalse, 3. assertIsNot, 4. assertIsNotNone, 5. assertIs, 6. assertNotEqual, 7. assertEqual
