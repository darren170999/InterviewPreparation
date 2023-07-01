# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # ones, tens, hundreds
        head1 = l1 # use head1 as ans
        head2 = l2
        carry = 0
        # Check if same length -> not possible
        # Alternative, make an ans ll ->. store tabulated 
        # if ans is None break while
        added = head1.val + head2.val
        total = added+ carry
        if(total>9):
            carry = 1
            total = total %10
        else:
            carry = 0
        ans = ListNode(val = total, next=None) # storing answer
        res = ans
        head1 = head1.next
        head2 = head2.next
        while head1 and head2:# accounted for if they are the same
            added = head1.val + head2.val
            total = added + carry
            if total > 9:
                carry = 1
                total = total%10
            else:
                carry = 0
            res.next = ListNode(val = total, next=None)
            res = res.next
            head1 = head1.next
            head2 = head2.next
        # print(carry)
        while head1 or head2: # this will append and check for carry diff
            if head1:
                total = head1.val + carry
                if(total>9):
                    carry = 1
                    total = total%10
                else:
                    carry = 0
                head1 = head1.next
            else: # head 2 exists
                total = head2.val + carry
                if(total > 9):
                    carry = 1
                    total = total%10
                else:
                    carry = 0
                head2 = head2.next                
            res.next = ListNode(val = total, next=None)
            res = res.next
        if carry == 1:
            res.next = ListNode(val = carry, next=None)
            res= res.next
        return ans