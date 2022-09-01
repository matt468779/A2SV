class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = float('inf')
        for s in strs:
            short = min(short, len(s))
            
        res = 0
        for i in range(short):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:res]
            res += 1
            
        return strs[0][:res]