#  -> ARRAY
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2

# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.


# Example 2:

# Input: nums = [0,1]
# Output: 2

# Explanation:
# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.


# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8

# Explanation:
# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

# Constraints:

#     n == nums.length
#     1 <= n <= 104
#     0 <= nums[i] <= n
#     All the numbers of nums are unique.

 

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?



## Problem: Check list for one missing number in range[0, n]
## Solution 1:

def missing_number_solution_1(nums):

    nums.sort()  # Sort the list in place
    for i, v in enumerate(nums):
        if i != v:
            return i  # Return the missing number
    return len(nums)  # If no number is missing in the sequence
        
    ## NOTE: This solution is Nlog(N), which is relatively slow and the reason being sorting (merge or quick) in python is Nlog(N).




## Problem: Check list for one missing number in range[0, n]
## Solution 2:


def missing_number_solution_2(nums):
    ## O(N): Iterate through list and sum (twice: once for given list and once for expected using range)
    
    missing_number = sum(range(len(nums) + 1)) - sum(nums)

    """When you have multiple operations in an algorithm that each have a linear time complexity O(n), 
    and these operations are sequential (not nested), the overall time complexity of the algorithm remains linear, O(n).

    Here's how it works:

        Summing Linear Operations: If your algorithm involves several separate linear operations, such as:
            - First iterating over an array of n elements,
            - Then, in a separate loop, iterating over the same or another array of n elements,
            - And perhaps another loop doing the same, each operation has a complexity of O(n). 
                If you sum these, the resulting complexity for these sequential operations is O(n) + O(n) + O(n), and so on.

        Simplification: According to Big O notation rules, when you add complexities of the same order, 
            the overall complexity is dominated by the term that grows fastest as n increases. 
            For linear operations, O(n) + O(n) + O(n) simplifies to O(n) because the growth rate 
            in terms of the largest input size n doesn't change - it remains linear.
    """
    return missing_number

## NOTE: 
# -> Len = O(1)
# -> Range Object Creation: O(1)
# -> Sum = O(N)
# -> +1 in range(n) because n will be excluded otherwise



# Example Usage:
if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    print(missing_number_solution_2(nums))  # Output: True