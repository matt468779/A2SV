class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(point):
            if parent[point] == point:
                return point
            
            parent[point] = find(parent[point])
            return parent[point]
        
        def union(point1, point2):
            parent1 = find(point1)
            parent2 = find(point2)
            
            if parent1 == parent2:
                return False
            
            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            
            return True
        
        edges = []
        for i in range(n):
            for j in range(i):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        
        edges.sort()
        res = 0
        for dist, point1, point2 in edges:
            if union(point1, point2):
                res += dist
        
        return res