# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        if root is None:
            return 0
        q = deque([root])
        while q:
            curr = q.pop()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            heapq.heappush(heap,curr.val)
        for i in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap)
            

