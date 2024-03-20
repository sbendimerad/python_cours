from random import choice

def display_board(board):
    # Displays the current state of the board
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board,free_fields):
    # Allows the player to enter their move, checks for validity, and updates the board
    move = int(input("Enter your move (1-9): "))
    row = (move - 1) // 3
    col = (move - 1) % 3
    while (row, col) not in free_fields:
        print("Invalid move. The position is either occupied or out of range.")
        move = int(input("Enter your move (1-9): "))
        row = (move - 1) // 3
        col = (move - 1) % 3
    board[row][col] = 'O'
    return board

def make_list_of_free_fields(board):
    # Returns a list of all unoccupied positions on the board
    free_fields = []
    for row in range(3):
        for col in range(3):
            if isinstance(board[row][col], int):
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # Checks if there's a winning condition on the board for the given sign ('X' or 'O')
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[row][col] == sign for row, col in condition):
            return True
    return False

def draw_move(board, free_fields):
    # Computer randomly selects a move from the available free fields and updates the board
    if not free_fields:
        return board
    row, col = choice(free_fields)
    board[row][col] = 'X'
    return board

def main():
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]  # Initial board setup
    display_board(board)  # Display the initial board

    while True:
        free_fields = make_list_of_free_fields(board)  # Get current free fields
        board = enter_move(board, free_fields)  # Player makes a move

        # Check for a player win
        if victory_for(board, 'O'):
            display_board(board)
            print("You won!")
            break

        # Computer's turn
        free_fields = make_list_of_free_fields(board)  # Update free fields after player's move
        board = draw_move(board, free_fields)  # Computer makes a move
        display_board(board)

        # Check for a computer win
        if victory_for(board, 'X'):
            display_board(board)
            print("Computer won!")
            break

        # Check for a tie
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    print("launch as a script")
    main()
else :
    print("launched as a module")
