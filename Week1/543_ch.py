from typing import List, Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def depth(node):
    if node is None:
        return 0
    return 1+max(depth(node.left),depth(node.right))

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return max(depth(root.left) + depth(root.right), self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
    
