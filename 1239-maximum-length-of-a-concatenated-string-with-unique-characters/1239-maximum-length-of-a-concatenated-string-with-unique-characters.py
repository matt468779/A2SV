class Solution:
    def maxLength(self, arr: List[str]) -> int:
        longest = 0
        unique_set = set()
        def solve(idx):
            
            if idx >= len(arr):
                return len(unique_set)
            
            choice1 = 0
            if check_in_set(arr[idx]):
                unique_set.update(set(arr[idx]))
                choice1 = solve(idx+1)
                for char in arr[idx]:
                    unique_set.discard(char)
            choice2 = solve(idx+1)
            
            return max(choice1, choice2)
            
        def check_in_set(word):
            if len(word) != len(set(word)):
                return False
            
            for char in word:
                if char in unique_set:
                    return False
            return True
        
        return solve(0)
