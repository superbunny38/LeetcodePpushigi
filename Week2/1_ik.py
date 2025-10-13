from typing import List


class Solution:
    # Two Pointers
    # Time: O(nlogn) (sort)
    # Space: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1


    # Hash Table
    # Time: O(n)
    # Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for idx, num in enumerate(nums):
            search = target - num
            if search in cache:
                return [idx, cache[search]]
            cache[num] = idx
