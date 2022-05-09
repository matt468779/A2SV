class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [len(temperatures)-1]
        answer = [0]
        for i in range(len(temperatures)-2, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack == []:
                answer.append(0)
                stack.append(i)
            else:
                answer.append(stack[-1])
                stack.append(i)

        ans = []
        for i in range(len(temperatures)):
            popped = answer.pop()
            ans.append(0 if popped == 0 else popped - i)

        return ans