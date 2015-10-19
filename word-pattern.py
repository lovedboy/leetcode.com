class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p_dict = {}
        matched_str = {}
        s_list = str.split()
        
        if len(s_list) != len(pattern):
            return False
            
        for i in xrange(0, len(pattern)):
            p = p_dict.get(pattern[i])
            if p is None:
                if s_list[i] in matched_str:
                    return False
                p_dict[pattern[i]] = s_list[i]
                matched_str[s_list[i]] = ''
            else:
                if p != s_list[i]:
                    return False
        return True
            
            
            