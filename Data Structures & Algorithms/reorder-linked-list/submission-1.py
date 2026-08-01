# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        r_curr = slow.next
        slow.next = None

        # reverse second half
        prev = None

        while r_curr:
            nxt = r_curr.next
            r_curr.next = prev
            prev = r_curr
            r_curr = nxt

        # merge
        list_1 = head
        list_2 = prev

        while list_1 and list_2:
            temp = list_1.next
            list_1.next = list_2
            list_1 = list_1.next
            list_2 = temp
        
