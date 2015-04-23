#https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        
        first = 0
        last = len(nums)

        while first < last:
            
            mid = (first + last) / 2
            if nums[mid] == target:
                return mid

            if nums[first] <= nums[mid]:

                if target <= nums[mid] and target >= nums[first]:
                    last = mid
                else:
                    first = mid + 1
            else:
                if target < nums[first] and  target >= nums[mid]:
                    first = mid + 1
                else:
                    last = mid
        return -1

# print Solution().search([3,1],3)

