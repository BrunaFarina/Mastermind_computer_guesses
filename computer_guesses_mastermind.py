import random
board = ["_", "_", "_", "_"]
def guess_computer(board):
    value1 = str(random.randint(0, 9))
    value3 = str(random.randint(0, 9))
    value4 = str(random.randint(0, 9))
    value2 = str(random.randint(0, 9))
    guess = value1 + value2 + value3 + value4
    return guess

def guess_my_number_mastermind(board):
    feedback = ""
    board_check = []
    comp_guess = ""
    while board != comp_guess:
        comp_guess = guess_computer(board)
        print(board[0] + board[1] + board[2] + board[3])
        for i in range(0, len(comp_guess)):
            if board[i] == comp_guess[i]:
                board[i] = comp_guess[i]
                comp_guess = "".join(str(x) for x in board)
        feedback = input(f"Any correct digit in {comp_guess}? ")
        if feedback == "yes" or feedback == "y":
            board_check = input(f"Write the numbers here replacing (or maintaining) the underscores (ex: '_3_8'): ")
            board = board_check
        else:
            print("Try again, Mike!")
    print(f"You got {comp_guess} correctly!")
            #board = board.join(str(x) for x in board_check)


guess_my_number_mastermind(board)