class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        visited = set()
        temp = []
        res = []
        candidates.sort()
        def solve(target, i):
            state = tuple(temp)
            if state in visited:
                return
            visited.add(state)
            if target == 0:
                res.append(list(temp))
                return
            
            for j in range(i, len(candidates)):
                if target < candidates[j]:
                    break
                
                temp.append(candidates[j])
                solve(target-candidates[j], j+1)
                temp.pop()
        
        solve(target, 0)
        return res