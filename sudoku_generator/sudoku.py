import random
import tkinter as tk
from tkinter import ttk

# Difficulty map: how many cells to remove for each level
difficulty_map = {
    "Easy": 35,
    "Medium": 45,
    "Hard": 55,
}

# Check whether placing num in the given row/col is valid
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

# Backtracking solver to fill the board with a complete solution
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

# Generate a fully solved Sudoku board
def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    solve(board)
    return board

# Remove a number of cells from the solved board to make a puzzle
def remove_cells(board, num_remove):
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    for i in range(num_remove):
        row, col = positions[i]
        board[row][col] = 0

# Create a Sudoku puzzle with a given difficulty level
def create_puzzle(num_remove=40):
    puzzle = generate_sudoku()
    remove_cells(puzzle, num_remove)
    return puzzle

# Convert the board to text lines for display
def board_to_text(board):
    lines = []
    for row in board:
        lines.append(" ".join(str(num) if num != 0 else "." for num in row))
    return "\n".join(lines)

# Main GUI application
def main():
    root = tk.Tk()
    root.title("Sudoku Generator")
    root.geometry("320x380")

    difficulty_var = tk.StringVar(value="Medium")

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill="both", expand=True)

    label = ttk.Label(frame, text="Choose difficulty:")
    label.pack(anchor="w")

    difficulty_menu = ttk.Combobox(
        frame,
        textvariable=difficulty_var,
        values=list(difficulty_map.keys()),
        state="readonly",
    )
    difficulty_menu.pack(fill="x", pady=5)

    result_text = tk.Text(frame, width=25, height=13, font=("Consolas", 12))
    result_text.pack(fill="both", expand=True, pady=10)
    result_text.configure(state="disabled")

    def generate_and_display():
        level = difficulty_var.get()
        num_remove = difficulty_map.get(level, 45)
        puzzle = create_puzzle(num_remove)
        result_text.configure(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, board_to_text(puzzle))
        result_text.configure(state="disabled")

    generate_button = ttk.Button(frame, text="Generate Puzzle", command=generate_and_display)
    generate_button.pack()

    generate_and_display()
    root.mainloop()

if __name__ == "__main__":
    main()

        