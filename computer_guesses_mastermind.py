import random

def guess_computer(board):
    # Generate a random guess
    guess = ""
    for i in range(4):
        # If the digit is already guessed correctly, keep it the same
        if board[i] != "_":
            guess += board[i]
        else:
            guess += str(random.randint(0, 9))
    return guess

def guess_my_number_mastermind(board):
    feedback = ""
    while True:
        comp_guess = guess_computer(board)
        feedback = input("Any correct digits in the right position (yes/no)? ").lower()
        if feedback == "yes" or feedback == "y":
            # Ask the user to input the correct digits
            board_check = input("Write the numbers here replacing (or maintaining) the underscores (e.g., '_3_8'): ")
            # Update the board with correct digits
            for i in range(4):
                if board_check[i] != "_":
                    board[i] = board_check[i]
        elif feedback == "no" or feedback == "n":
            print("Try again, Mike!")
        else:
            print("Please enter 'yes' or 'no'.")
        # Check if the board matches the guess
        if "".join(board) == comp_guess:
            print(f"The computer guessed {comp_guess} correctly!")
            break

board = ["_", "_", "_", "_"]
guess_my_number_mastermind(board)
