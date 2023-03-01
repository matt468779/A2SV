class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_score = []
        for i in range(len(scores)):
            age_score.append((ages[i], scores[i]))
        
        res = 0
        age_score.sort()
        dp = [0] * len(scores)
        for i in range(len(scores)-1, -1, -1):
            dp[i] = age_score[i][1]
            max_possible = 0
            for j in range(i+1, len(scores)):
                if age_score[j][1] >= age_score[i][1]:
                    max_possible = max(max_possible, dp[j])
            
            dp[i] += max_possible
            res = max(res, dp[i])
            
        return res