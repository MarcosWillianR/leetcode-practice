# Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array

# You are given an integer array nums of length n. 
# Create an array ans of length 2n where:

# ans[i] == nums[i] and 
# ans[i + n] == nums[i] for 
# 0 <= i < n (0-indexed).

# Example 1:
# Input: nums = [1,4,1,2]
# Output: [1,4,1,2,1,4,1,2]

nums = [1,4,1,2]

def getConcatenation(nums):
    ans = [None] * (len(nums) * 2) # array of ans 2n
    p = 0

    for i in range(0, len(ans)):
        if p == len(nums):
            p = 0 # will help to reset the pointer if the pointer points to the end of the length of nums.

        ans[i] = nums[p] # ans[i] == nums[i]
        p += 1
    
    print(ans)
    return ans


getConcatenation(nums)
  