import math

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True
            
        leftHeight = self.getDepth(root.left)
        rightHeight = self.getDepth(root.right)
        return math.fabs(leftHeight - rightHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1
        

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)

A.left = B
B.left = C
A.right = D
D.right = E

print(Solution().isBalanced(A))