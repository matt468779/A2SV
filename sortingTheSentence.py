class Solution:
    def sortSentence(self, s: str) -> str:

        sentenceWords = s.split(" ")
        result = [""] * (len(sentenceWords)+1)

        for word in sentenceWords:
            index = word[len(word)-1]
            result[int(index)] =word.removesuffix(index)
        return self.toString(result)
    
    def toString(self, arr) -> str:
        sentence = arr[1]
        for i in range(2, len(arr)):
            sentence += " " + arr[i]
        return sentence