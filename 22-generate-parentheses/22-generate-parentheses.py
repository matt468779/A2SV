class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.combinations = []
        def formParenthesis(opened, closed, parenthesis):
            if opened > 0 and opened < closed:
                formParenthesis(opened-1, closed, parenthesis+"(")
                formParenthesis(opened, closed-1, parenthesis+")")
            elif opened > 0 and opened == closed:
                formParenthesis(opened-1, closed, parenthesis+"(")
            elif opened < 1 and closed > 0:
                formParenthesis(opened, closed-1, parenthesis+")")
            else:
                self.combinations.append(parenthesis)
                
        formParenthesis(n-1, n, "(")
        return self.combinations