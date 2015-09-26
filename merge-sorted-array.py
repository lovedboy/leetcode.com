# https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        length = m
        
        while i < length and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                t = length
                while t > i:
                    nums1[t] = nums1[t-1]
                    t -=1
                nums1[i] = nums2[j]
                j += 1
                i += 1
                length += 1
        
        for t in xrange(j, n):
            nums1[length] = nums2[t]
            length += 1
