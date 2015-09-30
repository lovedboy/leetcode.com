class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmp = {}
        for num in nums:
            if num in tmp:
                return True
            tmp[num] = 0
        
        return False
        