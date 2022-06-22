class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frq = {}
        for word in words:
            if word in frq.keys():
                frq[word] -= 1
            else:
                frq[word] = -1
                
        resHeap = []
        for key in frq.keys():
            resHeap.append((frq[key], key))
        heapq.heapify(resHeap)
        temp = heapq.heappop(resHeap)
        res = [temp[1]]
        lastEq = 0
        sameFrq = temp[0]
        for j in range(1, k):
            temp = heapq.heappop(resHeap)
            res.append(temp[1])
            
            if temp[0] == sameFrq:
                i = len(res)-1
                while i < lastEq and res[i] < res[i-1]:
                    res[i], res[i-1] = res[i-1], res[i]
                    i -= 1
            else:
                lastEq = j
                sameFrq = temp[0]
        return res