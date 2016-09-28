'''
Problem Statement 
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function,
nums should    be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        for i in range(count):
            nums.remove(0)
        nums.extend([0]*count)
        
        
 #Other solution that failed "in-place" requirement 
 
 class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead
        """
        count = nums.count(0)
        nums = list(filter(lambda x : x!=0,nums))
        nums.extend([0]*count)

# This didnt work because nums = list(..) creates a new list object local 
# rather than modifying calling object's nums.
