# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        time_to_infect_tree, _ = self.dfs(root, start)
        return time_to_infect_tree

    def dfs(self, root, start):
        if root == None:
            return -1, -1

        left_infect_time, left_distance = self.dfs(root.left, start)
        right_infect_time, right_distance = self.dfs(root.right, start)
		
        if left_distance == -1 and right_distance == -1:
            distance = -1
            infect_time = max(right_infect_time, left_infect_time) + 1

        elif left_distance != -1:
            distance = left_distance + 1
            infect_time = max(left_infect_time, right_infect_time + left_distance + 2)
           
        else:
            distance = right_distance + 1
            infect_time = max(right_infect_time, left_infect_time + right_distance + 2)

        if root.val == start:
            distance = 0

        return infect_time, distance