class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        if i >= len(intervals) or newInterval[0] > intervals[i][1] or newInterval[0] < intervals[i][0]:
            res.append([newInterval[0]])
        else:
            res.append([intervals[i][0]])
        
        while i < len(intervals) and intervals[i][1] < newInterval[1]:
            i += 1

        if i < len(intervals) and intervals[i][0] <= newInterval[1] <= intervals[i][1]:
            res[-1].append(intervals[i][1])
            i += 1
        else:
            res[-1].append(newInterval[1])
            
        res.extend(intervals[i:])
        
        return res