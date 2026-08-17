# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        
        dummy = ListNode(0, head)
        curr = dummy
        for _ in range(count-n):
            curr = curr.next
        tmp = curr.next.next
        curr.next = tmp
        return dummy.next