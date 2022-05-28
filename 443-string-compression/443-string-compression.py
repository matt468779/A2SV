class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append('')
        same = chars[0]
        count = 0
        i = 0
        l = len(chars)
        while i < l:
            if chars[0] == same:
                count += 1
            else:
                chars.append(same)
                if count > 1:
                    for n in str(count):
                        chars.append(n)
                count = 1
                same = chars[0]
            chars.pop(0)
            i+=1
        return len(chars)
                