# Function to initialize the board
def initialize_board(size):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board

# Function to display the board
def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('--' * len(row))

# Function to check if a move is valid
def is_valid_move(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board):
        if board[row][col] == ' ':
            return True
    return False

# Function to make a move
def make_move(board, row, col, symbol):
    board[row][col] = symbol

# Function to check if there is a winner
def check_winner(board, symbol):
    size = len(board)
    # Check rows, columns, and diagonals
    for i in range(size):
        if all([board[i][j] == symbol for j in range(size)]) or all([board[j][i] == symbol for j in range(size)]):
            return True
    if all([board[i][i] == symbol for i in range(size)]) or all([board[i][size - 1 - i] == symbol for i in range(size)]):
        return True
    return False

# Function to check if the board is full (a draw)
def is_draw(board):
    return all([cell != ' ' for row in board for cell in row])

# Function to get user input for a move
def get_player_move(board, symbol):
    while True:
        try:
            move = input(f"Player {symbol}, enter your move (row and column): ").strip().upper()
            row, col = int(move[0]) - 1, ord(move[1]) - ord('A')
            if is_valid_move(board, row, col):
                return row, col
            else:
                print("Invalid move. Please try again.")
        except (IndexError, ValueError):
            print("Invalid input format. Please enter a valid move.")

# Function to update the scores based on the winner
def update_scores(scores, winner):
    if winner == 'X':
        scores['X'] += 1
    elif winner == 'O':
        scores['O'] += 1

# Function to save the current game state to a file
def save_game(board, move_history, current_symbol):
    with open('tic_tac_toe_save.txt', 'w') as file:
        for move in move_history:
            file.write(f"{move[0]} {move[1]} {move[2]}\n")  # Write moves
        file.write(f"{current_symbol}\n")  # Write current player symbol
        for row in board:
            file.write(' '.join(row) + '\n')  # Write board state

# Function to load a saved game state from a file
def load_game():
    with open('tic_tac_toe_save.txt', 'r') as file:
        move_history = []
        for _ in range(3):  # Assuming 3 moves (row, col, player) are stored per line
            move = tuple(map(int, file.readline().strip().split()))
            move_history.append(move)
        current_symbol = file.readline().strip()
        board = [list(file.readline().strip()) for _ in range(len(move_history) + 1)]  # Board size inferred from moves
    return board, move_history, current_symbol

# Main game loop
def main():
    board_size = 3
    board = initialize_board(board_size)
    current_symbol = 'X'
    scores = {'X': 0, 'O': 0}
    move_history = []

    while True:
        display_board(board)
        row, col = get_player_move(board, current_symbol)
        make_move(board, row, col, current_symbol)
        move_history.append((row, col, current_symbol))

        if check_winner(board, current_symbol):
            display_board(board)
            print(f"Player {current_symbol} wins!")
            update_scores(scores, current_symbol)
            break
        elif is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        current_symbol = 'O' if current_symbol == 'X' else 'X'

    # Save the game state
    save_game(board, move_history, current_symbol)
    print(f"Scores: Player X - {scores['X']} | Player O - {scores['O']}")

if __name__ == "__main__":
    main()
