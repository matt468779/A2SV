class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m, p, g = 0, 0, 0
        for i in range(len(garbage)-1, -1, -1):
            if m == 0 and 'M' in garbage[i]:
                m = i
            if g == 0 and 'G' in garbage[i]:
                g = i
            if p == 0 and 'P' in garbage[i]:
                p = i
            
            if m!=0 and g!=0 and p!=0:
                break
        
        travel_presum = [0] * len(garbage)
        
        for i in range(len(travel)):
            travel_presum[i+1] = travel_presum[i] + travel[i]

        res = travel_presum[m] + travel_presum[p] + travel_presum[g]

        for g in garbage:
            res += len(g)
            
        return res