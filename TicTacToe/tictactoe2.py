b = input()
board = [list(b[:3]), list(b[3:6]), list(b[6:9])]
print('---------')
for i in range(len(board)):
    print('| ', end='')
    for j in range(len(board[i])):
        print(f"{board[i][j]} ", end='')
    print('|')
print('---------')
