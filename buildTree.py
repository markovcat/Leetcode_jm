# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if inorder is None and postorder is None:
            return None
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        root = TreeNode(postorder[-1])
        print(inorder)
        print(postorder)
        print(postorder[-1])
        indexRoot = inorder.index(postorder[-1])
        
        leftSubtree_inorder = inorder[:indexRoot]
        rightSubtree_inorder = inorder[indexRoot + 1:]
        leftSubtree_postorder = postorder[:len(leftSubtree_inorder)]
        rightSubtree_postorder = postorder[len(leftSubtree_inorder):-2]
        
        root.left = self.buildTree(leftSubtree_inorder, leftSubtree_postorder)
        root.right = self.buildTree(rightSubtree_inorder, rightSubtree_postorder)
        
        return root

inorder = [1,2,3,4]
postorder = [3,4,2,1]
print(Solution().buildTree(inorder, postorder))