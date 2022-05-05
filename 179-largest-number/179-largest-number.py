class Solution:
    maxDigit = 0
    def toInt(self, number: List[int]) -> int:
        num = str(number[0])
        length = len(number)
        count = 0        

        for i in range(1, self.maxDigit):
            if i < length and (number[i] > number[0] or number[i] == max(number))  and number[0] !=9 :
                count += 1
            num += str(number[i%length])
        
        for _ in range(self.maxDigit, 10 + count):
            num += "9"

        return int(num)

    def equalDigit(self, nums: List[int]) -> int:
        num = ""
        for i in range(self.maxDigit):
            if i < len(nums):
                num += str(nums[i])
            else:
                num+=str(nums[i%len(nums)])
        return int(num)

    def split(self, num: int) -> List[int]:
        nums = []
        for i in str(num):
            nums.append(int(i))

        return nums

    def largestNumber(self, nums: List[int]) -> str:
        self.maxDigit = len(str(max(nums)))

        for i in range(len(nums)):
            nums[i] = self.split(nums[i])

        nums.sort(key = lambda x: (-x[0], -self.equalDigit(x), -self.toInt(x), len(x)))

        strNums = ""
        start = True
        for num in nums:
            for nu in num:
                if start == True and nu == 0:
                    continue
                else:
                    start = False
                strNums += str(nu)
        if strNums == "":
            strNums = "0"
        return strNums