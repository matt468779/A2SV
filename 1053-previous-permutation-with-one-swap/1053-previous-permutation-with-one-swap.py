class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1, -1, -1):
            minIdx = i
            minVal = float('-inf')
            for j in range(i+1, len(arr)):
                if arr[j] < arr[i] and arr[j] > minVal:
                    minIdx = j
                    minVal = arr[j]

            if minVal != float('-inf'):
                arr[minIdx], arr[i] = arr[i], arr[minIdx]
                break

        return arr