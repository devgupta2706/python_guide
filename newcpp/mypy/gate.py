import cmd

class OX_cmd():
    intro = "Enter your choice : new, load, quit" 
    prompt = "OX_game"
    Tgame = ""

def printGame():
    display = '''
    1 | 2 | 3    {} | {} | {}
    ---------    ------------
    4 | 5 | 6    {} | {} | {}
    ---------    ------------
    7 | 8 | 9    {} | {} | {}'''
    print(display.format(*game))

def winMove(i, game, mark):
    temp_game = list(game)
    temp_game[i] = mark
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]]
    for a, b, c in wins:
        chars = temp_game[a] + temp_game[b] + temp_game[c]
        if chars == "XXX" or chars == "OOO":
            return True
    return False

def userChoice():
    while True:
        inp = input("User choice your mark[x/o]: ")

        if inp in ['x', 'X']:
            print('You chose "X".\nYou play First.')
            return 'X', 'O';
        elif inp in ['o', 'O']:
            print('You chose "O".\nComputer plays First.')
            return 'O', 'X'
        else:
            print("Please Enter valid input!")

def compMove(comp, user, game):
    for i in range(0,9):
        if game[i -1] == " " and winMove(i - 1, game, comp):
            return (i - 1)

    for i in range(0,9):
        if game[i -1] == ' ' and winMove(i - 1, game, user):
            return (i - 1)
    for i in [5,1,7,3,2,9,8,6,4]:
        if game[i -1] == ' ':
            return (i - 1)

def userMove():
    while True:
        inp = input("Enter Your choice (1-9) : ")
        if inp.isdigit() and int(inp) > 0 and int(inp) < 10:
            inp = int(inp)
            if game[inp - 1] == " ":
                return (inp - 1)
            else:
                print("Your place is already taken")
        else:
            print("Please enter valid position (1-9)")

def new_game():
    while True:
        nxt = input('Do you want to play again?(y/n):')
        if nxt in['y','Y']:
            again = True
            break
        elif nxt in ['n','N']:
            print('Have a great day !')
            again = False
            break
        else:
            print('Enter correct input')
    if again:
        print('___NEW GAME___')
        main_game()
    else:
        return False

def win_check(human , cpu):
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if game[win_place[0] - 1] == game[win_place[1] - 1] == game[win_place[2] - 1] == human:
            print('User wins the match!')
            if not new_game():
                return False
        elif game[win_place[0] - 1] == game[win_place[1] - 1] == game[win_place[2] - 1] == cpu:
                print('Computer wins the match!')
                if not new_game():
                    return False
    if ' ' not in game:
        print('MATCH DRAW!!')
        if not new_game():
            return False
    return True

def main_game():
    global game 
    tGame = OX_cmd().prompt
    print(tGame)
    game = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    play = True

    user , comp = userChoice()
    printGame()
    while play:
        if user == 'X':
            x = userMove()
            game[x] = user
            printGame()
            play = win_check(user , comp)
            if play:
                o = compMove(comp , user , game)
                print(f'Computer Entered:', o + 1)
                game[o] = comp
                printGame()
                play = win_check(user , comp)
        else:
            x = compMove(comp , user , game)
            print('Computer Entered: ', x + 1)
            game[x] = comp
            printGame()
            play = win_check(user , comp)
            if play:
                o = userMove()
                game[o] = user
                printGame()
                play = win_check(user , comp)
main_game()