class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        in_degree = [0] * n
        graph = {}
        for edge in edges:
            in_degree[edge[1]] += 1
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
        
        todo = deque([i for i in range(n) if in_degree[i] == 0])
        
        res = [set() for _ in range(n)]
        while todo:
            l = len(todo)
            
            for _ in range(l):
                parent = todo.popleft()
                if parent not in graph:
                    continue
                for child in graph[parent]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        todo.append(child)
                        
                    res[child].add(parent)
                    res[child] = res[child].union(res[parent])
                    
                            
        for i in range(len(res)):
            res[i] = sorted(res[i])
        
        return res