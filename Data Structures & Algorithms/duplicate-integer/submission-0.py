class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        holder = {}
        
        for numb in nums:
           if numb not in holder:
            holder[numb] = 1
           else:
            return True
        return False

        