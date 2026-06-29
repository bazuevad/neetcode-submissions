from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val==".":
                    continue
                if val in cols[col]:
                    return False
                if val in rows[row]:
                    return False
                box = (row//3)*3 + (col//3)
                if val in boxes[box]:
                    return False
                cols[col].add(val)
                rows[row].add(val)
                boxes[box].add(val)
        return True