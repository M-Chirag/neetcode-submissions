# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        #reach nth node, actually n-1 th node since there's a dummy
        for i in range(n+1):
            fast = fast.next
        
        #move slow and fast together so that distance is always n in between them
        while fast:
            slow = slow.next
            fast = fast.next 
        
        # remove nth node i.e link n-1 with n+1
        slow.next = slow.next.next

        #return original head
        return dummy.next 



        