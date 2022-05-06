class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens.reverse()
        stack = [tokens.pop()]
        while True:
            if stack[-1] == "+":
                stack.pop()
                stack.append(int(stack.pop()) + int(stack.pop()))
                if len(tokens) == 0:
                    break
            elif stack[-1] == "-":
                stack.pop()
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
                if len(tokens) == 0:
                    break
            elif stack[-1] == "*":
                stack.pop()
                stack.append(int(stack.pop()) * int(stack.pop()))
                if len(tokens) == 0:
                    break
            elif stack[-1] == "/":
                stack.pop()
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a / b)
                if len(tokens) == 0:
                    break
            elif tokens != []:
                stack.append(tokens.pop())
            else:
                break

        return int(stack[0])