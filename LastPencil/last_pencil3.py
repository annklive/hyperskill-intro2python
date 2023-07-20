players = ['John', 'Jack']
PENCIL = "|"
n_pencils = int(input("How many pencils would you like to use:\n"))
first_player = input(f"Who will be the first ({','.join(players)}):\n")

remaining_pencils = n_pencils
player = players.index(first_player)

while remaining_pencils > 0:
    print(PENCIL*remaining_pencils)
    print(f"{players[player]}'s turn:")
    p = int(input())
    remaining_pencils -= p
    player = (player + 1) % 2
    

