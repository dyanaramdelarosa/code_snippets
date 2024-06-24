# Problem Link: https://leetcode.com/problems/climbing-stairs/
# Author: Dyanara Dela Rosa
# Date: June 16, 2024

class Solution:
    def climbStairs(self, n: int) -> int:
        stairs_memoize = [1, 2]

        if n < len(stairs_memoize):
            return stairs_memoize[n-1]

        for i in range(len(stairs_memoize), n):
            stairs_memoize.append(stairs_memoize[i-1] + stairs_memoize[i-2])

        return stairs_memoize[n-1]
