'''
Problem Statement 

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''

from functools import reduce

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 9 :
            return num
        while num > 9:
            ListA = list(str(num))
            num = int(reduce(lambda x,y: int(x)+int(y),ListA))

        return num
