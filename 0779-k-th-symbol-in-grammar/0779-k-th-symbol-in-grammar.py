class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def solve(start, end, curr):
            if start == end:
                return curr

            if (start+end) / 2 > k:
                return solve(start, (start+end)//2, curr)
            else:
                return solve((start+end)//2+1, end, int(not curr))
        
        start, end = 1, 2**(n-1)
        return solve(start, end, 0)
        
        
        