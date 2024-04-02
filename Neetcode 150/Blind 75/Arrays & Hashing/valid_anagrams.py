"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def lowStr(x: str) -> str:
            return "".join(sorted(x)).lower()

        return lowStr(s) == lowStr(t)

        ## Optimal:
        """
        if len(s) != len(t):
            return False
        x = set(s)
        for i in x:
            if s.count(i) != t.count(i):
                return False
        return True
        """
