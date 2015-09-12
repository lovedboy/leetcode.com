# https://leetcode.com/problems/single-number/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):

        x = 0
        for num in nums:
            x ^= num
        return x
