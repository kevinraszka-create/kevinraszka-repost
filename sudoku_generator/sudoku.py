import random

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    solve(board)
    return board

def remove_cells(board, num_remove):
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    for i in range(num_remove):
        row, col = positions[i]
        board[row][col] = 0

def create_puzzle(num_remove=40):
    puzzle = generate_sudoku()
    remove_cells(puzzle, num_remove)
    return puzzle

if __name__ == "__main__":
    puzzle = create_puzzle(40)
    for row in puzzle:
        print(row)

        