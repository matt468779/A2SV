class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1 and maxDoubles:
            if target % 2:
                target -= 1
                res += 1
            else:
                target = target // 2
                res += 1
                maxDoubles -= 1
        
        if target > 1:
            return res + target-1
        return res