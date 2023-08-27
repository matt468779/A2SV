class Solution:
    def canCross(self, stones: List[int]) -> bool:
        poss_stones = set(stones)
        visited = set()
        dp = {}
        def solve(curr_pos, jump):
            state = (curr_pos, jump)
            if curr_pos not in poss_stones:
                return False
            if curr_pos == stones[-1]:
                return True
            if curr_pos in visited:
                return False
            if state in dp:
                return dp[state]
            
            visited.add(curr_pos)
            
            option1 = solve(curr_pos+jump, jump)
            option2 = solve(curr_pos+jump+1, jump+1)
            option3 = solve(curr_pos+jump-1, jump-1)

            visited.remove(curr_pos)
            
            dp[state] = option1 or option2 or option3
            return dp[state]
        
        return solve(stones[0], 0)