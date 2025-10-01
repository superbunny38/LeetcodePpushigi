class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sorting
        # Time: O(nlogn)
        # Space: O(n) (Python TimSort의 경우)
        # return sorted(s) == sorted(t)

        # Counter: 아래와 기본적으로 목표는 똑같음
        # Alphabet만 들어온다면 이게 더 효율적 (n < 26)
        # Time: O(n)
        # Space: O(n)
        # return Counter(s) == Counter(t)

        # Two strings are anagrams if they have the same characters with the same frequencies.
        # Time: O(n)
        # Space: O(1) (O(26))

        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        for c in t:
            cnt[ord(c) - ord('a')] -= 1

        return not any(cnt)