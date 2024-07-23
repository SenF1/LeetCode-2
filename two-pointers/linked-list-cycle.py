# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visted_node = set()
        current_node = head
        while current_node:
            if current_node in visted_node:
                return True
            else:
                visted_node.add(current_node)
                current_node = current_node.next
        return False
        