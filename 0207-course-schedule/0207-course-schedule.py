class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
            in_degree[pre[1]] += 1
        
        q = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
                
        covered = 0
        while q:
            popped = q.pop()
            for node in graph[popped]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    q.append(node)
            
            covered += 1
        
        return covered == numCourses