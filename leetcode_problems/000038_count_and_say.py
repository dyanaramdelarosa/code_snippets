# Problem Link: https://leetcode.com/problems/count-and-say/
# Author: Dyanara Dela Rosa
# Date: Oct 14, 2026

class Solution:
    def get_rle(self, s: str) -> str:
        current_char = ""
        current_count = 0
        new_s = ""
        for i in s:
            if i == current_char:
                current_count += 1
            else:
                if current_char:
                    new_s = f"{new_s}{current_count}{current_char}"
                current_char = i
                current_count = 1
        new_s = f"{new_s}{current_count}{current_char}"
        return new_s

    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(2, n+1):
            s = self.get_rle(s)
        return s
