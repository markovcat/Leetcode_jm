# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, root, sum, current):
        if root is None:
            return []
        if root.left is None and root.right is None and root.val == sum:
            return [li + [root.val] for li in current]
        
        return self.helper(root.left, sum - root.val, [li + [root.val] for li in current]) + \
            self.helper(root.right, sum - root.val, [li + [root.val] for li in current])
            
        
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None:
            return []
        if root.left is None and root.right is None and root.val == sum:
            return [[root.val]]
        
        current = [[root.val]]
        # print(current)
        # print(self.helper(root.left, sum - root.val, current))
        # print(self.helper(root.right, sum - root.val, current))

        return self.helper(root.left, sum - root.val, current) + self.helper(root.right, sum - root.val, current)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
A.left = B
B.left = C
print(Solution().pathSum(A, 6))