class Solution:
    def findMin(self, nums: List[int]) -> int:
        numsLen = len(nums)
        if numsLen == 1:
            return nums[0]
        
        minVal = 1000

        l = 0
        r = numsLen - 1

        while l <= r and l >= 0 and r < numsLen:
            m = int((l + r) /2)

            #figure out which part we are in(left or right)
            #rotated (except if rotated the len of list) means there
            #is a left and right part
            #both parts are sorted
            #left part is the just the last n - some at the beg of list
            #right part is the just the untouched part at the end of thelist
            #right part by logic houses the smallest numbers

            #if # at m is greater than # at l
            #we are in the left side, we must adjust search to look at the right part

            if nums[m] >= nums[l]:
                minVal = min(nums[l], minVal)

                l = m + 1 #move index to mid + 1 b/c we have crossed out left part
            #we are in the right part of list
            #where the smallest numbers are
            #we need to go left in the right part to get the 
            #smallest number now

            elif nums[m] < nums[l]:
                minVal = min(nums[m], minVal)
                r = m -1
                
        return minVal