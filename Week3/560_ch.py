from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return 1
        