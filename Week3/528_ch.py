from typing import List
import random

class Solution:
    def __init__(self, w: List[int]):
        self.cumulative_dist = []
        self.n = len(w)
        denom = sum(w)
        for weight in w:
            self.cumulative_dist.append(weight/denom)
        
        prev_sum = self.cumulative_dist[0]
        for i in range(1, self.n):
            self.cumulative_dist[i] = prev_sum+self.cumulative_dist[i]
            prev_sum = self.cumulative_dist[i]
        # print(self.cumulative_dist)
    
    def pickIndex(self) -> int:
        random_number = random.random()
        index = 0
        while True:
            if random_number<=self.cumulative_dist[index]:
                return index
            index +=1
            
        
# Your Solution object will be instantiated and called as such:
obj = Solution(w=[1,3])
param_1 = obj.pickIndex()
print(param_1)