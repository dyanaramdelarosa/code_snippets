# Problem Link: https://leetcode.com/problems/valid-palindrome/
# Author: Dyanara Dela Rosa
# Date: August 14, 2024

import re
class Solution:
    def cleanInput(self, s: str) -> str:
        pattern = re.compile('[\W_]+', re.UNICODE)
        return pattern.sub('', s)

    def isPalindrome(self, s: str) -> bool:
        s = self.cleanInput(s).lower()
        return s == s[::-1]
        
