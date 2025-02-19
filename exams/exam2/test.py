def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-'*5)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_move():
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter integers.")

def main():
    board = initialize_board()
    players = ['X', 'O']
    turn = 0

    while True:
        display_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        row, col = get_move()

        if board[row][col] == ' ':
            board[row][col] = player
            if check_win(board, player):
                display_board(board)
                print(f"Player {player} wins!")
                break
            elif is_board_full(board):
                display_board(board)
                print("It's a tie!")
                break
            turn += 1
        else:
            print("That position is already taken. Try again.")

if __name__ == "__main__":
    main()