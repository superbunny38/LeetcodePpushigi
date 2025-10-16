from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r,cur= 0,n-1,n-1
        
        res = [0 for _ in range(n)]
        
        while cur>=0:
            if abs(nums[r])>abs(nums[l]):
                res[cur] = abs(nums[r])*abs(nums[r])
                r-=1
            else:
                res[cur] = abs(nums[l])*abs(nums[l])
                l+=1
            cur -=1
        return res
    
s = Solution().sortedSquares(nums=[-7,-3,2,3,11])
print(s)