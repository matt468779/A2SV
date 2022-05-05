class Solution:
    def find(self, nums: list[int], start: int, end:int, key):
        half = ( start + end )//2
        if start < end: 
            if key > nums[half]:
                return self.find(nums, half+1, end, key)
            elif key < nums[half]:
                return self.find(nums, start, half, key)
            else: 
                return half
        elif start == end:
            if nums[start] == key:
                return start
        return -1
        
        
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        i = 0
        half = len(nums) // 2
        while len(nums) > 1 and i <= half:
            index = self.find(nums, 1, len(nums)-1, k-nums[0])
            if index != -1:
                nums.pop(index)
                count += 1
            
            if nums[0] >= k//2 + 1:
                break
            nums.pop(0)
            i += 1
                        
        return count