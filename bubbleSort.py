def countSwaps(a):
    # Write your code here
    n = len(a)
    isSwapped = False
    swaps = 0
    for i in range(n-1, -1, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                isSwapped = True
                swaps += 1
        if not isSwapped:
            break
    print("Array is sorted in " + str(swaps)+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[n-1]))
