class Solution: 
    def select(self, arr, i):
        # code here
        selected = i
        for j in range(i+1, len(arr)):
            if arr[selected] > arr[j]:
                selected = j
        return selected
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            selected = self.select(arr, i)
            arr[i], arr[selected] = arr[selected], arr[i]
    
if __name__ == "__main__":
    arr = [5,4,3,2,1]
    sol = Solution()

    sol.selectionSort(arr, 5)
    print(arr)