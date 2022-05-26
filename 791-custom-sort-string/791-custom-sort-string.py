class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderDict={}
        for i in range(len(order)):
            orderDict[order[i]] = i
            
        strArr = []
        for char in s:
            strArr.append(char)
        strArr.sort(key=lambda x: orderDict.get(x, -1))
        
        sortedString = ""
        for char in strArr:
            sortedString += char
        
        return sortedString