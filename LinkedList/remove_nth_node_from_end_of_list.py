# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse LL
        # traverse again and remove that item
        # reverse again
        if head and head.next is None: # len 1
            return None
        elif head.next.next is None and head.next: # len 2
            if(n==1):
                head.next = None
                return head
            if n== 2:
                head = head.next
                return head
        else: # len 3 and above
            curr = head
            prev = None
            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            # here prev holds reversed LL
            new = prev
            while n > 2:
                new = new.next
                n -= 1
            if(n==2):
                new.next = new.next.next
            else:
                prev = new.next
                new.next = None
                new = prev
            c = prev
            prv = None
            while c is not None:
                t = c.next
                c.next = prv
                prv = c
                c=t
            return prv