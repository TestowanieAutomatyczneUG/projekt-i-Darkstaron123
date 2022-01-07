

from src.menuClass import MenuClass


def test_choose_language_is_str():
    assert type(MenuClass().chooseLanguage("EN"))==str
def test_choose_language_is_not_int():
    assert type(MenuClass().chooseLanguage("EN"))!=int
def test_choose_language_is_not_float():
    assert type(MenuClass().chooseLanguage("EN"))!=float
def test_choose_language_is_not_complex():
    assert type(MenuClass().chooseLanguage("EN"))!=complex
def test_choose_language_is_not_list():
    assert type(MenuClass().chooseLanguage("EN"))!=list
def test_choose_language_is_not_tuple():
    assert type(MenuClass().chooseLanguage("EN"))!=tuple
def test_choose_language_is_not_range():
    assert type(MenuClass().chooseLanguage("EN"))!=range
def test_choose_language_is_not_dict():
    assert type(MenuClass().chooseLanguage("EN"))!=dict
def test_choose_language_is_not_set():
    assert type(MenuClass().chooseLanguage("EN"))!=set
def test_choose_language_is_not_frozenset():
    assert type(MenuClass().chooseLanguage("EN"))!=frozenset
def test_choose_language_is_not_bool():
    assert type(MenuClass().chooseLanguage("EN"))!=bool
def test_choose_language_is_not_bytearray():
    assert type(MenuClass().chooseLanguage("EN"))!=bytearray
def test_choose_language_is_not_memoryview():
    assert type(MenuClass().chooseLanguage("EN"))!=memoryview
def test_log_out_is_not_str():
    assert type(MenuClass().logOut("EN"))!=str
def test_log_out_is_int():
    assert type(MenuClass().logOut("EN"))==int
def test_log_out_is_not_float():
    assert type(MenuClass().logOut("EN"))!=float
def test_log_out_is_not_complex():
    assert type(MenuClass().logOut("EN"))!=complex
def test_log_out_is_not_list():
    assert type(MenuClass().logOut("EN"))!=list
def test_log_out_is_not_tuple():
    assert type(MenuClass().logOut("EN"))!=tuple
def test_log_out_is_not_range():
    assert type(MenuClass().logOut("EN"))!=range
def test_log_out_is_not_dict():
    assert type(MenuClass().logOut("EN"))!=dict
def test_log_out_is_not_set():
    assert type(MenuClass().logOut("EN"))!=set
def test_log_out_is_not_frozenset():
    assert type(MenuClass().logOut("EN"))!=frozenset
def test_log_out_is_not_bool():
    assert type(MenuClass().logOut("EN"))!=bool
def test_log_out_is_not_bytearray():
    assert type(MenuClass().logOut("EN"))!=bytearray
def test_log_out_is_not_memoryview():
    assert type(MenuClass().logOut("EN"))!=memoryview


