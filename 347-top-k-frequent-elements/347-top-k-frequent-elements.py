class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        frequency = [[1, nums[0]]]
        j = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                frequency[j][0] += 1
            else:
                frequency.append([1, nums[i+1]])
                j += 1
        
        frequency.sort(reverse=True)
        answer = []
        for i in range(k):
            answer.append(frequency[i][1])

        return answer