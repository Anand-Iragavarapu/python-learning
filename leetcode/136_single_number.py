class Solution:
    def singleNumber(self, nums):
        # empty set to track seen numbers
        seen = set()
        
        # loop through each number
        for num in nums:
            if num in seen:
                #if number is seen before, remove it 
                seen.remove(num)
            else:
                # if the number is never seen, add it
                seen.add(num)
        
        # only the single number remains
        return seen.pop()
