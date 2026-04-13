# LeetCode #217 - Contains Duplicate
# Problem: Return True if any number appears more than once and False if all are unique
# Approach: Set store seen numbers, check before adding
# Time complexity: O(n) 

class Solution(object):
    def containsDuplicate(self, nums):
        
        seen = set()  # empty set 
        
        for i in range(len(nums)):  # we walk through each number one by one
            
            if nums[i] in seen: 
                return True  # yes if duplicate found
            
            seen.add(nums[i])  # no then add current number to set and keep going
        
        return False  # finished the whole list and no duplicates found
