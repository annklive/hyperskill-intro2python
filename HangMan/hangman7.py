import random
import string

word_list = ['python', 'java', 'swift', 'javascript']
chosen_word = random.choice(word_list)
masker = '-'
hint = masker * len(chosen_word)
attemps = 8

guessed = set()

print("H A N G M A N")

while attemps > 0:
    print()
    print(hint)
    guess = input("Input a letter: ")

    if len(guess) != 1:
        print("Please, input a single letter.")
        continue
    if guess not in string.ascii_lowercase:
        print("Please, enter a lowercase letter from the English alphabet.")
        continue
    if guess in guessed:
        print("You've already guessed this letter.")
        continue
    else:
        guessed.add(guess)
    
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
        if hint == chosen_word:
            break
    else:
        attemps -= 1
        print("That letter doesn't appear in the word.")


print()
if hint != chosen_word:
    print("You lost!")
else:
    print(f"You guessed the word {chosen_word}!")
    print("You survived!")
