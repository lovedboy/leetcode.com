class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 1, len(nums)-1
        while low <= high:
            middle = (low + high) / 2
            tmp = 0
            for x in nums:
                if x <= middle:
                    tmp +=1
                    
            if tmp > middle:
                high = middle - 1
            else:
                low = middle + 1
                
        return low