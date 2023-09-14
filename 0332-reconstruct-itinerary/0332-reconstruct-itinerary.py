class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for dep, arr in tickets:
            graph[dep].append(arr)
        
        for dep in graph:
            graph[dep].sort(reverse=True)
            
        res = []
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            res.append(node)  

        dfs('JFK')
        return res[::-1]