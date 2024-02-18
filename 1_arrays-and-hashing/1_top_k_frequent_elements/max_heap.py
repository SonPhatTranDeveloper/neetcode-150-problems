"""
Count the items and store them in a max heap, so the time complexity is k * log n instead of n * log n
Author: Son Phat Tran
"""

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Cache all the numbers in a dictionary
        counts = defaultdict(lambda: 0)
        for num in nums:
            counts[num] += 1

        # Create a heap
        items = [(-counts[item], item) for item in counts]
        heapq.heapify(items)

        # Get the top-k items
        results = []
        for _ in range(k):
            item = heapq.heappop(items)
            results.append(item[1])

        return results
