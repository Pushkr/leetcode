'''
Intersection of Two Arrays:
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # find unique elements
        set1 = set(nums1)
        set2 = set(nums2)
        
        # find the shorter set to minimize search operation
        if len(set1) <len(set2):
            shorter_set = set1
            longer_set = set2
        elif len(set1) > len(set2):
            shorter_set = set2
            longer_set = set1
        else :
            shorter_set = set1
            longer_set = set2
        
        result = []
        
        for element in shorter_set:
            if element in longer_set:
                result.append(element)
        
        return result
