class Solution:
    def isAnagram(self, s, t):
        count_s = {}
        count_t = {}
        
        for letter in s: # count letters in s
            if letter in count_s:
                count_s[letter] += 1 #adding 1 to existing count
            else:
                count_s[letter] = 1 #start at 1 if there is a new letter
        
        for letter in t: #count letters in t
            if letter in count_t:
                count_t[letter] += 1
            else:
                count_t[letter] = 1
        
        return count_s == count_t
