from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        def _rob(nums):
            if len(nums) == 0:
                return nums
            elif len(nums) == 1:
                return nums[0]
            elif len(nums) == 2:
                return max(nums)
            else:
                dp = [nums[0],max(nums[0],nums[1])]
                
                for idx in range(2,len(nums)):
                    dp.append(max(dp[-1],dp[-2]+nums[idx]))
                return dp[-1]
        
        return max(_rob(nums[:-1]),_rob(nums[1:]))
            
            
    
s = Solution().rob(nums=[0])
print(s)
print()
s = Solution().rob(nums=[2,1,3,1])
print(s)
print()
s = Solution().rob(nums=[1,2,3,1])
print(s)
print()
s = Solution().rob(nums=[1,2,3])
print(s)
print()
