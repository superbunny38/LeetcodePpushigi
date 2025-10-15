from typing import List
import math

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        current_pos = 0
        
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            
            if current_pos == i:
                current_pos = farthest
                jumps +=1
        return jumps
    
s = Solution().jump(nums=[1,2,1,1,1])
print(s)
print()
s = Solution().jump(nums=[2,3,0,1,4])
print(s)
print()