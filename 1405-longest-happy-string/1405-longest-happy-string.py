class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = []
        if a > 0:
            chars.append([-a, 'a'])
        if b > 0:
            chars.append([-b, 'b'])
        if c > 0:
            chars.append([-c, 'c'])
        heapq.heapify(chars)
        
        res = []
        while len(chars) >= 1:
            largest = heapq.heappop(chars)
            if len(res) < 2 or res[-1] != largest[1] or res[-2] != res[-1] == largest[1]:
                res.append(largest[1])
                largest[0] += 1
            elif chars:
                secondLargest = heapq.heappop(chars)
                res.append(secondLargest[1])
                secondLargest[0] += 1
                if secondLargest[0] <= -1:
                    heapq.heappush(chars, secondLargest)
            else:
                break
                
            if largest[0] <= -1:
                heapq.heappush(chars, largest)

        return ''.join(res)