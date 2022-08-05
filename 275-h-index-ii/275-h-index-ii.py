class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lo = 0
        hi = len(citations)-1
        
        while lo < hi:
            mid = (lo+hi)//2
            if citations[mid] >= len(citations)-mid:
                hi = mid
            else:
                lo = mid+1
                
        if citations[hi] >= len(citations)-hi:
            return len(citations)-hi
        return 0 