class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = [[] for _ in range(len(bombs))]
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                dist = (bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2
                if i != j and dist <= bombs[i][2]**2:
                    graph[i].append(j)
        
        def bfs(i):
            q = deque([i])
            visited = set()
            while q:
                popped = q.popleft()
                visited.add(popped)
                for j in graph[popped]:
                    if j not in visited:
                        q.append(j)
            
            return len(visited)
        
        res = 0
        for i in range(len(bombs)):
            res = max(res, bfs(i))
            
        return res