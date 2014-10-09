# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False
        return self.compareTrees(root.left, root.right) and root.left.val == root.right.val
    
    def compareTrees(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        # root1 and root2 not None
        if root1.val != root2.val:
            return False
        else:
            return self.compareTrees(root1.right, root2.left) and self.compareTrees(root1.left, root2.right)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(2)
D = TreeNode(3)
E = TreeNode(3)
A.left = B
A.right = C
B.right = D
C.left = E

print(Solution().isSymmetric(A))