import random

board = [i for i in range(0, 9)]
player, computer = '', ''

moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))
tab = range(1, 10)


def print_board():
    x = 1
    for i in board:
        end = ' | '
        if x % 3 == 0:
            end = ' \n'
            if i != 1: end += '---------\n';
        char = ' '
        if i in ('X', 'O'): char = i;
        x += 1
        print(char, end=end)


def select_char():
    chars = ('X', 'O')
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars


def can_move(brd, player, move):
    if move in tab and brd[move - 1] == move - 1:
        return True
    return False


def can_win(brd, player, move):
    places = []
    x = 0
    for i in brd:
        if i == player: places.append(x);
        x += 1
    win = True
    for tup in winners:
        win = True
        for ix in tup:
            if brd[ix] != player:
                win = False
                break
        if win == True:
            break
    return win


def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move - 1] = player
        win = can_win(brd, player, move)
        if undo:
            brd[move - 1] = move - 1
        return (True, win)
    return (False, False)


def computer_move():
    move = -1
    # Winning Move
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            move = i
            break
    if move == -1:
        # Block
        for i in range(1, 10):
            if make_move(board, player, i, True)[1]:
                move = i
                break
    if move == -1:
        # Wise Choice
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move = mv
                    break
    return make_move(board, computer, move)


def space_exist():
    return board.count('X') + board.count('O') != 9


player, computer = select_char()
print('Player [%s] versus Computer [%s]' % (player, computer))
result = '%%% ! Draw ! %%%'
while space_exist():
    print_board()
    print('Make Your Move Wisely! [1-9] : ', end='')
    move = int(input())
    moved, won = make_move(board, player, move)
    if not moved:
        print(' >> Space Used Already ! Try another move !')
        continue
    #
    if won:
        result = '*** Voila ! You won ! ***'
        break
    elif computer_move()[1]:
        result = '=== Oh no ! You lose ! =='
        break;

print_board()
print(result)