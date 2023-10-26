class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[-1]*n for _ in range(n)]
        for i, j, weight in times:
            graph[i-1][j-1] = weight
        
        q = [(0, k-1)]
        time = [float('inf')] * n
        time[k-1] = 0
        visited = set()
        while q:
            t, node = heapq.heappop(q)
            
            if node in visited or t > time[node]:
                continue
            for neighbor in range(n):
                if graph[node][neighbor] == -1:
                    continue
                time[neighbor] = min(time[neighbor], t+graph[node][neighbor])
                heapq.heappush(q, (time[neighbor], neighbor))
            visited.add(node)
            
        res = max(time)
        if res == float('inf'):
            return -1
        
        return res