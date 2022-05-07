class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        temp = []

        for char in s:
            if char != ')':
                stack.append(char)
            else:
                poped = stack.pop()
                while poped != '(':
                    temp.append(poped)
                    poped = stack.pop()

                temp.reverse()
                while temp != []:
                    stack.append(temp.pop())
        result = ""
        for char in stack:
            result += char
        return result