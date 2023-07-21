import random

word_list = ['python', 'java', 'swift', 'javascript']
chosen_word = random.choice(word_list)
masker = '-'
hint = masker * len(chosen_word)
attemps = 8

print("H A N G M A N")

for i in range(attemps):
    print()
    print(hint)
    guess = input("Input a letter: ")
    if guess in hint:
        continue
    else:
        if guess in chosen_word: 
            idx = 0
            new_hint = ''
            while idx < len(chosen_word):
                if hint[idx] != masker:
                    new_hint += hint[idx]
                elif chosen_word[idx] == guess:
                    new_hint += guess
                else:
                    new_hint += masker
                idx += 1
            hint = new_hint
        else:
            print("That letter doesn't appear in the word.")

print()
print("Thanks for playing!")

