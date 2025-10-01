from functools import cache

# 피보나치
class Solution:
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
