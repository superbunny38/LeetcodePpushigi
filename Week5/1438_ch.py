from typing import List
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ret,l = 0,0
        min_queue, max_queue = deque(),deque()

        
        for r in range(len(nums)):
            
            while min_queue and nums[r] < min_queue[-1]:
                min_queue.pop()
            
            while max_queue and nums[r] > max_queue[-1]:
                max_queue.pop()
            
            min_queue.append(nums[r])
            max_queue.append(nums[r])
            
            while max_queue[0] - min_queue[0]>limit:
                if nums[l] == max_queue[0]:
                    max_queue.popleft()
                if nums[l] == min_queue[0]:
                    min_queue.popleft()
                l+=1
            
            ret = max(ret,r-l+1)
        return ret
        