class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tmp_dict = {}
        for x in xrange(0, len(nums)):
            num = nums[x]
            index = tmp_dict.get(num)
            if index is not None and x - index <= k:
                return True
            tmp_dict[num] = x
        
        return False