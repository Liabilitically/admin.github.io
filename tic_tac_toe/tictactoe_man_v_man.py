def play_against_player():
    def printboard(board):
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

    def play(box,xo):
        box = int(box)

        board[box] = xo

        if xo=='x':
            hX.append(box)
        else:
            hO.append(box)
        printboard(board)
        
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    hX = []
    hO = []
    X = False
    O = False

    def setup():
        board_sample = [[0,1,2],[3,4,5],[6,7,8]]

        for i in board_sample:
            print(i)

    def check():
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


    box = [0,1,2,3,4,5,6,7,8]
    xo = ['x','o']
    setup()
    X = False
    O = False
    for turns in range(9):
        if turns%2==0 and X==False and O==False:
            print("It's X's turn!")
            expected = 'x'
        elif turns%2==1 and X==False and O==False:
            print("It's O's turn!")
            expected = 'o'

        if X==False and O==False:
            inp = input("Enter submission: ")
            while True:
                try:
                    first = int(inp[0])
                except:
                    print("Invalid entry! (Exit key 02)")
                if (len(inp)==2) and (first in box) and (inp[1] in xo) and (inp[1]==expected) and (first not in (hX or hO)):
                    break
                else:
                    print("Invalid entry! (Exit key 01)")
                inp = input("Enter corrected submission: ")

            play(inp[0],inp[1])
            X = check()[0]
            O = check()[1]
        else:
            if X==True:
                print("X won!")
            elif O==True:
                print("O won!")
            
            break

    if X==False and O==False:
        print("Ooh, it's a tie!")
    else:
        print("Congratulations!")