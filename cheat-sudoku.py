def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, row, col):
    # Cek baris
    for j in range(len(board[0])):
        if board[row][j] == num:
            return False

    # Cek kolom
    for i in range(len(board)):
        if board[i][col] == num:
            return False

    # Cek kotak 3x3
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def main():
    # 0 berarti kosong
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Papan Sudoku Awal:")
    print_board(board)

    if solve_sudoku(board):
        print("\nPapan Sudoku Setelah Diisi:")
        print_board(board)
    else:
        print("Tidak ada solusi yang ditemukan.")

if __name__ == "__main__":
    main()