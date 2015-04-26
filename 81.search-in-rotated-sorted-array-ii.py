
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):

        first = 0
        mid = len(nums) / 2

        if nums[mid] == target:
            return True

        if nums[first] > nums[mid]:
            if target < nums[first] and target > nums[mid]:
                return self.search(nums[mid+1:], target)

            else:
                return self.search(nums[:mid], target)

        elif nums[first] < nums[mid]:

            if target >= nums[first] and target < nums[mid]:
                return self.search(nums[:mid], target)
            else:
                return self.search(nums[mid+1:] ,target)

        else:
            return self.search(nums[:mid], target) or self.search(nums[mid+1:], target)