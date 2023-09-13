class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        count_sorted = sorted(count.values(), reverse = True)
        res = 0
        unique_val = float('inf')

        for val in count_sorted:
            if val < unique_val:
                unique_val = val
            else:
                unique_val = max(0, unique_val-1)
                res += val - unique_val
                
        return res