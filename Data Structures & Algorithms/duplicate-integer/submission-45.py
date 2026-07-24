class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        inspector_pool = []

        for num in (nums):
            if num in inspector_pool:
                return True
            else:
                inspector_pool.append(num)
        return False
        
        
        

            
        



        
        