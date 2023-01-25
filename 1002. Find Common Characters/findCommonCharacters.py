class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = sorted(list(words[0]))

        for word in words[1:]:
            tempWord = sorted(list(word))
            resPointer = 0
            wordPointer = 0
            tempRes = []
            while resPointer < len(res) and wordPointer < len(word):
                if tempWord[wordPointer] == res[resPointer]:
                    tempRes.append(res[resPointer])
                    wordPointer += 1
                    resPointer += 1
                elif tempWord[wordPointer] < res[resPointer]:
                    wordPointer += 1
                else:
                    resPointer += 1
            res = tempRes
        
        return res
