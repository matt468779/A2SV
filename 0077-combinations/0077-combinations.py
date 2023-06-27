class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = []
        res = []
        def solve(i):
            if len(temp) == k:
                res.append(list(temp))
                return
            
            if i > n:
                return
            
            temp.append(i)
            solve(i+1)
            temp.pop()

            solve(i+1)
                
        solve(1)
        return res