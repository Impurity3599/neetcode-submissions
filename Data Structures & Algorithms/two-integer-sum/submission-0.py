class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbIdx = {}

        for idx, numb in enumerate(nums):
            opp = target - numb
            if opp in numbIdx:  
                 return(    [numbIdx[opp], idx]) 
            
            numbIdx[numb] = idx

        return -1