from typing import List
import math
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        storage = dict()

        for idx, num in enumerate(nums):
            if num not in storage:
                storage[num] = [1,idx,idx]
            else:
                storage[num][0] +=1
                storage[num][-1] = idx
        
        max_degree, min_length = 0, math.inf
        for store in storage.values():
            if max_degree < store[0]:
                max_degree = store[0]
                min_length = (store[2]-store[1]+1)
            elif max_degree == store[0]:
                min_length = min(store[2]-store[1]+1, min_length)
        return min_length
