class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        for idx in range(1, len(nums)):
            if nums[idx -1 ] == nums[idx]:
                return True
        
        return False
         