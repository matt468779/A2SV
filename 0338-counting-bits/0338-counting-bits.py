class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [None] * (n+1)
        for i in range(n+1):
            res[i] = i & 1
            j = i >> 1
            while j:
                if res[j] != None:
                    res[i] += res[j]
                    break
                res[i] += j & 1
                j >>= 1
        
        return res