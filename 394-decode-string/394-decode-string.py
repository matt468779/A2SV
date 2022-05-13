class Solution:
    def decodeString(self, s: str) -> str:
        brackets = []
        times = ""
        word = ""
        encoded = ""
        for char in s: 
            if char == '[':
                brackets.append('[')
            elif char == ']':
                brackets.pop()
            elif char.isdecimal() and brackets == []:
                times += char
            elif brackets == [] and times == "":
                word += char
            if brackets != []:
                encoded += char
            if brackets == [] and times != "" and encoded != "":
                encoded = encoded.replace('[', '', 1)
                for _ in range(int(times)):
                    word += self.decodeString(encoded)
                encoded = ""
                times = ""
        return word