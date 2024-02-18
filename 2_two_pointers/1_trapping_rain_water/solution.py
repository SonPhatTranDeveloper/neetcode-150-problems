"""
The idea of this solution is to find the water held at all index i
The water held at index i is calculated using min(L, R) - height[i]
where L is the maximum height to the left of index i
and R is the maximum height to the right of index i
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Create arrays to hold the maximum left and right heights
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        # Find the max left and right array
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i-1])

        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])

        # Find the amount of water trapped
        trapped = 0

        for i in range(len(height)):
            current_trapped = max(min(max_left[i], max_right[i]) - height[i], 0)
            trapped += current_trapped

        return trapped