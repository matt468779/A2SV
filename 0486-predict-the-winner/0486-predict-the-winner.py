class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def solve(left, right):
            if left > right:
                return 0
            if left == right:
                return nums[left]
            
            choice1 = nums[left] + min(solve(left+2, right), solve(left+1, right-1))
            choice2 = nums[right] + min(solve(left+1, right-1), solve(left, right-2))            
            
            return max(choice1, choice2)
        
        p1_score = solve(0, len(nums)-1)
        return p1_score >= sum(nums)/2