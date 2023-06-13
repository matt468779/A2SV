class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [0, 1, 1]
        for i in range(3, n+1):
            trib.append(trib[-1] + trib[-2] + trib[-3])
        
        return trib[n]