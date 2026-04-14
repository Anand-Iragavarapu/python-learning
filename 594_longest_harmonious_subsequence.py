class Solution:
    def findLHS(self, nums):
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        result = 0
        # check each number in the dictionary
        for num in freq:
            # A harmonious subsequence must contain both num and num + 1
            if num + 1 in freq:
                # The length is the sum of the counts of both numbers
                result = max(result, freq[num] + freq[num + 1])
        
        return result
