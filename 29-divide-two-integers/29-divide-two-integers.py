class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            pos = True
            if divisor < 0:
                dividend = -dividend
                divisor = -divisor
        else:
            pos = False
            if divisor < 0:
                divisor = -divisor
            else:
                dividend = -dividend
                
        if divisor == 1:
            if not pos:
                dividend = -dividend
            if dividend > 2147483647:
                dividend = 2147483647
            elif dividend <= -2147483648:
                dividend = -2147483648
            return dividend
        
        s = 0
        q = 1
        quot = 0
        div = divisor
        while s+div+div <= dividend:
            while s+div+div <= dividend:
                div += div
                q += q
                s += div
                quot += q
            div = divisor
            q = 1

        if s+divisor <= dividend:
            quot += 1
        
        return quot if pos else -quot