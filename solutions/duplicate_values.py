# 📝 Problem: Check for Duplicates in a List -> ARRAY

## 📌 Description
#Given an integer array `nums`, return `True` if any value appears at least twice in the array. Otherwise, return `False` if all elements are distinct.

## 🧩 Examples

### Example 1:
```python
# Input
nums = [1, 2, 3, 1]

# Output
True
```
**Explanation:** The element `1` appears twice at indices `0` and `3`.

---

### Example 2:
```python
# Input
nums = [1, 2, 3, 4]

# Output
False
```
**Explanation:** All elements are distinct.

---

### Example 3:
```python
# Input
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

# Output
True
```
**Explanation:** Multiple numbers appear more than once.

---

## 🔹 Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## 💡 Optimized Solution (Time & Space: O(N))
### Approach:
- Use a **set** to track unique numbers.
- If the size of the set is equal to the length of `nums`, then all elements are unique (`False`).
- Otherwise, duplicates exist (`True`).

### 🚀 Python Implementation:
```python
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

# Example Usage:
if __name__ == "__main__":
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(contains_duplicate(nums))  # Output: True
```

---

## ✅ Complexity Analysis
- **Time Complexity:** `O(N)`, where `N` is the number of elements in `nums`, as we iterate once to create a set.
- **Space Complexity:** `O(N)`, since a set is used to store unique elements.

---

## ✅ Notes
- **Sets are fast**: Note that an empty set cannot be created using `{}` as it creates a dictionary unless values are included.
- **Set Implementation**: Sets in Python are implemented using **hash tables**, allowing for average-case `O(1)` time complexity for lookup, insert, and delete operations.

---



