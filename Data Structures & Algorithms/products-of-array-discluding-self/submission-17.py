class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1] * n

        left = 1
        for i in range(n):
            product[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            product[i] *= right
            right *= nums[i]
        
        return product
