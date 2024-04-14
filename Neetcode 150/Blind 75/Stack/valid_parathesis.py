"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "{": "}", "[": "]"}
        closed = [")", "}", "]"]
        seen = []
        for ch in s:
            if ch in closed:
                if len(seen) > 0:
                    opn = seen.pop()
                    if dic[opn] != ch:
                        return False
                else:
                    return False
            else:
                seen.append(ch)

        if len(seen) == 0:
            return True
        return False
