"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def lowStr(s: str) -> str:
            return "".join(sorted(s)).lower()

        dic = {}
        for s in strs:
            key = lowStr(s)
            # print(key)
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
            # print("dic", dic)

        output = []
        for k, v in dic.items():
            output.append(v)
        return output
