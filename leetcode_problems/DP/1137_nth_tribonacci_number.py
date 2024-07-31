# Problem link: https://leetcode.com/problems/n-th-tribonacci-number/
# Author: Dyanara Dela Rosa
# Date: June 16, 2024

class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci_memoize = [0, 1, 1]

        if len(tribonacci_memoize) > n:
            return tribonacci_memoize[n]
        
        for i in range(len(tribonacci_memoize), n+1):
            tribonacci_memoize.append(tribonacci_memoize[i-1] + tribonacci_memoize[i-2] + tribonacci_memoize[i-3])

        return tribonacci_memoize[n]