class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.res = []
        def findNext(num, l):
            if l == n:
                self.res.append(num)
                return 
            lastDig = num%(10)
            if lastDig + k < 10 and k != 0:
                findNext(num*10+(lastDig+k), l+1)
            if lastDig - k > -1:
                findNext(num*10+(lastDig-k), l+1)
        
        for i in range(1, 10):
            findNext(i, 1)
        
        return self.res
                