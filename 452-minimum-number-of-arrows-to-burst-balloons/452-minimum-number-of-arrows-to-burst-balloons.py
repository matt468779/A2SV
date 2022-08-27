class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        points.append([float('inf'), float('inf')])
        i = 0
        res = 0
        while i < len(points)-1:
            j = i
            left = points[i][0]
            right = points[i][1]
            while j < len(points) and left <= right:
                j += 1
                left = max(left, points[j][0])
                right = min(right, points[j][1])

            i = j
            res += 1

        return res