"""

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            i = dic.get(num, 0)
            if i == 0:
                dic[num] = 1
            else:
                return True
        return False

        ## Optimal:
        """
        dups = set()
        for num in nums:
            if num in dups:
                return True
            dups.add(num)
        return False
        
        """
