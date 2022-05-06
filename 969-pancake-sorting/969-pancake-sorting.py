class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        length = len(arr)
        for i in range(len(arr), 0, -1):
            
            if arr[0] == length-i+1 and arr[0] != length:
                arr[:i] = reversed(arr[:i])
                flips.append(i)
            elif arr[i-1] != length-i+1:
                min = arr[0]
                minIndex = 0
                for j in range(1, i):
                    if arr[j] < min:
                        min = arr[j]
                        minIndex = j

                flips.append(minIndex+1)
                flips.append(i)

                arr[:minIndex+1] = reversed(arr[0:minIndex+1])
                arr[:i] = reversed(arr[:i])
            
        flips.append(length)
        return flips