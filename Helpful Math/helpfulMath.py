nums = input().split('+')
 
count1, count2, count3 = 0, 0, 0
 
for num in nums:
   if num == '1':
      count1 += 1
   elif num == '2':
      count2 += 1
   else:
      count3 += 1
 
print('+'.join(['1']*count1 + ['2']*count2 + ['3']*count3))
