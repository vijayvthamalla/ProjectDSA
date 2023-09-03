"""
169. Majority Element
Easy
16.6K
483
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List


def majorityElement(nums: List[int]) -> int:
    m = len(nums) // 2
    prev = nums[0]
    count = 1

    for i in range(1, len(nums)):
        if nums[i] != prev and count != 0:
            count -= 1
        elif nums[i] != prev and count == 0:
            count = 1
            prev = nums[i]
        else:
            count += 1
        nums[i] = count
    return prev
