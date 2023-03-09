class Solution:
    def lastRemaining(self, n: int) -> int:
        def solve(step, first, last, left_to_right):
            if first == last:
                return first
            
            if (last-first) % step == 0:
                return solve(step*2, first+step//2, last-step//2, not left_to_right)
            elif left_to_right:
                return solve(step*2, first+step//2, last, not left_to_right)
            else:
                return solve(step*2, first, last-step//2, not left_to_right)
                
        return solve(2, 1, n, True)
    