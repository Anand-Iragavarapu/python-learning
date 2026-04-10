# LeetCode #217 - Contains Duplicate
# Problem: Return True if any number appears more than once, False if all unique
# Approach: store seen numbers in the Set, check before adding
# Time complexity: O(n) 

class Solution(object):
    def containsDuplicate(self, nums):
        
        seen = set()  # empty set - like a notebook but only stores numbers, no indices
        
        for i in range(len(nums)):  # walk through each number one by one
            
            if nums[i] in seen:  # have I seen this number before?
                return True  # yes - duplicate found
            
            seen.add(nums[i]  # no - add current number to set and keep going
        
        return False  # finished the whole list, no duplicates found
