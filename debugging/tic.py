#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    """Kthen 'X' ose 'O' nëse ka fitues, përndryshe None."""
    # Rreshta
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return row[0]
    # Kolona
    for c in range(3):
        if board[0][c] != " " and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # Diagonalet
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def ask_coordinate(prompt):
    """Lexon një numër 0–2 nga përdoruesi, me validim dhe rikërkim."""
    while True:
        try:
            val = int(input(prompt))
            if val in (0, 1, 2):
                return val
            print("Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # kontrollo nëse ka fitues ose barazim përpara inputit (për siguri)
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        if board_full(board):
            print("It's a draw!")
            break

        # leximi i koordinatave me validim
        row = ask_coordinate(f"Enter row (0, 1, or 2) for player {player}: ")
        col = ask_coordinate(f"Enter column (0, 1, or 2) for player {player}: ")

        # kontrollo nëse vendi është i lirë
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # bëj lëvizjen
        board[row][col] = player

        # kontrollo pas lëvizjes
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # ndërro lojtarin
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
