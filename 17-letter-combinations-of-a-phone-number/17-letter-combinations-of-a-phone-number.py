class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        res = collections.deque(mapping[int(digits[0])])
        for n in digits[1:]:
            l = len(res)
            s = mapping[int(n)]
            for i in range(l):
                now = res.popleft()
                for nex in s:
                    res.append(now+nex)
        
        return list(res)
            