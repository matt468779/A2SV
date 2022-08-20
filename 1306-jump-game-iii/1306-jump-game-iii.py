class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.reached = set()
        self.q = collections.deque([start])
        
        def addToQueue(nextInd):
            if nextInd >= 0 and nextInd < len(arr) and nextInd not in self.reached:
                self.q.append(nextInd)
        
        while self.q:
            l = len(self.q)
            for _ in range(l):
                popped = self.q.popleft()
                if arr[popped] == 0:
                    return True
                
                self.reached.add(popped)
                addToQueue(popped + arr[popped])
                addToQueue(popped - arr[popped])
        return False