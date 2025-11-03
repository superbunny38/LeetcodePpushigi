# Brute Force
# Follow up question: "What if the input is huge? Can you avoid flattening upfront?"
# class Vector2D:
#
#     def __init__(self, vec: List[List[int]]):
#         self.lst = [x for row in vec for x in row]
#         self.curr = 0
#
#     def next(self) -> int:
#         result = self.lst[self.curr]
#         self.curr += 1
#         return result
#
#     def hasNext(self) -> bool:
#         return self.curr < len(self.lst)
from typing import List


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.row, self.col = 0, 0
        self.vec = vec
        self._skip_empty()

    def _skip_empty(self):
        while self.row < len(self.vec) and len(self.vec[self.row]) == 0:
            self.row += 1

    def next(self) -> int:
        result = self.vec[self.row][self.col]
        if len(self.vec[self.row]) - 1 == self.col:
            self.row += 1
            self.col = 0
        else:
            self.col += 1
        self._skip_empty()
        return result

    def hasNext(self) -> bool:
        return self.row < len(self.vec)
