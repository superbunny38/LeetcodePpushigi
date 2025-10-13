from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # Already processed
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = (nums[i] + nums[left] + nums[right])
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # 현재 찾은 Left, Right와 중복되는 것들은 모두 무시
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 현재 찾은 Left, Right와 완전히 다른 값부터 재탐색
                    left += 1
                    right -= 1

                elif s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
        return result


