from typing import List


class Solution:

    # Brute Force (v1)
    # Time: O(n^3)
    # Space: O(1)
    def subarraySum(self, nums, k):
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                # 매번 구간 합 계산
                if sum(nums[i:j + 1]) == k:  # O(n)
                    count += 1
        return count

    # Brute Force (v2)
    # Time: O(n^2)
    # Space: O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix Sum
        s = [0]
        for num in nums:
            s.append(s[-1] + num)

        cnt = 0
        for l in range(len(s) - 1):
            for r in range(l + 1, len(s)):
                if (s[r] - s[l]) == k:
                    cnt += 1
        return cnt




