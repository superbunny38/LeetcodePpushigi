from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left<right:
            mid = (left+right)//2
            count = 0
            for p in piles:
                count += math.ceil(p/mid)
            
            if count <= h:
                right = mid
            elif count > h:
                left =mid+1
              
        return left

s = Solution().minEatingSpeed(piles = [3,6,7,11], h = 8)
print(s)
print()
print()
s = Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 5)
print(s)
print()
print()
s = Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 6)
print(s)
print()
print()