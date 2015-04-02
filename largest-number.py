
'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num.sort(cmp = Solution.cmp , reverse=True)
        print num
        num_str = ''.join([str(i) for i in num])
        num_str = num_str.rstrip('0')
        return num_str if num_str != '' else '0'

    @staticmethod
    def cmp(a,b):

        sab = str(a) + str(b)
        sba = str(b) + str(a)
        if sab > sba:
            return 1
        elif sab == sba:
            return 0
        else:
            return -1
        

# print Solution().largestNumber([3, 30, 34, 5, 9])