class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        l, r = 0, 1
        curr_line_len = len(words[0])
        while r < len(words):
            if curr_line_len + len(words[r]) + r - l <= maxWidth:
                curr_line_len += len(words[r])
            else:
                spaces = maxWidth - curr_line_len
                if r-l-1 == 0:
                    res.append(words[l] + ' '*(maxWidth-len(words[l])))
                else:
                    extra_spaces = spaces // (r-l-1)
                    remainder_spaces = spaces % (r-l-1)
                    temp = []
                    space = ' ' * extra_spaces
                    for i in range(l, r-1):
                        temp.append(words[i])
                        temp.append(space)
                        if remainder_spaces:
                            temp.append(' ')
                            remainder_spaces -= 1

                    temp.append(words[r-1])
                    res.append(''.join(temp))
                    
                curr_line_len = len(words[r])
                l = r
                
            r += 1
        
        temp = []
        for i in range(l, r-1):
            temp.append(words[i])
            temp.append(' ')
            
        temp.append(words[-1] + ' '*(maxWidth - curr_line_len - (r - l - 1)))
        res.append(''.join(temp))
        
        return res