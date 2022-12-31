class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {}
        for i in range(len(order)):
            orderDict[order[i]] = i
        orderDict['X'] = -1

        def isGreater(word1, word2):
            word1 += 'X'
            word2 += 'X'
            l = min(len(word1), len(word2))
            for i in range(l):
                if orderDict[word1[i]] > orderDict[word2[i]]:
                    return True
                elif orderDict[word1[i]] < orderDict[word2[i]]:
                    return False

            return False
        
        for i in range(len(words)-1):
            if isGreater(words[i], words[i+1]):
                return False
        return True
