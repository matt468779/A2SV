class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        s = 0
        res = 0
        for i in range(1, n+1):
            if i not in banned:
                if s+i <= maxSum:
                    s += i
                    res += 1
                else:
                    break
        
        return res
        