import pytest
from string_utils import StringUtils

stringutils = StringUtils()


@pytest.mark.parametrize("string, result", [
    ("skypro", "Skypro"),
    ("online", "Online"),
    ("123", "123"),
    ("a few words in a sentence", "A few words in a sentence"),
    ("несколько слов в предложении", "Несколько слов в предложении"),
    ("", ""),
    (" ", " "),
    (None, None)
])
def test_capitalize(string, result):
    res = stringutils.capitilize(string)
    assert res == result


@pytest.mark.parametrize("string, result", [
    (" skypro", "skypro"),
    ("  skypro", "skypro"),
    ("   skypro", "skypro"),
    ("", ""),
    (" ", ""),
    (None, None)
])
def test_trim(string, result):
    res = stringutils.trim(string)
    assert res == result


@pytest.mark.parametrize("string, delimeter, result", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ":", []),
    (" ", ":", []),
    (None, ":", None)
])
def test_to_list(string, delimeter, result):
    assert stringutils.to_list(string, delimeter) == result


@pytest.mark.parametrize("string, symbol, result", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "A", False),
    ("  ", "A", False),
    (None, None, False)
])
def test_contains(string, symbol, result):
    res = stringutils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("", "A", ""),
    ("  ", "  ", ""),
    (None, "A", None)
])
def test_delete_symbol(string, symbol, result):
    res = stringutils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [
    ("SkyPro", "S", True),
    ("SkyPro", "p", False),
    ("", "a", False),
    ("  ", "a", False),
    (None, None, False)
])
def test_starts_with(string, symbol, result):
    res = stringutils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),
    ("", "a", False),
    ("  ", "a", False),
    (None, None, False)
])
def test_end_with(string, symbol, result):
    res = stringutils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, result", [
    ("", True),
    (" ", True),
    ("Skypro", False),
    ("a", False),
    ("123", False),
    (None, True)
])
def test_is_empty(string, result):
    res = stringutils.is_empty(string)
    assert res == result


@pytest.mark.parametrize("lst, joiner, expected", [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    ([], "- ", "" ),
    (None, "- ", "")
])
def test_list_to_string(lst, joiner, expected):
    res = stringutils.list_to_string(lst, joiner)
    assert res == expected

