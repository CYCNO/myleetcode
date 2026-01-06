class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. check for all row
        for i in range(9):
            temp = []
            for j in range(9):
                elem = board[i][j]
                if elem == ".":
                    pass
                elif elem not in temp:
                    temp.append(elem)
                elif elem in temp:
                    return False
        
        # 2. check for all column
        for i in range(9):
            temp = []
            for j in range(9):
                elem = board[j][i]
                if elem == ".":
                    pass
                elif elem not in temp:
                    temp.append(elem)
                elif elem in temp:
                    return False
        # check all 3x3 subgrids
        for i in range(9):
            temp = []
            sr = (i // 3) * 3
            sc = (i % 3) * 3

            for j in range(3):
                for k in range(3):
                    elem = board[sr + j][sc + k]
                    if elem == ".":
                        continue
                    if elem in temp:
                        return False
                    temp.append(elem)

        return True
