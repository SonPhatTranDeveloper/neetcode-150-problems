"""
Normal solution to count the list, sort it and get the first k items
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

        # Sort the dictionary
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        # Return the sorted item
        return [item[0] for item in sorted_counts[:k]]
