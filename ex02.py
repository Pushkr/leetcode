'''
Problem Statement :
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return (len(s))
        else:
            lenList = 0
            temp = ''
            i = 0
            while i < len(s):
                if s[i] not in temp:
                    temp = temp + s[i]
                else:
                    if len(temp) > lenList:
                        lenList = len(temp)
                    i = i - len(temp) + 1
                    temp = s[i]
                i += 1

            if len(temp) > lenList:
                lenList = len(temp)
            return lenList
