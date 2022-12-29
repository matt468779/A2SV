class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        indS, indT = 0, 0
        while indS < len(s) and indT < len(t):
            if s[indS] == t[indT]:
                indT += 1
            indS += 1

        return len(t) - indT
