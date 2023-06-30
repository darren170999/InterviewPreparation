class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None):
            return None
        else:
            curr = head
            prev = None
            while(curr is not None): # reversing portion of ll
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev