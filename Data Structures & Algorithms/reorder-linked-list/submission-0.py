# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first let's divide it into 2
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev,curr = curr,nxt
        first, second = head, prev
        while second:
            nxt1,nxt2 = first.next,second.next
            first.next = second
            second.next = nxt1
            first,second = nxt1,nxt2
