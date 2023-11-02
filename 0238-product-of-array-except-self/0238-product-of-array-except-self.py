class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = [0] * len(nums)
        countZero = 0
        zeroIndex = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                countZero += 1
                zeroIndex = i
                if countZero == 1:
                    continue

            if countZero > 1:
                return res
            
            product *= nums[i]
            
        if countZero == 1:
            res[zeroIndex] =  product
            return res

        for i in range(len(nums)):
            res[i] = product // nums[i]

        return res