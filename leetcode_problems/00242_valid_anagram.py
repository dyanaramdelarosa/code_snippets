# Problem Link: https://leetcode.com/problems/missing-number/
# Author: Dyanara Dela Rosa
# Date: Mar 24, 2025


from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return Counter(s) == Counter(t)