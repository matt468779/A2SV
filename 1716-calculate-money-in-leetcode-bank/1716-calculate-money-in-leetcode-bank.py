class Solution:
    def totalMoney(self, n: int) -> int:
        remaining_days = n%7
        weeks = n//7
        firstWeekTotal = ((1+7) * 7) // 2
        
        last_remaining = ((weeks+1 + weeks+remaining_days) * remaining_days) // 2
        
        first_weeks = (firstWeekTotal * weeks) + (((weeks-1)*7)*(weeks))//2
        
        return first_weeks + last_remaining