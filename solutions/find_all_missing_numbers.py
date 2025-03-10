#  -> ARRAY
# Find All Numbers Disappeared in an Array


# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] 
# that do not appear in nums.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:

# Input: nums = [1,1]
# Output: [2]

# Constraints:

#     n == nums.length
#     1 <= n <= 105
#     1 <= nums[i] <= n

 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.



## Problem: Check given list for missing numbers in range(1, len(nums))
## Solution 1: Time -> O(N): Iterate through range and append to new list if not in given list. O(N) space.

def find_all_missing_numbers(nums):
    set_num = set(nums)
    ret_num = []

    for i in range(1, len(nums) + 1):
        if i not in set_num:
            ret_num.append(i)
    return ret_num

## NOTE: In place negation of indices for O(1) Space


## Solution 2 -> In place negation of indices for O(1) Space
def findDisappearedNumbers(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        temp = abs(nums[i]) - 1
        if nums[temp] > 0:
            nums[temp] *= -1
            """
                - Loop through the List: The loop iterates through each element in the list nums.
                - Calculate Index: temp = abs(nums[i]) - 1 calculates the index corresponding to the value at nums[i]. The abs() function ensures that the value is positive, and subtracting 1 adjusts it to a zero-based index.
                - Negate the Value at Index: if nums[temp] > 0: nums[temp] *= -1 checks if the value at the calculated index temp is positive. If the value to mark the presence of the number nums[i].
            """
    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i+1)
            """
                - Initialize Result List: res = [] initializes an empty list to store the missing numbers.
                - Loop through the List: The loop iterates through the list nums again, using enumerate to get both the index i and the value n.
                - Check for Positive Values: if n > 0 checks if the value at index i is positive. If it is, it means the number i + 1 is missing (since it was never negated).
                - Append Missing Numbers: res.append(i + 1) appends the missing number i + 1 to the result list res.
            """
            """This approach modifies the list in place and achieves O(1) space complexity."""
    return res


# Example Usage:
if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(find_all_missing_numbers(nums))  
    print(findDisappearedNumbers(nums))