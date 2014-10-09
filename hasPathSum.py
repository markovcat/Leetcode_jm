# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def currentSum(self, root):
        if root is None:
            return []
        
        sums = self.currentSum(root.left) + self.currentSum(root.right)
        
        if sums:
            results = [value + root.val for value in sums]
        else:
            results = [root.val]
            
        return results
        
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        
        sums = self.currentSum(root)
        
        if sum in sums:
            return True
        else:
            return False
        

A = TreeNode(1)
B = TreeNode(2)
A.left = B
print(Solution().hasPathSum(A, 1))