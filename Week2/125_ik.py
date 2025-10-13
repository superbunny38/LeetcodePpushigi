class Solution:
    # Time: O(n)
    # Space: O(n)
    def isPalindrome(self, s: str) -> bool:
        l = [c for c in s.lower().replace(" ", "") if c.isalnum()]
        return l == l[::-1]

    # faster
    # Time: O(n)
    # Space: O(n)
    def isPalindrome(self, s: str) -> bool:
        lst = [c for c in s.lower().replace(" ", "") if c.isalnum()]

        l, r = 0, len(lst)-1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        return True