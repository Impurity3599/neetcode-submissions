class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if t == "":
            return ""
        t_map = {}
        s_map = {}

        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        

        l = 0
        res = [-1, -1]
        resLen = float("infinity")
        curr_win = {}
        need = len(t_map)
        have = 0

        for r in range(0, len(s)):
            curr_char_r = s[r]
            
            
            curr_win[curr_char_r] = curr_win.get(curr_char_r, 0) + 1
            #if freq is the exact same, increment have
            if curr_char_r in t_map and curr_win[curr_char_r] == t_map[curr_char_r]:
                have +=1
            
           #if have == need 
            while have == need:
                #if len of substr is greater than just found sring
                if (r -l + 1 < resLen):
                    res = [l, r]
                    resLen = r-l +1 
                
                #increment l and remove character
                
                curr_char_l = s[l]
                curr_win[curr_char_l]-=1

                if curr_char_l in t_map and curr_win[curr_char_l] < t_map[curr_char_l]:
                    have-=1

                l+=1
                


        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
