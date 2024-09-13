# Problem Link: https://leetcode.com/problems/string-to-integer-atoi/
# Author: Dyanara Dela Rosa
# Date: September 13, 2024

class Solution:
    def remove_leading_whitespace(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] != " ":
                return s[i:]
        return ""


    def extract_sign(self, s: str) -> (int, str):
        if s[0] == '-': return -1, s[1:]
        if s[0] == '+': return 1, s[1:]
        return 0, s


    def get_number(self, s: str) -> int:
        num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                if num == 0:
                    num = int(s[i])
                else:
                    num = num * 10 + int(s[i])
            else:
                break
        return num
    
    
    def round(self, num: int) -> int:
        lowest = -2**31
        highest = 2**31 - 1
        if num < lowest: return lowest
        if num > highest: return highest
        return num
            
    def myAtoi(self, s: str) -> int:
        s = self.remove_leading_whitespace(s)
        if s:
            sign, s = self.extract_sign(s)
        if s:
            num = self.get_number(s)
            if sign:
                num = sign * self.get_number(s)
            return self.round(num)
        return 0


        
