class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        if root.left is None:
            return self.minDepth(root.right) + 1

        if root.right is None:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        # current = []
        # next = [root]
        # current_depth = 0
        # while next:
        #     current_depth += 1
        #     current = next
        #     next = []
        #     print([node.val for node in current])
        #     while current:
        #         node = current.pop()
        #         if node.left is None or node.right is None:
        #             return current_depth
        #         else:
        #             next.append(node.left)
        #             next.append(node.right)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)

A.left = B
A.right = C
B.left = D


print(Solution().minDepth(A))