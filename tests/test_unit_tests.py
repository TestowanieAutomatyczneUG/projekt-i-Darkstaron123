# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
from unittest.mock import patch

from src.menuClass import MenuClass
from src.discipleClass import DiscipleClass
from src.subjectClass import SubjectClass
from src.markClass import MarkClass


class MenuClassTest(unittest.TestCase):
    def setUp(self):
        self.temp = MenuClass()
    #testing menu() function
    @patch('src.menuClass.MenuClass.menu')
    def test_menu_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN", 0)#i had to give in any choose so tests go on
        self.assertTrue(mock_function.called)
    #0
    @patch('src.discipleClass.DiscipleClass.chooseAndDisplayDisciple')
    def test_menu_chooseAndDisplayDisciple_worked(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.chooseAndDisplayDisciple("EN")
        self.assertTrue(mock_function.called)

    @patch('src.menuClass.MenuClass.menu')
    def test_menu_chooseAndDisplayDisciple_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN", 0)
        self.assertTrue(mock_function.called)
    #1
    @patch('src.discipleClass.DiscipleClass.addDisciple')
    def test_menu_addDisciple_worked(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.addDisciple("EN")
        self.assertTrue(mock_function.called)

    @patch('src.menuClass.MenuClass.menu')
    def test_menu_addDisciple_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN", 1)
        self.assertTrue(mock_function.called)
    #2
    @patch('src.discipleClass.DiscipleClass.editDisciple')
    def test_menu_editDisciple_worked(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.editDisciple("EN")
        self.assertTrue(mock_function.called)

    @patch('src.menuClass.MenuClass.menu')
    def test_menu_editDisciple_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN", 2)
        self.assertTrue(mock_function.called)
    #3
    @patch('src.discipleClass.DiscipleClass.removeDisciple')
    def test_menu_removeDisciple_worked(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.removeDisciple("EN")
        self.assertTrue(mock_function.called)

    @patch('src.menuClass.MenuClass.menu')
    def test_menu_removeDisciple_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN", 3)
        self.assertTrue(mock_function.called)
    #4
    @patch('src.menuClass.MenuClass.importDatabaseFromCSV')
    def test_menu_importDatabaseFromCSV_worked(self, mock_function):
        mockClass = MenuClass()
        mockClass.importDatabaseFromCSV("EN")
        self.assertTrue(mock_function.called)

    @patch('src.menuClass.MenuClass.menu')
    def test_menu_importDatabaseFromCSV_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN", 4)
        self.assertTrue(mock_function.called)
    #5
    @patch('src.menuClass.MenuClass.exportDatabaseToCSV')
    def test_menu_exportDatabaseToCSV_worked(self, mock_function):
        mockClass = MenuClass()
        mockClass.exportDatabaseToCSV("EN")
        self.assertTrue(mock_function.called)

    @patch('src.menuClass.MenuClass.menu')
    def test_menu_exportDatabaseToCSV_called(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN",5)
        self.assertTrue(mock_function.called)
    #6
    @patch('src.menuClass.MenuClass.menu')
    def test_menu_log_out(self, mock_function):
        mockClass = MenuClass()
        mockClass.menu("EN","6")
        self.assertTrue(mock_function.called)
    #testing choose_language() function
    #choose language=============================================================================================
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
    def test_choose_language_is_not_set(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),set)
    def test_choose_language_is_not_frozenset(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),frozenset)
    def test_choose_language_is_not_bool(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),bool)
    def test_choose_language_is_not_bytes(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),bytes)
    def test_choose_language_is_not_bytesarray(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),bytearray)
    def test_choose_language_is_not_memoryview(self):
        self.assertNotEqual(type(self.temp.chooseLanguage("EN")),memoryview)
    def exception_choose_language_other(self):
        self.assertRaises(Exception("Wrong language inputed."),self.temp.chooseLanguage("Uga Booga"))
# choose language=======================================================================================================
# log out===============================================================================================================
    def test_log_out_return_zero(self):
        self.assertEqual(self.temp.logOut("FR"),0)
    def test_log_out_is_int(self):
        self.assertEqual(type(self.temp.logOut("FR")),int)
    def test_log_out_is_not_float(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),float)
    def test_log_out_is_not_complex(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),complex)
    def test_log_out_is_not_list(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),list)
    def test_log_out_is_not_string(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),str)
    def test_log_out_is_not_tuple(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),tuple)
    def test_log_out_is_not_range(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),range)
    def test_log_out_is_not_dict(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),dict)
    def test_log_out_is_not_set(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),set)
    def test_log_out_is_not_frozenset(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),frozenset)
    def test_log_out_is_not_bool(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),bool)
    def test_log_out_is_not_bytes(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),bytes)
    def test_log_out_is_not_bytearray(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),bytearray)
    def test_log_out_is_not_memoryview(self):
        self.assertNotEqual(type(self.temp.logOut("FR")),memoryview)

# log out===============================================================================================================
class DiscipleClassTest(unittest.TestCase):
    def setUp(self):
        self.temp = DiscipleClass()

# notices quantity from disciple========================================================================================
    def test_countNumberOfNotices_is_int(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertTrue(type(self.temp.countNumberOfNotices(data['disciples'][0])) == int)
    def test_countNumberOfNotices_is_not_string(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),str)
    def test_countNumberOfNotices_is_not_float(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),float)
    def test_countNumberOfNotices_is_not_complex(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),complex)
    def test_countNumberOfNotices_is_not_list(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),list)
    def test_countNumberOfNotices_is_not_tuple(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),tuple)
    def test_countNumberOfNotices_is_not_range(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),range)
    def test_countNumberOfNotices_is_not_dict(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),dict)
    def test_countNumberOfNotices_is_not_set(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),set)
    def test_countNumberOfNotices_is_not_frozenset(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),frozenset)
    def test_countNumberOfNotices_is_not_bool(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),bool)
    def test_countNumberOfNotices_is_not_bytes(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),bytes)
    def test_countNumberOfNotices_is_not_bytearray(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),bytearray)
    def test_countNumberOfNotices_is_not_memoryview(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.countNumberOfNotices(data['disciples'][0])),memoryview)
# notices quantity from disciple========================================================================================
# mark average from disciple============================================================================================
    def test_calculateMarkAverageFromDisciple_is_result_float(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertTrue(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==float)
    def test_calculateMarkAverageFromDisciple_result_is_not_string(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==str)
    def test_calculateMarkAverageFromDisciple_result_is_not_int(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==int)
    def test_calculateMarkAverageFromDisciple_result_is_not_list(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==list)
    def test_calculateMarkAverageFromDisciple_result_is_not_dict(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==dict)
    def test_calculateMarkAverageFromDisciple_result_is_not_tuple(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==tuple)
    def test_calculateMarkAverageFromDisciple_result_is_not_range(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==range)
    def test_calculateMarkAverageFromDisciple_result_is_not_complex(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==complex)
    def test_calculateMarkAverageFromDisciple_result_is_not_set(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==set)
    def test_calculateMarkAverageFromDisciple_result_is_not_frozenset(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==frozenset)
    def test_calculateMarkAverageFromDisciple_result_is_not_bool(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==bool)
    def test_calculateMarkAverageFromDisciple_result_is_not_bytes(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==bytes)
    def test_calculateMarkAverageFromDisciple_result_is_not_bytearray(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==bytearray)
    def test_calculateMarkAverageFromDisciple_result_is_not_memoryview(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertFalse(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]))==memoryview)
    def test_calculateMarkAverageFromDisciple_result_is_not_none(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNotNone(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])))
    def test_calculateMarkAverageFromDisciple_result_is_not_empty_string(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),'')
    def test_calculateMarkAverageFromDisciple_result_is_not_equal(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertNotEqual(type(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0])),'')
    def test_calculateMarkAverageFromDisciple_result_is_correct(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertEqual(self.temp.calculateMarkAverageFromDisciple(data['disciples'][0]),2.625)

# mark average from disciple============================================================================================
# mark average from subject=============================================================================================
    def test_calculateMarkAverageFromSubject_is_result_float(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertTrue(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks']))==float)
    def test_calculateMarkAverageFromSubject_result_is_not_string(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),str)
    def test_calculateMarkAverageFromSubject_result_is_not_int(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),int)
    def test_calculateMarkAverageFromSubject_result_is_not_complex(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),complex)
    def test_calculateMarkAverageFromSubject_result_is_not_list(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),list)
    def test_calculateMarkAverageFromSubject_result_is_not_tuple(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),tuple)
    def test_calculateMarkAverageFromSubject_result_is_not_range(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),range)
    def test_calculateMarkAverageFromSubject_result_is_not_dict(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),dict)
    def test_calculateMarkAverageFromSubject_result_is_not_set(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),set)
    def test_calculateMarkAverageFromSubject_result_is_not_frozenset(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),frozenset)
    def test_calculateMarkAverageFromSubject_result_is_not_bool(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),bool)
    def test_calculateMarkAverageFromSubject_result_is_not_bytes(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),bytes)
    def test_calculateMarkAverageFromSubject_result_is_not_bytearray(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),bytearray)
    def test_calculateMarkAverageFromSubject_result_is_not_memoryview(self):
        import json
        with open('data/test_data.txt') as json_file:
            data = json.load(json_file)
            self.assertIsNot(type(self.temp.calculateMarkAverageFromSubject(data['disciples'][0]['subjects'][0]['marks'])),memoryview)

    # mark average from subject=========================================================================================
    @patch('src.discipleClass.DiscipleClass.displayAllDisciples')
    def test_displayAllDisciples_called(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.displayAllDisciples("EN")
        self.assertTrue(mock_function.called)

    @patch('src.discipleClass.DiscipleClass.chooseAndDisplayDisciple')
    def test_chooseAndDisplayDisciple_called(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.chooseAndDisplayDisciple("EN")
        self.assertTrue(mock_function.called)


    @patch('src.discipleClass.DiscipleClass.addDisciple')
    def test_addDisciple_called(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.addDisciple("EN")
        self.assertTrue(mock_function.called)

    @patch('src.discipleClass.DiscipleClass.editDisciple')
    def test_editDisciple_called(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.editDisciple("EN")
        self.assertTrue(mock_function.called)

    @patch('src.discipleClass.DiscipleClass.removeDisciple')
    def test_removeDisciple_called(self, mock_function):
        mockClass = DiscipleClass()
        mockClass.removeDisciple("EN")
        self.assertTrue(mock_function.called)

class SubjectClassTest(unittest.TestCase):
    def setUp(self):
        self.temp = SubjectClass()

    @patch('src.subjectClass.SubjectClass.addSubject')
    def test_addSubject_called(self, mock_function):
        mockClass = SubjectClass()
        mockClass.addSubject("EN")
        self.assertTrue(mock_function.called)

    @patch('src.subjectClass.SubjectClass.editSubject')
    def test_editSubject_called(self, mock_function):
        mockClass = SubjectClass()
        mockClass.editSubject("EN")
        self.assertTrue(mock_function.called)

    @patch('src.subjectClass.SubjectClass.removeSubject')
    def test_removeSubject_called(self, mock_function):
        mockClass = SubjectClass()
        mockClass.removeSubject("EN")
        self.assertTrue(mock_function.called)
class MarkClassTest(unittest.TestCase):
    def setUp(self):
        self.temp = MarkClass()

    @patch('src.markClass.MarkClass.addMark')
    def test_addMark_called(self, mock_function):
        mockClass = MarkClass()
        mockClass.addMark("EN")
        self.assertTrue(mock_function.called)

    @patch('src.markClass.MarkClass.editMark')
    def test_editMark_called(self, mock_function):
        mockClass = MarkClass()
        mockClass.editMark("EN")
        self.assertTrue(mock_function.called)

    @patch('src.markClass.MarkClass.removeMark')
    def test_removeMark_called(self, mock_function):
        mockClass = MarkClass()
        mockClass.removeMark("EN")
        self.assertTrue(mock_function.called)






if __name__ == '__main__':
    unittest.main()
    #nosetests

#to check with ctrl + f
#used assert types from unittest: 1. assertTrue, 2. assertFalse, 3. assertIsNot, 4. assertIsNotNone, 5. assertIs,
# 6. assertNotEqual, 7. assertEqual
#used assert types from pyhamcrest: 8. assert_that(...,equal_to) 9. assert_that(...,is_not)

