EMPTY = ' '

def check_winner(board):
    n_row = len(board)
    n_col = len(board[0])
    winner = []

    # horizontal  
    for i in range(n_row):
        cell = board[i][0]
        if cell == EMPTY: continue
        j = 1
        while j < n_col and board[i][j] == cell:
            j += 1
        if j == n_col:
            winner.append(cell)

    # vertical
    for i in range(n_col):
        cell = board[0][i]
        if cell == EMPTY: continue
        j = 1
        while j < n_row and board[j][i] == cell:
            j += 1
        if j == n_row:
            winner.append(cell)
    
    # diagonal
    cell = board[0][0]
    if cell != EMPTY:
        i = 1
        j = 1
        while i < n_row and j < n_col and board[i][j] == cell:
            i += 1
            j += 1
        if i > n_row and j > n_col:
            winner.append(cell)

    cell = board[0][n_col-1]
    if cell != EMPTY:
        i = 1 
        j = n_col-2 
        while i < n_row and j >= 0 and board[i][j] == cell:
            i += 1 
            j -= 1
        if i == n_row and j == -1:
            winner.append(cell)

    return list(set(winner))

def game_finished(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False
    return True

def impossible_status(board, winner):
    if 'X' in winner and 'O' in winner:
        return True

    n_X = 0
    n_O = 0 
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X':
                n_X += 1
            elif board[i][j] == 'O':
                n_O += 1
    return abs(n_X - n_O) >= 2

def show_board(board):
    print('---------')
    for i in range(len(board)):
        print('| ', end='')
        for j in range(len(board[i])):
            print(f"{board[i][j]} ", end='')
        print('|')
    print('---------')

def game_turns(player):
    while True:
        try:
            move = [int(i) for i in (input()).split()]
            x, y = move[0], move[1]
            if x >= 1 and x <= 3 and y >= 1 and y <= 3:
                if board[x-1][y-1] != EMPTY:
                    print("This cell is occupied! Choose another one!")
                else:
                    break
            else:
                print("Coordinates should be from 1 to 3!")
        except ValueError:
            print('You should enter numbers!')

    board[x-1][y-1] = player
    show_board(board)

    
b = EMPTY * 9
board = [list(b[:3]), list(b[3:6]), list(b[6:9])]
show_board(board)

players = ['X', 'O']
current_player = 0

while True:
    player = players[current_player]
    game_turns(player)

    winner = check_winner(board)

    if impossible_status(board, winner):
        #print("Impossible")
        pass
    elif len(winner) == 1:
        print(f"{winner[0]} wins")
        break
    elif len(winner) == 0:
        if game_finished(board):
            print("Draw")
            break
        else:
            #print("Game not finished")
            pass

    current_player = (current_player + 1) % 2
