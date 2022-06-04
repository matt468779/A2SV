class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        mod = 1000000007
        x = pow(2,p) - 1
        return ((self.power(x-1,(x-1)//2) % mod) * (x % mod)) % mod
    
    def power (self, x, n):
        mod = 1000000007
        if n == 1:
            return x % mod
        elif n % 2 == 0:
            res = self.power(x, n//2)
            return (res%mod)**2 % mod
        elif n % 2 == 1:
            res = self.power(x, n//2)
            return (x%mod * (res%mod)**2 % mod)%mod
