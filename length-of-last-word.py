# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1 = 0
        l2 = 0
        for item in s:
            if item != ' ':
                l1 += 1
            else:
                l2 = l1 if l1 else l2
                l1 = 0
        return l1 if l1 else l2
