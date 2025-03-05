# Problem Link: https://leetcode.com/problems/missing-number/
# Author: Dyanara Dela Rosa
# Date: Mar 5, 2025


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # max_num = 0
        # has_zero = False
        # expected_total, total = 0, 0
        # for num in nums:
        #     if num > max_num:
        #         max_num = num
        #     if num == 0:
        #         has_zero = True
        #     total += num

        # for i in range(max_num+1):
        #     expected_total += i

        # if not has_zero:
        #     return 0
        # if expected_total == total:
        #     return max_num + 1
        # return expected_total - total

        n = len(nums)
        expected_total = n*(n+1)//2
        actual_sum = sum(nums)
        return expected_total - actual_sum
