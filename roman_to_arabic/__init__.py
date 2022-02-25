# created by Ioannis STASINOPOULOS, 22.Feb.2022

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
    return None


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
            # roman_number is redefined as parse_result[3] = part2 ( see parser() ).

            converted_clean_string = convert_non_subtr_num(clean_string)
            arabic_number = arabic_number + retain + converted_clean_string
    return arabic_number
