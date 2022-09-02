class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        lword = len(words[0])
        wordDict = {}
        for word in words:
            wordDict[word] = wordDict.get(word, 0) + 1
            
        i = 0
        res = []
        while i < len(s) - lword + 1:
            j = i
            perm = wordDict.copy()
            word = s[j:j+lword]
            while j < len(s) - lword + 1 and word in perm:
                if perm[word] > 1:
                    perm[word] -= 1
                else:
                    perm.pop(word)
                j += lword
                word = s[j:j+lword]

            if not perm:
                res.append(j - lword*len(words))
                
            i += 1
            
        return res