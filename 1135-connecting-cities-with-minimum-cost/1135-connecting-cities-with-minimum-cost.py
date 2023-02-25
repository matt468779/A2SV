class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
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
                return True
            return False
        
        connections.sort(key=lambda x: x[2])
        res = 0
        for connection in connections:
            if connection[0] not in parent:
                make_set(connection[0])
            if connection[1] not in parent:
                make_set(connection[1])
            
            if union_sets(connection[0], connection[1]):
                res += connection[2]

        repr_count = 0
        for city in range(1, n+1):
            if city not in parent:
                make_set(city)
            if city == parent[city]:
                repr_count += 1
            if repr_count > 1:
                return -1
            
        return res