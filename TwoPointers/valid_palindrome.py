class Solution(object):
    def isPalindrome(self, s):
        check = []
        for i in s:
            if i.isalnum():
                check.append(i.lower())  # Convert to lowercase for case-insensitive comparison

        return check == list(reversed(check))