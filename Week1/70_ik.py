from functools import cache


class Solution:
    # Recursive: 피보나치
    # Time: O(n) (Cache 없으면? O(2^n))
    # Space: O(n) (Recursion Stack)
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs_memo(self, n: int) -> int:
        memo = {}

        def helper(n):
            if n <= 2:
                return n
            if n in memo:
                return memo[n]

            memo[n] = helper(n - 1) + helper(n - 2)
            return memo[n]

        return helper(n)

    # DP
    # Time: O(n)
    # Space: O(1) (일반 DP는 n인데 Dynamic DP는 1임)
    def climbStairs_dp(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1  # n-2 위치
        prev1 = 2  # n-1 위치

        for i in range(3, n + 1):
            curr = prev1 + prev2  # 현재 계단 방법 수

            # Sliding Window
            prev2 = prev1
            prev1 = curr

        return prev1

    # DP Array
    # Time: O(n)
    # Space: O(n)
    def climbStairs_dp(n):
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
