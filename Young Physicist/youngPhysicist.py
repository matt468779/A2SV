n = int(input())
vectorSum = [0, 0, 0]
 
for _ in range(n):
   vector = list(map(int, input().split()))
 
   for i in range(len(vector)):
      vectorSum[i] += vector[i]
 
if vectorSum == [0, 0, 0]:
   print('YES')
else:
   print('NO')
