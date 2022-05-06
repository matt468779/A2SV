class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        frequency = [1]
        j = 0
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                frequency[j] += 1
            else:
                frequency.append(1)
                j+=1
        frequency.sort(reverse=True)

        j = 0
        half = len(arr) // 2
        count = 0
        while count < half:
            count += frequency[j]    
            j += 1
        return j