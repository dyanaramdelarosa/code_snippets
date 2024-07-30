# Problem Link: https://leetcode.com/problems/container-with-most-water/
# Author: Dyanara Dela Rosa
# Date: July 30, 2024


class Solution:
    def computeArea(self, x0: int, x1: int, y0: int, y1: int) -> int:
        return (x1 - x0) * min(y0, y1)

    def maxAreaBruteForce(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                max_area = max(max_area, self.computeArea(i, j, height[i], height[j]))

        return max_area

    def maxArea(self, height: List[int]) -> int:
        max_area, i, j = 0, 0, len(height)-1
        while i<j:
            max_area = max(max_area, self.computeArea(i, j, height[i], height[j]))
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
        return max_area
