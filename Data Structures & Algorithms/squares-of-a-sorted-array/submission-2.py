class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        l = 0
        r = len(nums)-1
        res = []

        while l<=r:
            l_val = nums[l] **2
            r_val = nums[r] **2

            if l_val > r_val:
                res.insert(0,l_val)
                l+=1
            else:
                res.insert(0,r_val)
                r-=1

        return res