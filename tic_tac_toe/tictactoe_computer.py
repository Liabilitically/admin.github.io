import random

def play_against_computer():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    hX = []
    hO = []
    X_won = False
    O_won = False
    possible_answers = ['0','1','2','3','4','5','6','7','8']
    user_choice = input("Would you like to be X or O?(x/o) ")

    def print_board(board):
        print("   |   |   ")
        print(" " + board[0] + " | " + board[1] + " | " + board[2] + "  ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" " + board[3] + " | " + board[4] + " | " + board[5] + "  ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" " + board[6] + " | " + board[7] + " | " + board[8] + "  ")
        print("   |   |   ")

    def print_with_input(user_input,computer_input,user_x_or_o):
        user_input = int(user_input)
        computer_input = int(computer_input)
        if user_x_or_o=="x":
            board[user_input] = "x"
            board[computer_input] = "o"
            print_board(board)
        elif user_x_or_o=="o":
            board[user_input] = "o"
            board[computer_input] = "x"
            print_board(board)

    def print_sample_board():
        sample_board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print("   |   |   ")
        print(" " + sample_board[0] + " | " + sample_board[1] + " | " + sample_board[2] + "  ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" " + sample_board[3] + " | " + sample_board[4] + " | " + sample_board[5] + "  ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" " + sample_board[6] + " | " + sample_board[7] + " | " + sample_board[8] + "  ")
        print("   |   |   ")

    def check(hX,hO):
        if ((0 in hX) and (1 in hX) and (2 in hX)) or ((3 in hX) and (4 in hX) and (5 in hX)) or ((6 in hX) and (7 in hX) and (8 in hX)) or ((0 in hX) and (3 in hX) and (6 in hX)) or ((1 in hX) and (4 in hX) and (7 in hX)) or ((2 in hX) and (5 in hX) and (8 in hX)) or ((0 in hX) and (4 in hX) and (8 in hX)) or ((2 in hX) and (4 in hX) and (6 in hX)):
            winX = True
            winO = False
        elif ((0 in hO) and (1 in hO) and (2 in hO)) or ((3 in hO) and (4 in hO) and (5 in hO)) or ((6 in hO) and (7 in hO) and (8 in hO)) or ((0 in hO) and (3 in hO) and (6 in hO)) or ((1 in hO) and (4 in hO) and (7 in hO)) or ((2 in hO) and (5 in hO) and (8 in hO)) or ((0 in hO) and (4 in hO) and (8 in hO)) or ((2 in hO) and (4 in hO) and (6 in hO)):
            winO = True
            winX = False
        else:
            winX = False
            winO = False

        return winX,winO

    if user_choice=="x":
        user_turns = 5
        print_sample_board()
        for i in range(user_turns):
            if X_won == False and O_won==False:
                user_input = input("Provide a box where you wish to play: ")
                if (len(user_input)!=1) or (user_input not in possible_answers):
                    while (len(user_input)!=1) or (user_input not in possible_answers):
                        print("Invalid entry! Please try again")
                        user_input = input("Provide a box where you wish to play: ")
                
                hX.append(int(user_input))
                possible_answers.remove(user_input)
                X_won = check(hX,hO)[0]
                if i==(user_turns-1):
                    break

                if X_won==False:
                    computer_input = str(random.randint(0,8))
                    if (computer_input not in possible_answers):
                        while (computer_input not in possible_answers):
                            computer_input = str(random.randint(0,8))

                    hO.append(int(computer_input))
                    possible_answers.remove(computer_input)
                    O_won = check(hX,hO)[1]

                print_with_input(user_input,computer_input,"x")
            elif X_won==True:
                print("You won!")
                break
            elif O_won==True:
                print("Oof, you lost!")
                break

        if X_won == False and O_won==False:
            print("Ooh, it's a tie!")    
    elif user_choice=="o":
        user_turns = 4
        print_sample_board()
        print()
        computer_input = str(random.randint(0,8))
        hX.append(int(computer_input))
        possible_answers.remove(computer_input)
        board[int(computer_input)] = "x"
        print_board(board)
        for i in range(user_turns):
            if X_won == False and O_won==False:
                user_input = input("Provide a box where you wish to play: ")
                if (len(user_input)!=1) or (user_input not in possible_answers):
                    while (len(user_input)!=1) or (user_input not in possible_answers):
                        print("Invalid entry! Please try again")
                        user_input = input("Provide a box where you wish to play: ")
                
                hO.append(int(user_input))
                possible_answers.remove(user_input)
                O_won = check(hX,hO)[1]

                if O_won==False:
                    computer_input = str(random.randint(0,8))
                    if (computer_input not in possible_answers):
                        while (computer_input not in possible_answers):
                            computer_input = str(random.randint(0,8))

                    hX.append(int(computer_input))
                    possible_answers.remove(computer_input)
                    X_won = check(hX,hO)[0]
                
                print_with_input(user_input,computer_input,"o")
            elif O_won==True:
                print("You won!")
                break
            elif X_won==True:
                print("Oof, you lost!")
                break

        if X_won == False and O_won==False:
            print("Ooh, it's a tie!")  
    else:
        print("Invalid response! Please re-run the program to try again.")