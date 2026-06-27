import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        actions = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),  # truncate toward zero
        }
        stack = []
        for t in tokens:
            if t in actions:
                if stack:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(actions[t](a,b))
            else:
                stack.append(int(t))
        return stack[0]