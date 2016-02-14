class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            s = 0
            while num > 0:
                s += (num -  num / 10 * 10)
                num = num / 10
            num = s
        return num