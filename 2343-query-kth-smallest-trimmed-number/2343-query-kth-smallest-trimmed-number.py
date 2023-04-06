class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        sorted_to_k = []
        l = len(nums[0])
        for i in range(1, l+1):
            temp = [0] * len(nums)
            for j in range(len(nums)):
                temp[j] = (nums[j][l-i:], j)
            temp.sort()
            sorted_to_k.append(temp)

        res = []
        for k, trim in queries:
            res.append(sorted_to_k[trim-1][k-1][1])
        
        return res