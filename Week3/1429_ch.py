from typing import List
from collections import Counter

class FirstUnique:
    
    def __init__(self, nums: List[int]):
        self.f_distr = Counter(nums)
        
    def showFirstUnique(self) -> int:
        for key, value in self.f_distr.items():
           if value != 1:
               continue
           else:
               return key
        return -1       
    def add(self, value: int) -> None:
        self.f_distr[value] +=1
        return None

obj = FirstUnique(nums=[2,3,5])
# print(obj)
param_1 = obj.showFirstUnique()
print(param_1)
obj.add(5)
param_1 = obj.showFirstUnique()
print(param_1)
obj.add(2)
param_1 = obj.showFirstUnique()
print(param_1)
obj.add(3)
param_1 = obj.showFirstUnique()
print(param_1)