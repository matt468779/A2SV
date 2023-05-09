class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            q_ind = 0
            p_ind = 0
            
            while p_ind < len(pattern) and q_ind < len(query):
                if query[q_ind] == pattern[p_ind]:
                    p_ind += 1
                elif query[q_ind].isupper():
                    break
                q_ind += 1
                
            is_match = False
            if p_ind == len(pattern):
                is_match = True
                for i in range(q_ind, len(query)):
                    if query[i].isupper():
                        is_match = False
                        break
                
            
            res.append(is_match)
        
        return res