class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        
        temp = [1]
        visited = set()
        for i in range(n-1):
            temp2 = []
            for num in temp:
                odd = num*2 - 1
                if odd <= n and odd not in visited:
                    temp2.append(odd)
                    visited.add(odd)
            
            for num in temp:
                even = num*2
                if even <= n and even not in visited:
                    temp2.append(even)
                    visited.add(even)
                    
            temp = temp2
            visited.clear()
        
        return temp