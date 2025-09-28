from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        trackSubstring = dict()
        left_idx, output= 0,1
        for idx, character in enumerate(s):
            print("on char:",character)
            if character in trackSubstring:
                left_idx = max(left_idx,trackSubstring[character] + 1)
            trackSubstring[character] = idx
            output = max(idx-left_idx+1,output)
            print("max so far:",output, "idx: ",idx,"left_idx:",left_idx)
            print("track:",trackSubstring)
            print()
        return output
ret = Solution().lengthOfLongestSubstring(s = 'abba')
print(ret)