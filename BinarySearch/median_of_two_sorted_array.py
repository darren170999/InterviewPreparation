class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary Search is needed
        # We will need to create a left and right partition
        # find the mid point with a mid = m+n//2, set nums2 to be smaller always
        # initially we partition the smaller one by half with a left and right pointer
        # Compare if left partitions' rightmost is <= right partition's leftmost for both cases
        # If true return the minimum of the two for odd, and return the avg of the two for even
        # If not true, we update the left pointer to mid+1 and update the partitions
        # Bigger partition is found by taking half - len(smaller's left partition)
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total+1) // 2
        if n > m:
            nums1, nums2 = nums2, nums1
            n,m = m,n
        l, r = 0, n
        while l<=r: # nums2 is always smaller size
            mid = (l+r)//2
            temp = half - mid
            # dont exceed
            left2 = nums2[mid - 1] if (mid > 0) else float('-inf')
            left1 = nums1[temp - 1] if (temp > 0) else float('-inf')
            right2 = nums2[mid] if (mid < n) else float('inf')
            right1 = nums1[temp] if (temp < m) else float('inf')
            if left1 <= right2 and left2 <= right1: # found the correct left and right partitions
                if total%2==0:
                    return (max(left2, left1) + min(right1, right2)) /2.0
                return max(left1, left2) 
            elif (left2 > right1):
                r = mid - 1
            else:
                l = mid + 1

            

            