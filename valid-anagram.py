class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = {}
        for key in s:
            value = s1.get(key,0)
            s1[key] = value + 1
        
        for key in t:
            v = s1.pop(key,None)
            if v is None:
                return False
            if v <=0:
                return False
            v -=1
            if v >=1:
                s1[key] = v
        if s1:
            return False
        return True
        