class Solution:
    def getSum(self, a: int, b: int) -> int:
        def sumTwo(a, b):
            res = 0
            carry = 0
            i = 1
            while a or b or carry:
                first = a & 1
                second = b & 1

                s = first ^ second ^ carry
                carry = first&second | first&carry | second&carry

                res |= i * s
                i *= 2

                a >>= 1
                b >>= 1

            return res

        def diffTwo(a, b):
            isNeg = False
            if a < 0 and abs(a) > abs(b):
                isNeg = True
            elif b < 0 and abs(b) > abs(a):
                isNeg = True
                
            a, b = max(abs(a), abs(b)), min(abs(a), abs(b))
            res = 0
            i = 1
            while a or b:
                first = a & 1
                second = b & 1
                res |= (second^first) * i

                if not first and second:
                    mask = 1
                    while not mask & a:
                        a |= mask
                        mask *= 2
                    a &= ~mask
                
                i *= 2
                a >>= 1
                b >>= 1
            
            return -res if isNeg else res
        
        if a < 0 and b < 0:
            return -sumTwo(-a, -b)
        if a >= 0 and b >= 0:
            return sumTwo(a, b)
        
        return diffTwo(a, b)
        
        
        