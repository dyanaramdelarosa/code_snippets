# Problem Link: https://leetcode.com/problems/delete-and-earn/
# Author: Dyanara Dela Rosa
# Date: July 20, 2024


from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        total = {}
        max_num = 0
        for num in count:
            total[num] = num * count[num]
            if num > max_num: max_num = num

        max_curr, max_1, max_2 = 0, 0, 0
        for num in range(1, max_num+1):
            if num in total:
                max_curr = max(total[num]+max_2, max_1)
                print(max_curr)
                max_1, max_2 = max_curr, max_1
            else:
                max_2 = max_1
        return max_curr
