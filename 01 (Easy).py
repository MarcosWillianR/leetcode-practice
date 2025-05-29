# Remove Duplicates From Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array

## Remover in-place
## preciso saber se o numero que eu estou vendo, eu ja vi antes, se sim, é duplicado.
## se o numero que estou vendo eh duplicado, preciso trocar o valor pelo proximo numero

def removeDuplicates(nums):
  p = 1
  for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
      nums[p] = nums[i]
      p += 1
  return p

arr1 = [1,1,2,3,4]
removeDuplicates(arr1) # Answer: nums = [1, 2, 3, 4, 4] p = 4

arr2 = [2,10,10,30,30,30]
removeDuplicates(arr2) # Answer: nums = [2, 10, 30, 30, 30, 30]   p = 4