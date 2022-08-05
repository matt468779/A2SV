"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:

        res = []
        for i in range(1, 1001):
            lo = 1
            hi = 1000
            while lo <= hi:
                mid = (lo + hi)//2
                cal = customfunction.f(i, mid)
                if cal == z:
                    res.append([i, mid])
                    break
                elif cal > z:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
        return res