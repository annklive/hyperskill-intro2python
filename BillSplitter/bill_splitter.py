import random


n_friends = int(input("Enter the number of friends joining (including you):\n"))

if n_friends <= 0:
    print("No one is joining for the party")
else:
    friends = {}
    
    print("\nEnter the name of every friend (including you), each on a new line:")
    for n in range(n_friends):
        name = input()
        friends[name] = 0
    
    total = int(input("\nEnter the total bill value:\n"))
    share = round(total / n_friends, 2)
    for name in friends:
        friends[name] = share
            
    lucky_feature = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky_feature == "Yes":        
        the_lucky = random.choice(list(friends.keys()))
        print(f"{the_lucky} is the lucky one!")
        share = round(total/(n_friends-1), 2)
        friends = {f:share for f in friends if f != the_lucky}
        friends[the_lucky] = 0
    else:
        print("\nNo one is going to be lucky")
        
    print('\n', friends)
