# Problem Link: https://leetcode.com/problems/rising-temperature/
# Author: Dyanara Dela Rosa
# Date: May 27, 2025

class Solution:
    def isHappy(self, n: int) -> bool:
        squares = {0:0, 1:1, 2:4, 3:9, 4:16, 5:25,
            6:36, 7:49, 8:64, 9:81
        }
        # squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

        prev_ans = set()
        while True:
            ans = 0
            for i in str(n):
                ans += squares[int(i)]
            if ans == 1:
                return True
            if ans in prev_ans:
                return False
            prev_ans.add(ans)
            n = ans
