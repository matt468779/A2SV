class Solution:
    def reorganizeString(self, s: str) -> str:
        s_counter = collections.Counter(s)
        hp = [(-count, char) for char, count in s_counter.items()]
        heapify(hp)
        
        res = []
        while len(hp) > 1:
            count1, char1 = heappop(hp)
            count2, char2 = heappop(hp)
            
            res.append(char1)
            res.append(char2)
            
            if count1 < -1:
                heappush(hp, (count1+1, char1))
            if count2 < -1:
                heappush(hp, (count2+1, char2))
            
        if hp and hp[0][0] < -1:
            return ''
        elif hp:
            res.append(hp[0][1])
        
        return ''.join(res)
        
            