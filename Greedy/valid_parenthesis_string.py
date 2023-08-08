class Solution:
    def checkValidString(self, s: str) -> bool:
        # wildcard involved, * can be anything Use 3 recursive calls, when wildcard is met At the end we have nothing if its true If start or end wrongly straigt return false but...
        # Theres a trick to solve this in linear time
        # use leftMin and leftMax to represent range of possibilities
        # leftMin cannot be below 0, reset to 0 when it dips to negative
        # if leftMax is -ve, we return False instantly
        leftMin, leftMax = 0, 0
        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            # rmb that these two values represent what are the range of possibilites, so we decrement leftMin, treat * as ) and increment leftMax, treat * as (
            else: # wildcard
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0: # to protect against this edge case, s: (*)(
                leftMin = 0
        return leftMin == 0
