"""
Using a variant of bucket sort, mapping the count to the items which have that count
Time complexity: O(nlogn)
Author: Son Phat Tran
"""

from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Cache all the numbers in a dictionary
        counts = defaultdict(lambda: 0)
        for num in nums:
            counts[num] += 1

        # Map count to elements having the counts
        mapping = []
        for _ in range(len(nums) + 1):
            mapping.append([])

        for item in counts:
            mapping[counts[item]].append(item)

        # Get the top-k elements
        results = []
        index = len(nums)
        while len(results) < k:
            while len(mapping[index]) == 0:
                index -= 1
            results += mapping[index]
            index -= 1

        return results
