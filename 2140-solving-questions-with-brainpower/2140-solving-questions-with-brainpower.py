class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        points = { len(questions)-1 : questions[-1][0] }
        
        for i in range(len(questions)-2, -1, -1):
            points[i] = max(points.get(i+questions[i][1]+1, 0) + questions[i][0], points.get(i+1, 0))
            
        return points[0]

        
