# Problem Link: https://leetcode.com/problems/isomorphic-strings/
# Author: Dyanara Dela Rosa
# Date: April 15, 2025


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_mappings = {}
        for schar, tchar in zip(s, t):
            if schar in char_mappings:
                if tchar != char_mappings[schar]:
                    return False
            else:
                if tchar in char_mappings.values():
                    return False
                char_mappings[schar] = tchar
        return True

