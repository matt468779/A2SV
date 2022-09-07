class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * len(cost)
        memo.extend([0, float('inf')])

        for i in range(len(cost)-1, -1, -1):
            memo[i] = cost[i] + min(memo[i+1], memo[i+2])

        return min(memo[0], memo[1])