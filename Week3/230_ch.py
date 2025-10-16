# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ret_val = 0
        self.k = k
        self.inorder(root)
        return self.ret_val
    
    def inorder(self,root):
        if root is None or self.k<=0:
            return
        self.inorder(root.left)
        self.k -=1
        if self.k == 0:
            self.ret_val = root.val
        self.inorder(root.right)
        
root = TreeNode(val=3)
one = TreeNode(val=1)
two = TreeNode(val=2)
four = TreeNode(val=4)
root.left = one
root.right = four
one.right = two
s = Solution().kthSmallest(root=root, k = 1)
print(s)