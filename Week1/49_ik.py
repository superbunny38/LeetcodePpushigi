from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Algorithm으로는 Sorting보다 Count가 빨라야 하는데 Leetcode상에서는 그렇지 않음
        1. Python의 sort, join은 C 레벨에서 최적화됨.
        2. Python의 문자열 hashing은 빠름 ("xxx".append("yyy"))
        3. Python의 Tuple hashing은 느림 (m[(0,1,0,...)].append("apple"))
        4. Count에서는 [0] * 26 을 매번 loop을 돌때마다 memalloc. List size가 커질수록 비효율적

        Count 방식을 빠르게 하려면?
        1. 튜플 대신 문자열 키 사용
            m["1a2b1c"].append(string)  # 빈도수를 문자열로
        2. 고정 크기 대신 실제 문자만
            from collections import Counter
            m[frozenset(Counter(string).items())].append(string)
        3. C 확장 사용
            import numpy as np  # NumPy 배열은 C 레벨
        """


        # Sorting
        # Time: O(n*klogk) (k: max length of a string in strs)
        # Space: O(n * k)
        #
        # m = defaultdict(list)
        # for string in strs:
        #     key = ''.join(sorted(string))
        #     m[key].append(string)
        # return list(m.values())

        # Count
        # Time: O(n*k)
        # Space: O(n) (O(n * 26))
        m = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            m[tuple(count)].append(string)
        return list(m.values())