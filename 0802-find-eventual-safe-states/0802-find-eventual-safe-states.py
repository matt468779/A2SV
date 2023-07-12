class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse_graph = [[] for _ in range(len(graph))]
        in_degree = [0] * len(graph)
        q = deque()
        
        # Reverse the graph
        for i in range(len(graph)):
            for node in graph[i]:
                reverse_graph[node].append(i)
                in_degree[i] += 1
        
        # Get the topological order
        for node in range(len(graph)):
            if in_degree[node] == 0:
                q.append(node)
        
        res = []
        while q:
            popped = q.popleft()
            res.append(popped)

            for node in reverse_graph[popped]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    q.append(node)
                        
        res.sort()
        return res