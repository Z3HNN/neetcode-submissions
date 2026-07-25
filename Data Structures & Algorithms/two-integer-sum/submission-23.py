class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            base = nums[i]
            for j in range(i + 1, len(nums)):
                s_num = nums[j]
                if (base + s_num) == target:
                    return [i,j]
