class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def operate(x, y, op):
            if op == '+':
                return x+y
            elif op == '-':
                return x-y
            elif op == '*':
                return x*y
            
        exp = []
        ops = set('+-*')
        temp = ''
        for char in expression:
            if char not in ops:
                temp += char
            else:
                exp.append(int(temp))
                exp.append(char)
                temp = ''
        exp.append(int(temp)) 
        
        memo = [['x']*len(exp) for _ in range(len(exp))]       
        def solve(l, r):
            if memo[l][r] != 'x':
                return memo[l][r]
            if l == r:
                return [exp[l]]
            
            res = []
            for i in range(l+1, r+1, 2):
                left = solve(l, i-1)
                right = solve(i+1, r)
                for j in left:
                    for k in right:
                        res.append(operate(j, k, exp[i]))
                    
            memo[i] = res
            return res
        
        return solve(0, len(exp)-1)
                
                
                
                
                
                
                
                
                
                
                
                