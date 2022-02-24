# created by Ioannis STASINOPOULOS, 22.Feb.2022

#######################################################
# This package contains functions in order to
# convert roman numerals into arabic numbers.

# The coding principle rests on the following observation:

# The numerals for 4 (IV) and 9 (IX) are written using
# "subtractive notation",where the first symbol (I) is
# subtracted from the larger one (V, or X),
# thus avoiding the clumsier (IIII, and VIIII).
# Subtractive notation is also used for 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# These are the only subtractive forms in standard use.
#
# The working logic is:

# - call the principal function roman_to_arabic(roman_number)

# - call parser(roman_number) to iterate through possible subtractive forms
# and check their existence inside roman_number.
# If roman_number does not contain any subtractive form, it is evaluated the
# 'additive way'. E.g. 'XIII' using convert_non_subtr_num().
# If e.g. roman_number = 'MCMXVIII', parser() finds the subtractive form
# 'CM'. It splits roman_number in two parts: M + XVIII and 'retains' the value
# of 'CM' in 'retain' (= 900 in this case).
# The 1st ('clean') part, 'M', is evaluated using convert_non_subtr_num().
# The 2nd part, 'XVIII', is passed as the new value for roman_number
# and parser(roman_number) is called again. This allows to convert numerals
# containing several subtractive forms.
#######################################################

############################
# Create useful dictionaries
############################
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
subtractive_forms = {
    # It is important to list them in descending order, so that
    # they are found from left to right inside roman_number.
    "CM": 900,
    "CD": 400,
    "XC": 90,
    "XL": 40,
    "IX": 9,
    "IV": 4
}


def parser(roman_number):  # aux function
    for key in subtractive_forms:  # iterate through possible subtractive forms
        if roman_number.find(key) != -1:  # There IS a subtractive forms
            found_subtr_form = True
            retain = subtractive_forms[key]

            split = roman_number.find(key)  # position to split roman_number = position before subtractive form
            part1 = roman_number[:split]
            part2 = roman_number[split + 2:]
            # leave out the subtractive form,
            # because we already converted it in retain
            return [found_subtr_form, retain, part1, part2]

        else:
            continue


def convert_non_subtr_num(roman_number):  # aux function
    """
    Goes through roman_number and converts it in additive way.
    Returns arabic number.
    """
    arabic_number = 0
    for i in range(0, len(roman_number)):
        arabic_number = arabic_number + values[roman_number[i]]
    return arabic_number


def roman_to_arabic(roman_number):  # main function
    arabic_number = 0
    while roman_number != "":
        parse_result = parser(roman_number)

        if parse_result is None:
            converted_clean_string = convert_non_subtr_num(roman_number)
            arabic_number = arabic_number + converted_clean_string
            return arabic_number

        else:
            retain, clean_string, roman_number = parse_result[1], \
                                                 parse_result[2], \
                                                 parse_result[3]
            # roman_number is redefined as parse_result[3] = part2

            converted_clean_string = convert_non_subtr_num(clean_string)
            arabic_number = arabic_number + retain + converted_clean_string
        pass
    return arabic_number
