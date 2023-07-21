EMPTY = '_'

def check_winner(board):
    n_row = len(board)
    n_col = len(board[0])
    winner = []

    # horizontal  
    for i in range(n_row):
        cell = board[i][0]
        j = 1
        while j < n_col and board[i][j] == cell:
            j += 1
        if j == n_col:
            winner.append(cell)

    # vertical
    for i in range(n_col):
        cell = board[0][i]
        j = 1
        while j < n_row and board[j][i] == cell:
            j += 1
        if j == n_row:
            winner.append(cell)
    
    # diagonal
    cell = board[0][0]
    i = 1
    j = 1
    while i < n_row and j < n_col and board[i][j] == cell:
        i += 1
        j += 1
    if i > n_row and j > n_col:
        winner.append(cell)

    cell = board[0][n_col-1]
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
    

b = input()
board = [list(b[:3]), list(b[3:6]), list(b[6:9])]
print('---------')
for i in range(len(board)):
    print('| ', end='')
    for j in range(len(board[i])):
        print(f"{board[i][j]} ", end='')
    print('|')
print('---------')
winner = check_winner(board)

if impossible_status(board, winner):
    print("Impossible")
elif len(winner) == 1:
    print(f"{winner[0]} wins")
elif len(winner) == 0:
    if game_finished(board):
        print("Draw")
    else:
        print("Game not finished")

    
