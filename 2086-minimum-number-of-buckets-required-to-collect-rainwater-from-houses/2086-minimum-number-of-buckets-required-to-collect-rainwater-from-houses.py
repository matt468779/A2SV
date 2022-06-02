class Solution:
    def minimumBuckets(self, street: str) -> int:
        street = list(street)
        count = 0
        stop = 0
        if len(street) == 1 and street[0] == 'H':
            return -1 
        elif (street[0] == 'H' and street[1] == 'H') or (street[-1] == 'H' and street[-2] == 'H'):
            return -1
        elif street[0] == 'H':
            stop = 1
            street[1] = 'B'
            count = 1
            
        for i in range(1,len(street)-1):
            if street[i] == 'H':
                if street[i-1] == 'H' and street[i+1] == 'H':
                    return -1
                elif street[i-1] != 'B' and street[i+1] != 'H':
                    count += 1
                    street[i+1] = 'B'
                elif street[i-1] != 'B' and street[i+1] == 'H':
                    count += 1
            else:
                stop = 0
        if street[-1] == 'H' and street[-2] != 'B':
            count += 1
            
        return count
                
                