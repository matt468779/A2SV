class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        mp = {skill : i for i, skill in enumerate(req_skills)} # digitized skills
        
        cand = []
        for skills in people: 
            val = 0
            for skill in skills: 
                val |= 1 << mp[skill] # digitized skill
            cand.append(val)
        
        @cache
        def fn(i, mask): 
            """Return smallest sufficient team of people[i:] for skills in mask."""
            if mask == 0: return []
            if i == len(people): return [0]*100 # impossible
            if not (mask & cand[i]): return fn(i+1, mask)
            return min(fn(i+1, mask), [i] + fn(i+1, mask & ~cand[i]), key=len)
        
        return fn(0, (1 << len(req_skills)) - 1)