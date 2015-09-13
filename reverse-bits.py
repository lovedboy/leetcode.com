# https://leetcode.com/problems/reverse-bits/

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        for x in range(0, 32):
            num += (n & 1) * (1 << (31 -x) )
            n >>= 1
        return num





