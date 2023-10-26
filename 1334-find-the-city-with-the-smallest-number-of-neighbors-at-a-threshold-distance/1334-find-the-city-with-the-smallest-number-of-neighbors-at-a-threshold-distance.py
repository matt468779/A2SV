class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')]*n for _ in range(n)]
            
        for node1, node2, weight in edges:
            dist[node1][node2] = weight
            dist[node2][node1] = weight
        
        for i in range(n):
            dist[i][i] = 0
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        res, minNeig = 0, float('inf')
        for i in range(n):
            neighbors = 0
            for j in range(n):
                neighbors += dist[i][j] <= distanceThreshold
                
            if neighbors <= minNeig:
                res = i
                minNeig = neighbors
        
        return res