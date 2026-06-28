"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {}
        
        def get_copy(node):
            if node is None:
                return None
            if node not in seen:
                seen[node] = Node(node.val)
            return seen[node]
        curr = head
        while curr:
            copy = get_copy(curr)
            copy.next = get_copy(curr.next)
            copy.random = get_copy(curr.random)
            curr = curr.next
        return get_copy(head)
