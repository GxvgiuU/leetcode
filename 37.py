class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        # straight forward backtracking, however much slower than the method below, 1112ms
        from collections import defaultdict
        candidates = "123456789"
        def valid2(board, i, j, g):
            if g in board[i].values():
                return False
            if any(g == b[j] for b in board.values()):
                return False
            row, column = int(i / 3) * 3, int(j / 3) * 3
            if any(g == board[r][c] for r in range(row, row + 3) for c in range(column, column + 3)):
                return False
            return True

        def solve2(board, count):
#             myprint(board)
#             print ""
            if count == 81:
                return True
            i, j = count / 9, count % 9
            if board[i][j] != ".":
                return solve2(board, count + 1)
            for g in candidates:
                if valid2(board, i, j, g):
                    board[i][j] = g
                    if solve2(board, count + 1):
                        return True
                    else:
                        board[i][j] = "."
            return False

        def mysplit2(board):
            s = defaultdict(lambda: defaultdict())
            for i in range(9):
                for j in range(9):
                    s[i][j] = board[i][j]
            return s

        re = mysplit2(board)
        solve2(re, 0)
        for i in range(9):
            board[i] = "".join(re[i][j] for j in range(9))
        return


        # not really straight forward, using a lot of tricks like human thinking, 116ms
        from collections import defaultdict
        from copy import deepcopy
        candidates = "123456789"

        def valid(board, i, j, g):
            if g in board[i].values():
                return False
            if any(g == b[j] for b in board.values()):
                return False
            row, column = int(i/3)*3, int(j/3)*3
            if any(g == board[r][c] for r in range(row, row+3) for c in range(column, column+3)):
                return False
            return True

        def mysplit(board):
            s = defaultdict(lambda: defaultdict())
            for i in range(9):
                for j in range(9):
                    s[i][j] = board[i][j]
            return s

        def solve(board):
            if any("." in b.values() for b in board.values()):
                p = defaultdict(list)
                infer = []
                for i in range(9):
                    for j in range(9):
                        if board[i][j] == ".":
                            for g in candidates:
                                if valid(board, i, j, g):
                                    p[(i, j)].append(g)
                            guess_len = len(p[(i, j)])
                            if not guess_len:  # guess wrong, no valid solution
                                return
                            elif guess_len == 1:
                                infer.append([i, j, p[(i, j)][0]])

                board = _solve(board, p, infer)
            return board

        def _priority(p):
            m = 9
            priority = []
            for i in range(9):
                for j in range(9):
                    n = len(p[(i, j)])
                    if n == 2:
                        return [n, i, j, p[(i, j)]]
                    elif n < m:
                        m = n
                        priority = [n, i, j, p[(i, j)]]
            return priority

        def _check(board, p, infer, i, j, g):
            p[(i, j)].remove(g)
            for x in range(9):
                if g in p[(i, x)]:
                    p[(i, x)].remove(g)
                    guess_len = len(p[(i, x)])
                    if guess_len == 1:
                        infer.append([i, x, p[(i, x)][0]])
                if g in p[(x, j)]:
                    p[(x, j)].remove(g)
                    guess_len = len(p[(x, j)])
                    if guess_len == 1:
                        infer.append([x, j, p[(x, j)][0]])
            row, column = int(i / 3) * 3, int(j / 3) * 3
            for r in range(row, row + 3):
                for c in range(column, column + 3):
                    if g in p[(r, c)]:
                        p[(r, c)].remove(g)
                        guess_len = len(p[(r, c)])
                        if guess_len == 1:
                            infer.append([r, c, p[(r, c)][0]])

        def _solve(board, p, infer):
            while infer:
                m = infer.pop()
                if not valid(board, m[0], m[1], m[2]):
#                     print "strange"
                    return
                board[m[0]][m[1]] = m[2]
                _check(board, p, infer, m[0], m[1], m[2])

            while any("." in b.values() for b in board.values()):
                priority = _priority(p)
                for c in priority[3]:
                    if not valid(board, priority[1], priority[2], c):
#                         print "strange"
                        continue
                    board[priority[1]][priority[2]] = c
                    board2, p2 = deepcopy(board), deepcopy(p)
                    infer2 = []
                    _check(board2, p2, infer2, priority[1], priority[2], c)

                    board2 = _solve(board2, p2, infer2)
                    if board2:
                        return board2
                return

            return board

        re = solve(mysplit(board))
        for i in range(9):
            board[i] = "".join(re[i][j] for j in range(9))
        return


def myprint(board):
    for i in range(9):
        for j in range(9):
            print board[i][j],
        print ""


s = Solution()
print "Q:"
board = ["...2...63", "3....54.1", "..1..398.", ".......9.", "...538...", ".3.......", ".263..5..", "5.37....8", "47...1..."]
myprint(board)
print "A:"
s.solveSudoku(board)
myprint(board)
print ""

print "Q:"
board = ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6", "...2759.."]
myprint(board)
print "A:"
s.solveSudoku(board)
myprint(board)
print ""

print "Q:"
board = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
myprint(board)
print "A:"
s.solveSudoku(board)
myprint(board)
print ""

print "Q:"
board = ["..6..3.4.", "915..2863", "3..9.1...", ".83.....2", ".7.1.4.8.", "2.....91.", "...2.6..8", "5928..631", ".6.3..5.."]
myprint(board)
print "A:"
s.solveSudoku(board)
myprint(board)
print ""
