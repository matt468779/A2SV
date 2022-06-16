class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        i=0
        for i in range(len(s)):
            if s[i] == '+':
                i += 1
                break
            elif s[i] == '-':
                sign = -1
                i += 1
                break
            elif s[i] == ' ':
                
                continue
            elif ord(s[i]) >= 48 and ord(s[i]) <= 57:
                break
            else:
                return 0
        while i < len(s) and s[i] == '0':
            i += 1
        res = 0
        j = i
        while i < len(s) and i-j <= 10 and ord(s[i]) >= 48 and ord(s[i]) <= 57:
            res = res*10 + ord(s[i]) - 48
            i += 1
            
        res *= sign
        if res < -2147483648:
            return -2147483648
        if res > 2147483647:
            return 2147483647
        
        return res