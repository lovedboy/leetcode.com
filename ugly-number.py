# https://leetcode.com/problems/ugly-number/

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for t in [2,3,5]:
            while num % t == 0:
                num /= t
        return num == 1