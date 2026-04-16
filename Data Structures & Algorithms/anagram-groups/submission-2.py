class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # if len(strs) ==1:
        #    return strs

        agrm = defaultdict(list)
        for x in strs:
            srtd = ''.join(sorted(x))

            agrm[srtd].append(x)
        
        return list(agrm.values())