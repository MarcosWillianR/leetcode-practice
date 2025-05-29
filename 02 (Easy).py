# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

def hasDuplicate(nums):
  already_in_list_nums = []
  has_duplicate = False
  for num in nums:
    if num in already_in_list_nums:
      has_duplicate = True
      break
    else:
      already_in_list_nums.append(num)
  return has_duplicate

arr1 = [1,2,3,4]
hasDuplicate(arr1) # False

arr2 = [1,2,2,3,4]
hasDuplicate(arr2) # True

arr3 = [1,2,3,1,2,3]
hasDuplicate(arr3) # True

print(hasDuplicate(arr3))