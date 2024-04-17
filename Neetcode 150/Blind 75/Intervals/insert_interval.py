"""

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

"""


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        res = []
        start, end = newInterval[0], newInterval[1]

        for i, interval in enumerate(intervals):
            if start > interval[1]:
                res.append(interval)
            elif end < interval[0]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            else:
                start = min(start, interval[0])
                print(start, i)
                i += 1
                if end <= interval[1]:
                    res.append([start, interval[1]])
                    if i < len(intervals):
                        res += intervals[i:]
                    return res
                elif i == len(intervals):
                    res.append([start, end])
                    return res
                break
        else:
            res.append(newInterval)
            return res

        for idx in range(i, len(intervals)):
            if end < intervals[idx][0]:
                res.append([start, end])
                # idx += 1
                break
            elif end <= intervals[idx][1]:
                res.append([start, intervals[idx][1]])
                idx += 1
                break
        else:
            res.append([start, end])
            return res

        if idx == len(intervals):
            return res

        res += intervals[idx:]
        return res


# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

#         # Case 1: Merge the interval (new_start < curr_end and new_start > curr_start)
#         # newInterval = [min(start, curr_end), max(end, curr_end)]

#         # Case 2: Interval is smaller than newInterval
#         # append to res

#         # Case 3: Interval is Larger than newInterval
#         # append newInterval

#         res = []

#         for curr_start, curr_end in intervals:

#             # Case 1:
#             if newInterval[0] <= curr_end and newInterval[1] >= curr_start:
#                 newInterval = [min(newInterval[0], curr_start), max(newInterval[1], curr_end)]

#             elif curr_end < newInterval[0]:
#                 res.append([curr_start, curr_end])

#             else:
#                 res.append(newInterval)
#                 newInterval = [curr_start, curr_end]

#         res.append(newInterval)
