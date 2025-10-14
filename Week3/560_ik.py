from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Accumulated Sum
        # If for some index j, there exists an index i s.t. s_j - s_k = k (j > k),
        # then [k:j] is one of our answers
        # Keep the count of accum sum in hashmap and for s_j, find (s_j - k) in hashmap and add cout of it.

        acc_sum = accumulate(nums)
        cnt_map = defaultdict(int)
        # For initial value
        cnt_map[0] = 1
        cnt = 0
        for s in acc_sum:
            target = s - k
            if target in cnt_map:
                cnt += cnt_map[target]
            cnt_map[s] = cnt_map[s] + 1
        return cnt
