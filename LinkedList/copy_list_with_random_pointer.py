"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # Step 1: Create a copy of each node and insert it next to the original node
        curr = head
        while curr: # if A-B-C-None => A-A'-B-B'-C-C'-None
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Set the random pointers for the copied nodes
        curr = head # reset curr to head
        while curr: 
            # if curr has a random pointer, the next one will too
            # Next Node's random point to curr's random next
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next # go to the next non-prime

        # Step 3: Separate the original list and the copied list
        new_head = head.next
        curr = head
        while curr.next:
            temp = curr.next
            curr.next = temp.next
            curr = temp

        return new_head
        # if head is None:
        #     return None
        # ans = copy = curr = head
        # while curr :
        #     tmp = Node(curr.val, curr.next, curr.random)
        #     curr.next = tmp
        #     curr= curr.next.next
        # while copy:
        #     if(copy.random != None):
        #         copy.random = copy.random.next
        # res = ans = copy.next
        # while ans and ans.next: # remove every alt node
        #     temp = ans.next
        #     ans.next = ans.next.next
        #     temp.next = None
        #     ans = ans.next
        # return res