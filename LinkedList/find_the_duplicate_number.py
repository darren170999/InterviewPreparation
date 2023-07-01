# Floyd's Algorithm and ll cycle
@Floyd
# init slow and fast pointers
# once we found the node that both pointers met,
# we leave slow pointer here
# next init new slow pointer and wherever they intersect
# will be the answer we are looking for
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
# here u found where the fast and slow pointeres intersect
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow # always exists