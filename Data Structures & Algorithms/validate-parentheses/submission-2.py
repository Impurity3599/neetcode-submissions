class Solution:
    def isValid(self, s: str) -> bool:
        s_len = len(s)

        if s_len % 2 == 1:
            return False
        
        stack = []
        
        open_close_dict ={
            "(": ")",
            "{": "}",
            "[": "]"
        }

        idx = 0

        while idx < s_len:
            curr_char = s[idx]

            if curr_char in open_close_dict:
                stack.append(open_close_dict[curr_char])
            else:
                if len(stack) == 0:
                    return False
                expected_char = stack.pop()
                if expected_char != curr_char:
                    return False
            idx+=1
        return True if len(stack) == 0 else False