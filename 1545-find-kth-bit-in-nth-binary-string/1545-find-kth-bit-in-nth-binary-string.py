class Solution:
    def invertReverse(self, a: str) -> str:
        b = ""
        for i in range(len(a)-1, -1, -1):
            if a[i] == "0":
                b += "1"
            else:
                b += "0"
        return b

    def findKthBit(self, n: int, k: int) -> str:
        bits = ["0"]*n
        temp = ""
        level = 2

        for i in range(1, n):
            bits[i] = bits[i-1] + "1" + self.invertReverse(bits[i-1])
        
        return bits[n-1][k-1]