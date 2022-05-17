from math import ceil

def codeFor1(n):
    if n == 1:
        return [1]  
    elif n == 0:
        return [0]
    return codeFor1(n//2) + [n%2]

def numOfOne(arr, l, r):
    if len(arr) == 1 and l == 1 and r == 1:
        return arr[0]
    l -= 1
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        a0 = pow(2, i) - 1
        if a0 >= r:
            break
        d = pow(2, i+1)
        j = 0 if l <= a0 else ceil((l-a0)/d)
        k = ceil((r-a0)/d)

        count += k - j 
    
    return count

inp = input().split(" ")
n = int(inp[0])
l = int(inp[1])
r = int(inp[2])

print(numOfOne(codeFor1(n), l, r))
