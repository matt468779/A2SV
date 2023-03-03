class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        
        nums_even = []
        nums_odd = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums_even.append(nums[i])
            else:
                nums_odd.append(nums[i])
                
        operations = 0
        even_idx = 0
        odd_idx = 0
        for i in range(len(target)):
            if target[i] % 2 == 0:
                operations += abs(target[i]-nums_even[even_idx]) // 2
                even_idx += 1
            else:
                operations += abs(target[i]-nums_odd[odd_idx]) // 2
                odd_idx += 1
        
        return operations // 2 