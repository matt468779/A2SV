class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # size means current size without item we are going to add
        # unique is the count of unique items
        def solve(size , unique):
            if size == goal : return 1
            if (size,unique) in dp:return dp[(size,unique)]
            ans = 0
            repeat = 0
            # check if we can repeat
            if goal - size > n - unique and size >= k+1:
                repeat = unique - k
                
            non_repeat = n - unique
            if repeat > 0:
                ans += solve(size+1,unique) * repeat
                
            ans += solve(size+1,unique+1) * non_repeat
            dp[(size,unique)] = ans
            
            return ans
        
        dp = {}
        return solve(0,0)%1000000007