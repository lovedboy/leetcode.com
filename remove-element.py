# https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        m = 0
        for i in xrange(0, len(nums)):
            if nums[i] != val:
                nums[m] = nums[i]
                m += 1
        nums = nums[0:m]
        return m