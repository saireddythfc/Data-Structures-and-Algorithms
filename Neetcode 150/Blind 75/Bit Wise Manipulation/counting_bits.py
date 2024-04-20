"""

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            ans[i] = 1 + ans[i - offset]
            # ans.append(bin(i).count('1'))
        return ans


# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         bits=[0,1,1,2]
#         if n<4:
#             return bits[:n+1]
#         k=1
#         while len(bits)<=n:
#             for i in range (k*4):
#                     bits.append(bits[i]+1)
#             k*=2
#         return bits[:n+1]
