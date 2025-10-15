from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = dict()
        
        for idx,num in enumerate(nums):
            find_ = target-num
            if num in find:
                return [find[num],idx]
            find[find_] = idx
            
s = Solution().twoSum(nums=[2,7,11,15],target=9)
print(s)