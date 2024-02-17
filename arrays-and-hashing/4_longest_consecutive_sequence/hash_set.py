"""
This solution involves saving all numbers in a hash set, then find the starting number
with no left element, and build up the sequence from there
Note to self: Almost found the solution, but not quite
Author: Son Phat Tran
"""


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a list containing the numbers
        items = set(nums)

        # Get the longest sequence
        longest = 0

        # Find the starting elements
        for item in nums:
            if item in items:
                length = 1

                if item - 1 not in items:
                    while item + 1 in items:
                        item = item + 1
                        length += 1

                longest = max(longest, length)

        return longest


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    print(sol.longestConsecutive(nums))
