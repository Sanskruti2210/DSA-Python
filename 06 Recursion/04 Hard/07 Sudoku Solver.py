'''
Create a program that fills in the blank cells in a Sudoku puzzle to solve it.
Every sudoku solution needs to follow to these guidelines:
1) In every row, the numbers 1 through 9 must appear exactly once.
2) In every column, the numbers 1 through 9 must appear exactly once.
3) In each of the grid's nine 3x3 sub-boxes, the numbers 1 through 9 must appear exactly once.
Empty cells are indicated by the '.' character.
'''

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]


def solve_sudoku(board):

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Store numbers that are already present
    for r in range(9):
        for c in range(9):

            if board[r][c] != ".":

                num = board[r][c]

                rows[r].add(num)
                cols[c].add(num)

                box = (r // 3) * 3 + (c // 3)
                boxes[box].add(num)

    def solve():

        best_row = -1
        best_col = -1
        best_candidates = None

        # Find the empty cell with minimum candidates
        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":

                    box = (r // 3) * 3 + (c // 3)

                    candidates = []

                    for num in "123456789":

                        if (num not in rows[r] and
                            num not in cols[c] and
                            num not in boxes[box]):

                            candidates.append(num)

                    # No number can be placed here
                    if len(candidates) == 0:
                        return False

                    # Keep the cell with minimum choices
                    if (best_candidates is None or
                            len(candidates) < len(best_candidates)):

                        best_candidates = candidates
                        best_row = r
                        best_col = c

                        # Only one choice, can't do better
                        if len(candidates) == 1:
                            break

            if best_candidates is not None and len(best_candidates) == 1:
                break

        # No empty cells → Sudoku solved
        if best_candidates is None:
            return True

        r = best_row
        c = best_col

        box = (r // 3) * 3 + (c // 3)

        # Try every possible number
        for num in best_candidates:

            # Pick
            board[r][c] = num

            rows[r].add(num)
            cols[c].add(num)
            boxes[box].add(num)

            # Explore
            if solve():
                return True

            # Backtrack
            board[r][c] = "."

            rows[r].remove(num)
            cols[c].remove(num)
            boxes[box].remove(num)

        return False

    solve()


solve_sudoku(board)


# Print solved Sudoku
for row in board:
    print(" ".join(row))