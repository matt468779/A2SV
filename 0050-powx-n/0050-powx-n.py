class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n == -1:
            return 1/x
        elif n == 0:
            return 1
        
        elif n % 2 == 0:
            res = self.myPow(x, n//2)
            return res * res
        elif n > 1 and n % 2 == 1:
            res = self.myPow(x, n//2)
            return x * res * res
        elif n < -1 and n % 2 == 1:
            res = self.myPow(x, (n//2)+1)
            return 1/x * res * res