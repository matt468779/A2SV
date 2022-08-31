class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        for i in range(num//1000):
            res += 'M'
        num %= 1000
        
        hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        
        res += hundreds[num//100]
        num %= 100
        res += tens[num//10]
        num %= 10
        res += ones[num]
        
        return res