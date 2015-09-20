# https://leetcode.com/problems/move-zeroes/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[m] = nums[i]
                m += 1
        for i in range(m, len(nums)):
            nums[i] = 0