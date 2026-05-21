# Problem Link: https://leetcode.com/problems/excel-sheet-column-title/
# Author: Dyanara Dela Rosa
# Date: April 8, 2025


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            columnNumber -= 1
            title += chr((columnNumber%26)+65)
            columnNumber //= 26
        return title[::-1]