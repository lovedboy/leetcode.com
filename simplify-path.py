# https://leetcode.com/problems/simplify-path/

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        p = ''
        length = len(path)
        for i in xrange(0, length+1):
            if i >= length:
                s = '/'
            else:
                s = path[i]
            if s == '/':
                if p == '..':
                    if stack:
                        stack.pop(-1)
                elif p == '.':
                    pass
                elif p:
                    stack.append(p)
                p = ''
            else:
                p += s
        
        return '/' + '/'.join(stack)