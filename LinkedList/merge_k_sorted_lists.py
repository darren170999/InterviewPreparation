class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Binary merging, merge two lists at a time and combine them into one list
        k = len(lists)
        if not lists or k == 0:
            return None

        def mergeTwoLists(list1, list2):
            if(list1 == None):
                return list2
            if(list2 == None):
                return list1
            head = ListNode()
            current = head
            while list1 and list2:
                if(list1.val >= list2.val):
                    current.next = list2
                    list2 = list2.next
                else:
                    current.next = list1
                    list1 = list1.next
                current = current.next
            current.next = list1 or list2
            return head.next
        while k > 1:
            ans = []
            for i in range(0, k , 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < k else None
                ans.append(mergeTwoLists(l1, l2))
            lists = ans
            k = len(lists)
        return lists[0]