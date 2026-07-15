# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_p = None

        while head:
            temp_p = head.next
            head.next = prev_p
            prev_p = head
            head = temp_p

        return prev_p

        