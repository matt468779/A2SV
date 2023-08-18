class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]
        for road in roads:
            graph[road[0]].add(road[1])
            graph[road[1]].add(road[0])
        
        res = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    res = max(res, len(graph[i]) + len(graph[j]) - (i in graph[j]))
        
        return res