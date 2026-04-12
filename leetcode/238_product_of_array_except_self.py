class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        # build left products
        left = [1] * n
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        # build right products
        right = [1] * n
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        # multiply left and right products 
        answer = [left[i] * right[i] for i in range(n)]
        return answer
