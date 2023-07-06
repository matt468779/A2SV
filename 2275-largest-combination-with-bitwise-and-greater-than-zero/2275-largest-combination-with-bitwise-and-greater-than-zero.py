class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        for _ in range(32):
            temp = 0
            for i in range(len(candidates)):
                temp += 1 & candidates[i]
                candidates[i] >>= 1
            
            res = max(res, temp)
        
        return res