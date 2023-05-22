# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Slow-fast pointer! 
        # Will eventually catch up to slow pointer if loop exists
        # Check if the node in front of fast exists. 
        slow = fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False