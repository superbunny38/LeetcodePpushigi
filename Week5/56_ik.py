from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = []

        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        result = []

        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                last = result.pop()

                if interval[0] <= last[1]:
                    if interval[1] <= last[1]:
                        result.append(last)
                    else:
                        result.append([last[0], interval[1]])
                else:
                    result.append(last)
                    result.append(interval)
        return result
