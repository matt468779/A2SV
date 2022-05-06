class Solution:
    def top(self, arr: List):
        if len(arr) > 0:
            return arr[len(arr)-1]
        return None
    def isValid(self, s: str) -> bool:
        stack = []
        for par in s:
            print (par)
            if par == '(' or par == '{' or par == '[':
                stack.append(par)
            elif (self.top(stack) == '{' and par == '}') or (self.top(stack) == '[' and par == ']') or (self.top(stack) == '(' and par == ')'):
                stack.pop()
            else:
                return False
        if len(stack):
            return False
        return True