class Solution:
    def reverse(self, x: int) -> int:
        maxInt = 214748364
        sign = -1 if x < 0 else 1
        x = sign * x
        res = 0
        while x > 0:
            mod = x % 10
            res = res * 10 + mod
            x = x // 10
            if res > maxInt and x%10 > 0:
                return 0
            elif res == maxInt and x%10 >= 2:
                return 0
            
        return sign*res