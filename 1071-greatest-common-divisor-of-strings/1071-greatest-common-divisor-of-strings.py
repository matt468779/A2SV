class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        print(str1[:100])
        if len(str1) > len(str2):
            long = str1
            short = str2
        elif len(str1) < len(str2):
            long = str2
            short = str1
        else:
            return str1 if str1 == str2 else ''
        
        for i in range(0, len(long)-len(short)+1, len(short)):
            if long[i:i+len(short)] != short:
                return ''
        if len(long[i+len(short):]) == 0:
            return short
        
        return self.gcdOfStrings(short, long[i+len(short):])
        
        
        
        
        