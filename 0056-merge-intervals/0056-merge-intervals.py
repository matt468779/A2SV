class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.append([float('inf'), float('inf')])
        intervals.sort()
        res = []
        lastFirst = intervals[0][0]
        lastSecond = intervals[0][1]
        for i in range(1, len(intervals)):
            if lastFirst <= intervals[i][0] <= lastSecond:
                lastSecond = max(lastSecond, intervals[i][1])
            else:
                res.append([lastFirst, lastSecond])
                lastFirst = intervals[i][0]
                lastSecond = intervals[i][1]
        
        return res