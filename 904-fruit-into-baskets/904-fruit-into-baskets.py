class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit1 = fruits[0]
        fruit2 = -1
        count1 = 1
        count2 = 0
        tempCount1 = 1
        tempCount2 = 0
        res = 0
        i = 1
        while i < len(fruits):                  
            if fruit1 == fruits[i]:
                count1 += 1
                if fruits[i-1] == fruits[i]:
                    tempCount1 += 1
                else:
                    tempCount1 = 1
            elif fruit2 == fruits[i]:
                count2 += 1
                if fruits[i-1] == fruits[i]:
                    tempCount2 += 1
                else:
                    tempCount2 = 1
            elif fruit2 == -1:
                fruit2 = fruits[i]
                count2 = 1
                tempCount2 = 1
            else:
                res = max(res, count1+count2)
                if fruits[i-1] == fruit2:
                    fruit1 = fruit2
                    count1 = tempCount2
                    tempCount1 = tempCount2
                else:
                    count1 = tempCount1
                tempCount2 = 1
                fruit2 = fruits[i]
                count2 = 1
                
            i += 1
        res = max(res, count1+count2)
                
        return res