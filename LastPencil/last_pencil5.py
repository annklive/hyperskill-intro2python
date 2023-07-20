import random


players = ['John', 'Jack']
PENCIL = "|"

print("How many pencils would you like to use:")
while True:
    try:
        n = int(input())
        if n < 0:
            print("The number of pencils should be numeric")
        elif n == 0:
            print("The number of pencils should be positive")
        else:
            n_pencils = n
            break
    except ValueError:
        print("The number of pencils should be numeric")

print(f"Who will be the first ({','.join(players)}):")
while True:
    p = input()
    if p not in players:
        print(f"Choose between '{players[0]}' and '{players[1]}'")
    else:
        first_player = p
        break

remaining_pencils = n_pencils
bot = players.index('Jack')
human = (bot + 1) % 2

possible_takens = ['1','2','3']

player = players.index(first_player)
while remaining_pencils > 0:
    print(PENCIL*remaining_pencils)
    print(f"{players[player]}'s turn:")
    if player == human:
        while True: 
            n_taken = input()
            if n_taken not in possible_takens:
                print("Possible values: '1', '2' or '3'")
            else:
                n_taken = int(n_taken)
                if n_taken > remaining_pencils:
                    print("Too many pencils were taken")
                else:
                    break
    else: # Bot 
        if remaining_pencils == 1:
            n_taken = 1
        elif (remaining_pencils - 5) % 4 == 0:
            n_taken = random.choice([1, 2, 3])
        elif remaining_pencils % 4 == 0:
            n_taken = 3
        elif (remaining_pencils - 3) % 4 == 0:
            n_taken = 2
        elif (remaining_pencils - 2) % 4 == 0:
            n_taken = 1
        print(n_taken)
       
    remaining_pencils -= n_taken
    player = (player + 1) % 2
    
    if remaining_pencils == 0:
        print(f"{players[player]} won!")

