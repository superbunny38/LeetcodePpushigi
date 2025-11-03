import heapq
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        lst = sorted([(v, k) for k, v in cnt.items()], key=lambda x: -x[0])
        return [key for _, key in lst[:k]]

    # Heap Sort
    # Time: O(nlogk) -> if k << n optimal
    # Space: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return heapq.nlargest(k, cnt, key=cnt.get)

    # Bucket Sort
    # Time: O(n)
    # Space: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        length = len(nums)
        buckets = [[] for _ in range(length + 1)] # freq: 0 ~ n

        for num, freq in cnt.items():
            buckets[freq].append(num)

        results = []
        for freq in range(length, 0, -1):
            results.extend(buckets[freq])
            if len(results) >= k:
                return results[:k]

