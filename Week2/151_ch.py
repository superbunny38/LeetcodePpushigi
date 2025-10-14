import time
class Solution:
    def reverseWords(self, s: str) -> str:
        ret = ''
        left_idx = 0
        while s[left_idx] == ' ':
            left_idx += 1
        is_before_space = False
        while left_idx < len(s):
            print("left_idx:",left_idx,"letter:",s[left_idx])
            print("ret: ",ret)
            # time.sleep(2)
            if s[left_idx] != ' ':
                # print(f"s[left_idx] != ' ', s[left_idx]:{s[left_idx]}")
                broke_bc_space = False
                for right_idx in range(left_idx+1,len(s)):
                    if s[right_idx] == ' ':
                        broke_bc_space = True
                        break
                if broke_bc_space:
                    ret = s[left_idx:right_idx]+ret
                    left_idx = right_idx
                else:
                    ret = s[left_idx:right_idx+1]+ret
                    return ret
            else:# s[left_idx] == ' ':
                is_letter_behind = False
                for right_idx in range(left_idx+1,len(s)):
                    if s[right_idx] == ' ':
                        continue
                    else:
                        is_letter_behind = True
                        break
                if is_letter_behind:
                    ret = ' '+ret
                    left_idx = right_idx
                else:
                    return ret
        return ret
        
s = Solution().reverseWords("the sky is blue")
print(s)