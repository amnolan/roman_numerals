# put problem statement below the solution

class RomanNumerals:
    def romanToInt(self, input_str: str) -> int:
        # create a dictionary to look up the chars from
        roman_to_integer = dict()
        roman_to_integer['I'] = 1
        roman_to_integer['V'] = 5
        roman_to_integer['X'] = 10
        roman_to_integer['L'] = 50
        roman_to_integer['C'] = 100
        roman_to_integer['D'] = 500
        roman_to_integer['M'] = 1000
        # because roman numerals are a stupid numbering system
        # treat the numbers as childishly simple numbers
        # so we are literally counting char by char instead of trying
        # to do some fancy look ahead list processing
        #
        # replace IV with IIII (4)
        # replace IX with VIIII (9)
        # replace XL with XXXX (40)
        # replace XC with LXXXX (90)
        # replace CD with CCCC (400)
        # replace CM with DCCCC (900)
        input_str = input_str.replace('IV',"IIII").replace("IX","VIIII").replace("XL","XXXX").replace("XC","LXXXX").replace("CD","CCCC").replace("CM","DCCCC")

        # after replacement the inner function map() will
        # loop over the lambda i is the current dictionary key
        # it will look up the corresponding numerical value with the
        # current char, fed in from the string replaced "input_str"
        # once the lamda has been ran on all items in the string
        # the resulting map will be a map of ints
        # you simply run the sum() function on the result and the
        # roman numerals will be correctly calculated
        return sum(
            map(
                lambda i: roman_to_integer[i], input_str
            )
        )

# problem statement
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
