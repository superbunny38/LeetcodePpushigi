from typing import List
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage_mapping = dict()
        ans = []
        for str in strs:
            key = ''.join(sorted(str))
            print("key:",key)
            if key in storage_mapping:
                ans[storage_mapping[key]].append(str)
            else:
                storage_mapping[key] = len(ans)
                print("storage_mapping[key] :",storage_mapping[key] )
                ans.append([str])
            
        return ans

ret = Solution().groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"])
print(ret)