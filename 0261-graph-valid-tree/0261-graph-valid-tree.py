class Solution:   
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = {}
        rank = {}
        def make_set(v):
            parent[v] = v
            rank[v] = 1

        def find_sets(v):
            if v == parent[v]:
                return v
            parent[v] = find_sets(parent[v])
            return parent[v]

        def union_sets(v1, v2):
            par_v1 = find_sets(v1)
            par_v2 = find_sets(v2)

            if par_v1 != par_v2:
                if rank[par_v1] > rank[par_v2]:
                    par_v1, par_v2 = par_v2, par_v1

                parent[par_v1] = par_v2
                rank[par_v2] += rank[par_v1]
                return False
            return True
        
        for edge in edges:
            if edge[0] not in parent:
                make_set(edge[0])
            if edge[1] not in parent:
                make_set(edge[1])
            
            if union_sets(edge[0], edge[1]):
                return False
        
        repr_count = 0
        for node in range(n):
            if node not in parent:
                make_set(node)
            if parent[node] == node:
                repr_count += 1
            if repr_count > 1:
                return False
        return True