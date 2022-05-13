class Solution:
    digits = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    tens = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    values = ['', 'Thousand', 'Million', 'Billion',]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        numString = str(num)
        
        if len(numString) % 3 == 2:
            numString = '0' + numString
        elif len(numString) % 3 == 1:
            numString = '00' + numString

        word = ''
        value = len(numString) // 3 - 1
        for i in range(0, len(numString)-2, 3):
            word += self.hundreds(numString[i: i+3])
            if numString[i] != '0' or numString[i+1] != '0' or numString[i+2] != '0':
                if value > 0:
                    word += self.values[value] + ' '
            value -= 1

        if word[-1] == " ":
            word = word[:len(word)-1]
        return word

    def hundreds(self, num: str):
        word = ''
        if num[0] != '0':
            word += self.digits[int(num[0])] + " " + "Hundred" + " "
        if num[1] > '1':
            word += self.tens[int(num[1])-1] + " "
        elif num[1] == '1':
            word += self.teens[int(num[2])] + " "
        if num[2] != '0' and num[1] != '1':
            word += self.digits[int(num[2])] + " "

        return word