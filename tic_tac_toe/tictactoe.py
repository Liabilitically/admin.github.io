from tictactoe_computer import play_against_computer
from tictactoe_man_v_man import play_against_player

game_mode = input("Do you wish to play against another player or against the computer?(p/c) ")

if game_mode=="p":
    play_against_player()
elif game_mode=="c":
    play_against_computer()
else:
    print("Invalid choice! Please re-run the program to try again!")