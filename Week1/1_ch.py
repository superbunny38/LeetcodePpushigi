class Solution:
    def twoSum(self, nums, target):
        sorted_nums = sorted(nums)
        left_idx, right_idx = 0, len(nums)-1
        while left_idx < right_idx:
            sum_ = nums[left_idx] + nums[right_idx]
            if sum_ == target:
                return [left_idx, right_idx]
            elif sum_ < target:
                left_idx +=1
            else:
                right_idx -=1