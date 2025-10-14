'''Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

class Solution:
    def minSubArrayLen(self, target, nums):
        
        left_idx = 0
        cur_sum = 0
        min_length = float('inf')
        
        for right_idx in range(len(nums)):
            cur_sum += nums[right_idx]
            while cur_sum >= target:
                cur_length = right_idx - left_idx + 1
                min_length = min(min_length, cur_length)
                cur_sum -= nums[left_idx]
                left_idx += 1
                    
        return min_length if min_length!=float('inf') else 0
    
print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print()
print()
print(Solution().minSubArrayLen(target=2,nums=[8]))
print(Solution().minSubArrayLen(target = 4, nums = [1,4,4]))
print(Solution().minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))