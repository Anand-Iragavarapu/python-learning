# LeetCode #1 - Two Sum
# Problem: Given a list of numbers and a target, return indices of two numbers that add up to target
# Approach: Hashmap - for each number, check if its partner already exists in dictionary
# Time complexity: O(n)


class Solution:
    def twoSum(self, nums, target):
        seen = {}  # we create an empty dictionary
        
        for i in range(len(nums)):  # we walk through one number at a time
            need = target - nums[i]  # we check what number do I need
            
            if need in seen:  
                return [seen[need], i]  # return two indices
            
            seen[nums[i]] = i  # add current number to notebook
        
        return []
