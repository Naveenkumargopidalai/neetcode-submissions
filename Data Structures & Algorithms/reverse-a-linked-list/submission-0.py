# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            temp = curr.next      # save next node
            curr.next = prev      # reverse pointer
            prev = curr           # move prev forward
            curr = temp           # move curr forward
        
        return prev