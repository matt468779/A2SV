class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        bits = [2**i for i in range(len(nums2))]
        state = [0]
        dp = {}
        def solve(i):
            if (i, state[0]) in dp:
                return dp[(i, state[0])]
            
            if i >= len(nums1):
                return 0
            
            res = float('inf')
            for j in range(len(nums2)):
                if not state[0] & bits[j]:
                    state[0] |= bits[j]        
                    res = min(res, (nums1[i] ^ nums2[j]) + solve(i+1))
                    state[0] ^= bits[j]
            
            dp[(i, state[0])] = res
            return res
        
        return solve(0)
