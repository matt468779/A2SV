class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        s = sorted(list(s))
        t = sorted(list(t))
        i = 0
        while i < len(s) and s[i] == t[i]:
            i += 1

        return t[i]
