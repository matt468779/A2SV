class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        for i in range(len(isConnected)):
            if isConnected[i][i]:
                stack = [i]
                while stack:
                    c = stack.pop()
                    if isConnected[c][c]:
                        stack.extend([j for j in range(len(isConnected[0])) if isConnected[c][j]])
                        isConnected[c][c] = 0
                provinces += 1
        return provinces
