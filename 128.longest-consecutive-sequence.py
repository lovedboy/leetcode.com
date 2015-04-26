#https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        
        temp_dict = { i:False for i in nums }

        longest = 0
        for num in nums:

            if temp_dict[num] is True:
                continue

            length = 0
            k = num

            while k in temp_dict:

                length += 1
                temp_dict[k] = True
                k += 1

            k = num - 1

            while k in temp_dict:

                length += 1
                temp_dict[k] = True
                k -= 1

            longest = max(longest, length)


        return longest