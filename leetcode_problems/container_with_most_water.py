# Problem Link: https://leetcode.com/problems/container-with-most-water/
# Author: Dyanara Dela Rosa
# Date: July 30, 2024


class Solution:
    def compute_area(self, x0: int, x1: int, y0: int, y1: int) -> int:
        return (x1 - x0) * min(y0, y1)

    def maxArea_brute_force(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                computed_area = self.compute_area(i, j, height[i], height[j])
                if max_area < computed_area:
                    max_area = computed_area

        return max_area

    def maxArea(self, height: List[int]) -> int:
        max_area, i, j = 0, 0, len(height)-1
        while i<j:
            area = self.compute_area(i, j, height[i], height[j])
            if max_area < area: max_area = area
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
        return max_area
