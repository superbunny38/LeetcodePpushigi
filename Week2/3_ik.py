class Solution:
    # Sliding Window
    # Time: O(n)
    # Space: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n, left = len(s), 0
        cache = {}
        cnt = 0

        for r in range(n):
            if s[r] in cache:
                # 중복된 문자가 left보다 왼쪽에 있을 수도 있으므로 max
                # ex) abba
                left = max(left, cache[s[r]] + 1)
            cache[s[r]] = r
            cnt = max(cnt, r - left + 1)

        return cnt

    # Brute Force
    # Time: O(n^2)
    # Space: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n in (0, 1):
            return n

        cnt = 0
        for l in range(n):
            cache = set()
            for r in range(l, n):
                if s[r] in cache:
                    break
                cache.add(s[r])
                if r - l + 1 > cnt:
                    cnt = r - l + 1
        return cnt
