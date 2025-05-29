# Valid Anagram
# https://leetcode.com/problems/valid-anagram

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, 
# but the order of the characters can be different.

def isAnagram(s, t):
  if len(s) != len(t):
    return False
  sorted_s = sorted(s)
  sorted_t = sorted(t)
  for idx, i in enumerate(sorted_s):
    if sorted_t[idx] != i:
      return False
  return True

isAnagram("racecar", "carrace") # True
isAnagram("jar", "jam") # False
isAnagram("banana", "nanaba") # True
isAnagram("banana", "nanababe") # False
isAnagram("xx", "x") # False