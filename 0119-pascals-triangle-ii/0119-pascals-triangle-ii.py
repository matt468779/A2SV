class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def solve(row):
            if row == 0:
                return [1]
            
            top = solve(row-1)
            res = [1] * (len(top)+1)
            for i in range(len(top)-1):
                res[i+1] = top[i] + top[i+1]
        
            return res
        
        return solve(rowIndex)