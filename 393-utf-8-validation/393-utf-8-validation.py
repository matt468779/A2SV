class Solution:
    def validUtf8(self, data: List[int]) -> bool:        
        i = 0
        while i < len(data):
            ones = 0
            bi = format(data[i], '08b')
            while ones < len(bi)-1 and bi[ones] == '1':
                ones += 1

            if bi[ones] == '1' or ones == 1 or i+ones > len(data) or ones > 4:
                return False
            
            j = i
            for j in range(i+1, i+ones):
                if format(data[j], '08b')[:2] != '10':
                    return False
            i = j+1
        return True
                