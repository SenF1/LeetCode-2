# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        left = self.rangeSumBST(root.left, low, high)
        right = self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            return left + right + root.val
        else:
            return left + right
