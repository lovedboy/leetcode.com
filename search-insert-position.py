class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        s = 0
        e = len(nums)
        while s <= e:
            m = (s+e)/2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s = m+1
            else:
                e = m-1
        return s
