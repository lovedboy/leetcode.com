class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cache_dict = dict()
        while 1:
            s = 0
            while n > 0:
                s += pow(n - n/10*10,2)
                n = n/10
            if s == 1:
                return True
            if s in cache_dict:
                return False
            cache_dict[s] = 0
            n = s
