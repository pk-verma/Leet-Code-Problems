#  -> ARRAY
## Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.

 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Solution 1:
def two_sum(nums, target):
    hash_map = {} # val, index
    for i, v in enumerate(nums):
        if target - v in hash_map:
            return i, hash_map[target - v]
        else:
            hash_map[v] = i
    
# Solution 2:
def two_sum_improved(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """
    hash_map = {} # val, index
    for indx, val in enumerate(nums):
        diff = target - val
        if diff in hash_map:
            return[indx, hash_map[diff]]
        hash_map[val] = indx


"""
Both solutions utilize a hash map (dictionary in Python) to efficiently find the pair of numbers that sum up to the target value. 
    This approach reduces the time complexity from O(n^2) (which would be the case with nested loops comparing each number with every 
    other number) to O(n) because it only requires a single pass through the input array.
"""
"""
Key Improvements over O(n^2) approaches:

    - Hash Map for Efficient Lookup: The hash map allows for near-constant-time lookups to check if the complement of a number has already been encountered in the array. 
        This avoids the need for nested loops to compare every number with every other number.
    - Single Pass: Both solutions require only a single pass through the input array, making them more efficient than nested loop approaches.
"""


# Example Usage:
if __name__ == "__main__":
    nums = [2,7,11,15] 
    target = 9
    print(two_sum(nums, target))  
    print(two_sum_improved(nums, target))  