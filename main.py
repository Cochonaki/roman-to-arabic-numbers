######################################################
# Run this test in the terminal, by executing
# 'pytest main.py'
######################################################

from roman_to_arabic import roman_to_arabic

def test_two():
    assert (roman_to_arabic('II') == 2)

def test_four():
    assert (roman_to_arabic('IV') == 4)

def test_nine():
    assert (roman_to_arabic('IX') == 9)

def test_thriteen():
    assert (roman_to_arabic('XIII') == 13)

def test_thritynine():
    assert (roman_to_arabic('XXXIX') == 39)

def test_246():
    assert (roman_to_arabic('CCXLVI') == 246)

def test_789():
    assert (roman_to_arabic('DCCLXXXIX') == 789)

def test_2421():
    assert (roman_to_arabic('MMCDXXI') == 2421)

def test_160():
    assert (roman_to_arabic('CLX') == 160)

def test_207():
    assert (roman_to_arabic('CCVII') == 207)

def test_1009():
    assert (roman_to_arabic('MIX') == 1009)

def test_1066():
    assert (roman_to_arabic('MLXVI') == 1066)

def test_1776():
    assert (roman_to_arabic('MDCCLXXVI') == 1776)

def test_1918():
    assert (roman_to_arabic('MCMXVIII') == 1918)

def test_1954():
    assert (roman_to_arabic('MCMLIV') == 1954)

def test_2014():
    assert (roman_to_arabic('MMXIV') == 2014)

# The largest number that can be represented in roman notation:
def test_3999():
    assert (roman_to_arabic('MMMCMXCIX') == 3999)
