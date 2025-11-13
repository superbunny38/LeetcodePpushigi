from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sum_ = 0
        sums[sum_] = 1
        ret = 0
        # if len(nums) == 1:
        #     return (nums[0] == k)*1
        
        for num in nums:
            sum_ += num
            
            
            # j>i
            # sum_j-sum_i = k
            # sum_i = k - sum_
            if sum_-k in sums:
                ret+=sums[sum_-k]
            sums[sum_] +=1
        return ret

# s = Solution().subarraySum(nums=[1,1,1], k=2)
# print(s)

# s = Solution().subarraySum(nums=[1,1,1,1,1], k=2)
# print(s)

s = Solution().subarraySum(nums=[1], k=0)
print(s)

s = Solution().subarraySum(nums=[1,2,3], k=3)
print(s)