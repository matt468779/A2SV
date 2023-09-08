class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(2, numRows+1):
            res.append([1])
            for j in range(i-2):
                res[-1].append(res[-2][j] + res[-2][j+1])
            res[-1].append(1)
            
        return res