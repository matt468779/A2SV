class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newIntervals = []
        i = 0
        while i < len(intervals):
            j = i
            initial = intervals[i][0]
            final = intervals[i][1]
            while( j < len(intervals)-1):
                if final >= intervals[j+1][0] or intervals[j+1][0] < intervals[i][1]:
                    if final < intervals[j+1][1]:
                        final = intervals[j+1][1]
                elif intervals[j+1][0] > final:
                    break
                
                j += 1
            newIntervals.append([initial, final])
            
            i = j+1
        return newIntervals    