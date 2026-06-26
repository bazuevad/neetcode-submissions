class MinStack:

    def __init__(self):
        self.min_stack = []
    
    def push(self, val: int) -> None:
        curr_min = min(self.min_stack[-1][0] if self.min_stack else val,val)
        self.min_stack.append((curr_min,val))

    def pop(self) -> None:
        self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1][1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]
