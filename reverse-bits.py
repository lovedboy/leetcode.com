# https://leetcode.com/problems/reverse-bits/

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit = bin(n)[2:]
        bit = (32 - len(bit)) * '0' + bit
        print bit
        s = 1
        sum = 0
        for b in bit:
            sum += int(b) * s
            s <<= 1
        return sum

