class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answ = []

        def backtrack(curr,open,close,n):
            if len(curr)==n*2:
                answ.append(curr)
                return
            if open<n:
                backtrack(curr+"(",open+1,close,n)
            if close <open:
                backtrack(curr+")",open,close+1,n)
            return
        backtrack("",0,0,n)
        return answ