class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        lastIndex = 0
        citations.sort()
        print(citations)
        for i in range(0, len(citations)):
            countgt = 0
            counteq = 0
            for j in range(lastIndex, len(citations)):
                if citations[j] > i+1:
                    countgt += 1
                elif citations[j] == i+1:
                    counteq += 1

            if countgt > i+1:
                continue
            if counteq + countgt >= i+1:
                h = i+1

            lastIndex += counteq
        
        return h