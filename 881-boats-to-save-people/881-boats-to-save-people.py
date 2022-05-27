class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        begin = 0
        end = len(people) - 1
        result = 0
        while begin < end:
            if people[begin] + people[end] <= limit:
                begin += 1
            end -= 1    
            result += 1
            
        if begin == end:
            result += 1
        return result