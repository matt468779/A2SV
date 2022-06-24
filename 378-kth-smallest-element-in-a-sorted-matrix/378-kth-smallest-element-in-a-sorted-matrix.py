class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        w = len(matrix[0])
        h = len(matrix)
        
        heap = []
        i = -1
        for i in range(k//w):
            while len(matrix[i]):
                heapq.heappush(heap, -matrix[i].pop())
        i += 1
        k = k - (k//w)*w
        while k > 0:
            heapq.heappush(heap, -matrix[i].pop())
            k -= 1

        for j in range(i, h):
            k = 0
            while k < len(matrix[j]):
                p = -matrix[j][k]
                if p > heap[0]:
                    heapq.heappushpop(heap, p)
                else:
                    break
                k += 1
                
        return -heap[0]     