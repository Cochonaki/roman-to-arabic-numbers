# Roman-to-arabic number converter
created by Ioannis STASINOPOULOS, 22.Feb.2022

Convert roman numerals into arabic numbers.

main.py contains 17 relevant tests for the code. 


The coding principle rests on the following observation:

The numerals for 4 (IV) and 9 (IX) are written using
"subtractive notation", where the first symbol (I) is
subtracted from the larger one (V, or X),
thus avoiding the clumsier (IIII, and VIIII).
Subtractive notation is also used for 40 (XL), 90 (XC), 400 (CD) and 900 (CM).

These are the only subtractive forms in standard use.
 
The working logic, implemented inside the 
```python
__init__.py
```
function of the roman_to_arabic package, is:

First call the principal function 
```python
roman_to_arabic(roman_number)
```

then call 
```python
parser(roman_number)
``` 
to iterate through possible subtractive forms
and check their existence inside roman_number.

If roman_number does not contain any subtractive form, it is evaluated the
'additive way', e.g. 'XIII' using the function
```python
convert_non_subtr_num()
```

E.g. for roman_number = 'MCMXVIII', parser() function finds the subtractive form
'CM'. It splits roman_number in two parts: 

M + XVIII 

and 'retains' the value
of 'CM' in 'retain' (= 900 in this case).

The 1st ('clean') part, 'M', is evaluated using convert_non_subtr_num().

The 2nd part, 'XVIII', is passed as the new value for roman_number
and parser(roman_number) is called again. 

This allows to convert numerals
containing several subtractive forms.

## Usage
Run the tests in your terminal, by executing
 
```python
pytest main.py
```
in your terminal.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

