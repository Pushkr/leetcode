'''
Problem Statement :
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

from functools import reduce

# Using XOR operation. 
class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y : x^y,nums)

# not efficient
class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = dict([(nums.count(x),x) for x in nums])
        return dict1[1]
 
# not efficient
 class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dummy = []
        for i in range(len(nums)):

            if  nums[i] not in dummy and nums.count(nums[i]) == 1 :
                return nums[i]
                break
            else:
                dummy.append(nums[i])
 
 
