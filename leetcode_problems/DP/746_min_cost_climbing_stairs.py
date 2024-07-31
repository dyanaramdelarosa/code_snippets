# Problem Link: https://leetcode.com/problems/min-cost-climbing-stairs/
# Author: Dyanara Dela Rosa
# Date: June 18, 2024

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_cost = [0, 0]
        for i in range(2, len(cost)+1):
            total_cost.append(min(total_cost[i-1]+cost[i-1], total_cost[i-2]+cost[i-2]))
        
        return total_cost[len(cost)]