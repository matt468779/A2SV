class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        res = 0
        for word in words:
            res += word[:n] == pref
        
        return res