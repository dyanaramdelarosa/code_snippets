# Problem Link: https://leetcode.com/problems/3sum/
# Author: Dyanara Dela Rosa
# Date: July 13, 2024

class Solution:
    def has_solution(solns, target):
        for soln in solns:
            if soln == target:
                return True
        return False
    
    def brute_force(self, nums: List[int]) -> List[List[int]]:
        solns = []
        # brute force
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                for k in range(j+1, nums_len):
                    if nums[i]+nums[j]+nums[k] == 0:
                        soln = sorted([nums[i], nums[j], nums[k]])
                        if not Solution.has_solution(solns, soln):
                            solns.append(soln)
        return solns
    
    def two_pointer(self, nums: List[int]) -> List[List[int]]:
        solns = []
        nums.sort()
        i = 0

        while i < len(nums):
            j = i + 1
            k =len(nums) - 1

            while j<k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    solns.append([nums[i], nums[j], nums[k]])
                    while j+1 < len(nums) and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                elif curr_sum > 0:
                    k -= 1
                elif curr_sum < 0:
                    j += 1
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return solns


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return self.brute_force(nums)
        return self.two_pointer(nums)

    
        
