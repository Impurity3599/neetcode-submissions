class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for idx, val in enumerate(nums):
            nums[idx] = (val ** 2)
        
        l = 0
        r = 1
        count = 0
        while l <= r and r < len(nums) and count < len(nums) :
            if nums[l] > nums[r]:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l+=1
            r+=1

            if r >= len(nums):
                print("here")
                count+=1
                r= 1
                l=0

        return nums