t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    blueSum, redSum = a[0], 0
    blue, red = 1, n-1
    res = False

    while blue < red:
        blueSum += a[blue]
        redSum += a[red]
        if redSum > blueSum:
            res = True
            break
        blue += 1
        red -= 1
    if res:
        print('YES')
    else:
        print('NO')
