class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answ = [0]* len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                temp, index = stack.pop()
                answ[index] = i - index
            stack.append((t,i))
        return answ