# https://leetcode.com/problems/two-sum/


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        
        temp_dict = {}
        for i in xrange(0, len(nums)):
            num = nums[i]
            if target - num not in temp_dict:
                temp_dict[num] = i + 1
            else:
                return temp_dict[target-num],i+1