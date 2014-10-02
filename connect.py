# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        # connect left and right children
        if root is None:
            return
        
        if root.left is not None and root.right is not None:
            root.left.next = root.right
            
            # connect right child with left child of current node's sibling
            if root.next is not None:
                root.right.next = root.next.left
        
            # use recursion to complete the connection
            self.connect(root.left)
            self.connect(root.right)
            
        return