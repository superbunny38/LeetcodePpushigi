# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(depth, node) -> int:
            if not node:
                return depth
            depth += 1
            left, right = helper(depth, node.left), helper(depth, node.right)
            return max(left, right)

        return helper(0, root)


