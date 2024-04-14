"""

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while left != right:
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] == target:
                    return left
                elif nums[left] > target:
                    left = mid + 1
                elif nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif target > nums[mid] and nums[right] >= target:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2

        return -1 if nums[left] != target else left


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1  # Calculate the middle index

            if nums[mid] == target:
                return mid  # Return the index if target is found

            if nums[mid] >= nums[left]:
                # Check if the left half is sorted and target is within this range
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Adjust right boundary
                else:
                    left = mid + 1  # Adjust left boundary
            else:
                # Check if the right half is sorted and target is within this range
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Adjust left boundary
                else:
                    right = mid - 1  # Adjust right boundary

        return -1  # Return -1 if target is not found

"""
