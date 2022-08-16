class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ind = {}
        res = []
        nums.sort()
        nums.append(inf)
        if nums[0] > 0 or nums[-1] < 0:
            return []
        boundary1 = -1
        boundary2 = -1
        for i in range(len(nums)):
            ind[nums[i]] = i
            if boundary1 == -1 and nums[i] >= 0:
                boundary1 = i
            if boundary2 == -1 and nums[i] > 0:
                boundary2 = i
        
        if boundary2 - boundary1 >= 3:
            res.append([0,0,0])

        for i in range(boundary1):
            if nums[i] != nums[i-1]:
                for j in range(i+1, boundary2):
                    if nums[j] != nums[j+1] and -nums[i] - nums[j] in ind:
                        res.append([nums[i], nums[j], -nums[i]-nums[j]])

        for i in range(boundary2, len(nums)-1):
            if nums[i] != nums[i-1]:
                for j in range(i+1, len(nums)-1):
                    if nums[j] != nums[j+1] and -nums[i] - nums[j] in ind:
                        res.append([nums[i], nums[j], -nums[i]-nums[j]])
        
        return res