# Problem link: https://leetcode.com/problems/roman-to-integer/
# Author: Dyanara Dela Rosa
# Date: June 15, 2024

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_mapping: dict[str, int] = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        s = s.replace("IV", "IIII")
        s = s.replace("IX", "IIIIV")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "XXXXL")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "CCCCD")

        total = 0
        for i in s:
            total += roman_to_int_mapping[i]
        return total
