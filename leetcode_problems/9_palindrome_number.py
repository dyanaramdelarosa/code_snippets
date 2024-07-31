# Problem Link: https://leetcode.com/problems/palindrome-number/
# Author: Dyanara Dela Rosa
# Date: June 14, 2024

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        mid = len(x) // 2
        if len(x)%2:
            return x[:mid] == x[:mid:-1]
        return x[:mid] == x[:mid-1:-1]