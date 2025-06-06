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
    ans = [None] * (len(nums) * 2)

    # def concatenateNext():
    #     for j in range(0, len(ans)):
    #         if ans[j] is None:
    #             ans[j] = nums[j] 

    for i in range(0, len(nums)):
        # if i == len(nums):
        #     concatenateNext()
        #     break
        ans[i] = nums[i]
    
    print(ans)


getConcatenation(nums)
  