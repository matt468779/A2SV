class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        while i < n:
            largest = i
            if 2*i+1 < n and arr[2*i+1] > arr[i]:
                largest = 2*i+1
            if 2*i+2 < n and arr[2*i+2] > arr[largest]:
                largest = 2*i+2
            if largest != i:
                arr[largest], arr[i] = arr[i], arr[largest]
                i = largest
            else:
                break
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n//2-1, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        for i in range(n):
            self.heapify(arr, n-i, 0)
            arr[0], arr[n-i-1] = arr[n-i-1], arr[0]
