class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add_nodes_with_carry(head1, head2, carry):
            added = head1.val + head2.val
            total = added + carry
            if total > 9:
                carry = 1
                total = total % 10
            else:
                carry = 0
            return total, carry
        
        head1 = l1
        head2 = l2
        carry = 0
        
        added, carry = add_nodes_with_carry(head1, head2, carry)
        ans = ListNode(val=added, next=None)
        res = ans
        head1 = head1.next
        head2 = head2.next
        
        while head1 and head2:
            added, carry = add_nodes_with_carry(head1, head2, carry)
            res.next = ListNode(val=added, next=None)
            res = res.next
            head1 = head1.next
            head2 = head2.next
        
        remaining = head1 or head2
        
        while remaining:
            total = remaining.val + carry
            if total > 9:
                carry = 1
                total = total % 10
            else:
                carry = 0
            remaining = remaining.next
            res.next = ListNode(val=total, next=None)
            res = res.next
        
        if carry == 1:
            res.next = ListNode(val=carry, next=None)
            res = res.next
        
        return ans
