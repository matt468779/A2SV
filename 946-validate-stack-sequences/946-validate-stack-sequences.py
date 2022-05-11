class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop = 0
        push = 0
        answer = True
        while pop < len(popped) or push < len(pushed):
            if pushed[push] != popped[pop]:
                push += 1
            else:
                pushed.pop(push)
                pop += 1
                if push > 0:
                    push -= 1

            if push >= len(pushed) and pop < len(popped):
                return False
            
        return answer