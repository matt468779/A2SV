class Solution:
    def decodeString(self, s: str) -> str:
        def get_num(i):
            while i < len(s) and s[i].isdigit():
                i += 1
            return i
        
        def get_end_bracket(j):
            open_bracket = 1
            while j < len(s) and open_bracket:
                if s[j] == '[':
                    open_bracket += 1
                elif s[j] == ']':
                    open_bracket -= 1
                j += 1
            return j
        
        def solve(l, r):
            if s[l:r].isalpha():
                return list(s[l:r])
            
            res = []    
            i = l
            while i < r:
                if s[i].isalpha():
                    res.append(s[i])
                elif s[i].isdigit():
                    j = get_num(i)
                    num = int(s[i:j])
                    left = j+1
                    right = get_end_bracket(j+1)
                    res.extend(solve(left, right-1)*num)
                    i = right-1
                i += 1
            
            return res
        
        return ''.join(solve(0, len(s)))