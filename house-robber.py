
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''



class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, x):
        if len(x)  == 0:
            return 0
        elif len(x) <=2:
            return max(x)
        else:
            a1 = x[0]
            a2 = x[1]
            a3 = x[2]
            
            return self.rob([ max(a1,a2),a1+a3] + x[3:])


# print Solution().rob([2,1,1,2])