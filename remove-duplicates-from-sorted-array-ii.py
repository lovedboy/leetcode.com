# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fp = None
        sp = None
        length = 0
        for i in xrange(0, len(nums)):
            cur = nums[i]
            if fp == sp and fp == cur:
                continue
            elif sp is None:
                sp = cur
            else:
                fp = sp
                sp = cur
            nums[length] = cur
            length += 1
        return length
