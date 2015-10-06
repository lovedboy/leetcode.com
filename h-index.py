class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        c_dict = {}
        length = len(citations)
        for c in citations:
            c = length if c > length else c
            c_dict[c] = c_dict.get(c,0) + 1
        
        papers  = 0
        while length > 0:
            papers += c_dict.get(length,0)
            if papers >= length:
                return length
            length -= 1
        return 0
            