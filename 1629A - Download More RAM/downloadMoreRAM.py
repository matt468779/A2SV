n = int(input())
for _ in range(n):
    nk = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(nk[0]):
        a[i] = (a[i], b[i])
    a.sort()
    
    ram = nk[1]
    i = 0
    while i < nk[0] and ram >= a[i][0]:
        ram += a[i][1]
        i += 1

    print(ram)
