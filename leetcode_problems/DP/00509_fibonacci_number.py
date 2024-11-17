# Problem link: https://leetcode.com/problems/fibonacci-number/
# Author: Dyanara Dela Rosa
# Date: June 16, 2024

class Solution:
    def fib(self, n: int) -> int:
        fib_cache = [0, 1]

        if len(fib_cache) > n:
            return fib_cache[n]

        for i in range(len(fib_cache), n+1):
            fib_cache.append(fib_cache[i-1] +fib_cache[i-2])

        return fib_cache[n]
