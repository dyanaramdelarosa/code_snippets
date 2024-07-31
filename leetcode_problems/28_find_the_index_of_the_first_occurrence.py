# Problem Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Author: Dyanara Dela Rosa
# Date: June 21, 2024

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # needle_len = len(needle)
        # for i in range(len(haystack)-needle_len+1):
        #     if haystack[i: i+needle_len] == needle:
        #         return i
        # return -1

        if needle in haystack:
            return haystack.find(needle)
        return -1
