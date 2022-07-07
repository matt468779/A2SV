class MedianFinder:

    def __init__(self):
       self.h1 = []
       self.h2 = []

    def addNum(self, num: int) -> None:
        if len(self.h1) > len(self.h2):
            heapq.heappush(self.h2, -heapq.heappushpop(self.h1, -num))
        elif len(self.h1) < len(self.h2):
            heapq.heappush(self.h1, -heapq.heappushpop(self.h2, num))
        else:
            if len(self.h1) == 0 or num <= self.h2[0]:
                heapq.heappush(self.h1, -num)
            else:
                heapq.heappush(self.h2, num)

    def findMedian(self) -> float:
        if len(self.h1) > len(self.h2):
            return -self.h1[0]
        elif len(self.h1) < len(self.h2):
            return self.h2[0]
        else:
            return (-self.h1[0] + self.h2[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
