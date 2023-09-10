class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        multiplier = 1
        res = 1
        pointer = 2
        for i in range(2, n+1):
            multiplier += 2 * pointer + 1
            pointer += 2
            res = (res * (multiplier % mod)) % mod
        
        return res
            