class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            node1, node2 = edges[i][0], edges[i][1]
            graph[node1].append((node2, -log10(succProb[i])))
            graph[node2].append((node1,-log10(succProb[i])))
        
        hp = [(0, start_node)]
        prob = [float('inf')] * n
        prob[start_node] = 0
        visited = set()
        
        while hp:
            p, node = heapq.heappop(hp)
            if node in visited:
                continue
                
            for nod, probability in graph[node]:
                if probability != 'x':
                    if nod in visited:
                        continue
                        
                    curr_prob = p+probability
                    if curr_prob < prob[nod]:
                        heapq.heappush(hp, (curr_prob, nod))
                        prob[nod] = curr_prob
                    
            visited.add(node)

        if prob[end_node] == float('inf'):
            return 0
        
        return pow(10, -prob[end_node])