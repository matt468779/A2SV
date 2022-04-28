def insertionSort1(n, arr):
    # Write your code here
    temp = arr[n-1]
    i = n - 2
    while temp < arr[i] and i >= 0:
        arr[i+1] = arr[i]
        i -= 1
        printArray(arr)
    arr[i+1] = temp
    printArray(arr)


def printArray(arr):
    arrayStr = str(arr[0])
    for i in range(1, len(arr)):
        arrayStr += " " + str(arr[i])
    print(arrayStr)


if __name__ == "__main__":
    a = [2, 4,6,8,0]
    insertionSort1(5, a)

