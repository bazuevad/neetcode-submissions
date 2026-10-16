class Solution:
    def backtrack(self,n,row,cols,d,ad,board,answer):
        if row==n:
            answer.append(board[:])
            return
        for col in range(n):
            diagonal = row+col
            anti = row-col
            if col in cols or diagonal in d or anti in ad:
                continue
            cols.add(col)
            d.append(diagonal)
            ad.append(anti)
            r = "."*col+"Q"+"."*(n-col-1)
            board.append(r)
            self.backtrack(n,row+1,cols,d,ad,board,answer)
            cols.remove(col)
            d.pop()
            ad.pop()
            board.pop()
        return

            
    def solveNQueens(self, n: int) -> List[List[str]]:
        answ = []
        cols = set()
        self.backtrack(n,0,cols,[],[],[],answ)
        return answ
        