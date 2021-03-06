'''
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.
'''

from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == t or len(t) == 0:
            return ""
        elif len(s) == 0 and len(t) > 0 :
            return t
        else :
            s1 = Counter(s)
            t1 = Counter(t)
            c =  (t1 - s1)
            return list(c)[0] if len(c) > 0 else ""
