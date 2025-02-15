# Problem Link: https://leetcode.com/problems/4sum/
# Author: Dyanara Dela Rosa
# Date: Feb 15, 2024


import math
from collections import Counter

class Solution:
    def add_solution(self, solutions, solution):
        for soln in solutions:
            if soln == solution:
                return
        solutions.append(solution)

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        solutions = []

        nums_len = len(nums)
        if nums_len < 4:
            return solutions

        unique_chars = len(Counter(nums))
        # optimization: combination with repetition
        # if max number of solutions are already met, stop checking other possible combinations
        possible_solns = math.factorial(unique_chars + 4 - 1)/(math.factorial(4)*math.factorial(unique_chars-1))
        print(f"{possible_solns=}")
        nums.sort()
        for a in range(nums_len-3):
            for b in range(a+1, nums_len-2):
                sub_target = target - nums[a] - nums[b]
                # two pointer here
                c = b+1
                d = nums_len-1
                while c < d:
                    partial_sum = nums[c] + nums[d]
                    if partial_sum == sub_target:
                        # print(f"solution: [{nums[a]=}, {nums[b]=}, {nums[c]=}, {nums[d]=}]")
                        # print(f"indices: [{a=}, {b=}, {c=}, {d=}]")
                        self.add_solution(solutions, [nums[a], nums[b], nums[c], nums[d]])
                        if len(solutions) == possible_solns:
                            return solutions
                        c+=1
                        d-=1
                    elif partial_sum < sub_target:
                        c += 1
                    else:
                        d -= 1

        return solutions
