class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        self.res = 0
        def dfs(node):
            if node > n//2:
                return cost[node-1]
            
            left = dfs(2*node)
            right = dfs(2*node + 1)
            self.res += abs(left - right)
            
            return cost[node-1] + max(left, right)
        
        dfs(1)
        return self.res