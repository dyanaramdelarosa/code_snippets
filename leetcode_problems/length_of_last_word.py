# Problem Link: https://leetcode.com/problems/length-of-last-word/
# Author: Dyanara Dela Rosa
# Date: June 23, 2024

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_tokens = s.split()
        return len(s_tokens[-1])