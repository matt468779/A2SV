class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n=len(nums)
        right=[inf for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            right[i]=min(right[i+1],nums[i])

        ans=inf
        left=inf
        for i in range(n):
            if left < nums[i] and right[i+1]<nums[i]:
                ans=min(ans,left+nums[i]+right[i+1])
            left=min(left,nums[i])
        if ans==inf:
            ans=-1
        return ans