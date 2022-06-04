class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue = [len(nums)-1]
        for i in range(len(nums)-2, -1, -1): 
            if queue[0] <= i+k:
                nums[i] = nums[i] + nums[queue[0]]
            else:
                queue.pop(0)
                nums[i] = nums[i] + nums[queue[0]]

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

        return nums[0]