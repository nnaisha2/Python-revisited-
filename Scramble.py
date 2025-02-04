import random
import sys
from random_word import RandomWords

while True:
    print('This is a simple word scramble game ✨')
    attemptsLeft = 2
    r = RandomWords()

    # Ensure a valid word is fetched
    realWord = None
    for _ in range(5):  # Try up to 5 times
        realWord = r.get_random_word()
        if realWord:  
            break  
    if not realWord:  
        print("Error fetching word. Please try again later.")
        sys.exit()

    print(realWord)  # Debugging, remove this for GitHub

    # Scramble word ensuring it's different
    word = list(realWord)
    scrambledWord = "".join(random.sample(word, len(word)))
    while scrambledWord == realWord:
        scrambledWord = "".join(random.sample(word, len(word)))

    print('Here is the scrambled word:', scrambledWord)

    # Player input loop
    while attemptsLeft > 0:
        guess = input('Please try: ')
        if guess == realWord:
            print('Hooray! 🎉 You won!')
            break
        else:
            attemptsLeft -= 1
            print('Not correct, attempts left:', attemptsLeft)

    if guess != realWord:
        print('You lost! 😞 The correct word was:', realWord)

    # Ask if they want to play again
    while True:
        userinput = input('Do you want to play again? (y/n): ').lower()
        if userinput == 'n':
            print("Thanks for playing! Goodbye. 👋")
            sys.exit()
        elif userinput == 'y':
            break  # Restart the game loop
