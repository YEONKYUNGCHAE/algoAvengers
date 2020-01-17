# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
   def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            print(p)
            print(q)
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        resultLeft  = self.isSameTree(p.left, q.left)
        resultRight = self.isSameTree(p.right,q.right)
        return (resultLeft == resultRight)
    
        
