class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def solve(target, i):
            if target < 0:
                return
            if target == 0:
                res.append(list(temp))
                return
            
            for j in range(i, len(candidates)):
                temp.append(candidates[j])
                solve(target-candidates[j], j)
                temp.pop()
                        
        solve(target, 0)
        return res