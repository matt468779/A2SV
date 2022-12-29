def solve():
    n = int(input())
    res = 0
    for i in range(n):
        inp = input()
        res += '+' in inp
        res -= '-' in inp
    print(res)
    
solve()
