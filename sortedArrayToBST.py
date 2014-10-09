import math

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if num is None:
            return None
        if len(num) == 0:
            return None
        if len(num) == 1:
            return TreeNode(num[0])
        
        mid = int(math.floor(len(num) / 2))
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid:])
        
        return root

nums = [1, 2, 3]

print(Solution().sortedArrayToBST(nums).right.val)