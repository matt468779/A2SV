n = int(input())
for _ in range(n):
    l = int(input())
    powerUps = list(map(int, input().split()))
    powerUps.sort()
    distinct = 1
    for i in range(1, len(powerUps)):
        if powerUps[i] != powerUps[i-1]:
            distinct += 1

    distinct = str(distinct)
    for i in range(int(distinct)):
        print(distinct, end=" ")
    for i in range(int(distinct)+1, l+1):
        print(str(i), end=" ")
