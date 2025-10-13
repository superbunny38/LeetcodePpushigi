from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        distribution = defaultdict(int)
        
        maxCount, maxLength = 0,0
        for s_idx in range(len(s)):
            
            distribution[s[s_idx]] += 1
            maxCount = max(maxCount,distribution[s[s_idx]])
            
            if maxLength-maxCount>=k:
                distribution[s[s_idx-maxLength]]-=1
            else:
                maxLength +=1
        
        return maxLength

s = Solution().characterReplacement(s = "ABAB",k=2)
print(s)
s = Solution().characterReplacement(s = "AABABBA",k=1)
print(s)
