# Word Scramble Game ✨

## About the Project
This is a simple Word Scramble game written in Python. The game randomly selects a word, scrambles it, and challenges the player to guess the original word within a limited number of attempts. If the player guesses correctly, they win; otherwise, they lose and are given the correct answer. The game also allows for replaying after each round.

## Why I Built This 🧠
I am currently revising my Python skills, focusing on foundational concepts such as:
- Variables and data types
- Loops (`while` loops, loop control)
- Conditional statements (`if`, `else`, `elif`)
- User input handling
- Randomization (`random.sample()` for shuffling)
- Basic error handling (`sys.exit()` for graceful exits)

This project serves as a hands-on exercise to reinforce these concepts while creating something fun and interactive.

## How It Works 🔄
1. The game starts by displaying an introduction message.
2. It attempts to fetch a random word using the `random-word` library (with retries if needed).
3. The word is scrambled, ensuring it differs from the original.
4. The player gets **two attempts** to guess the correct word.
5. If they guess correctly, they win! 🎉 If not, they lose and see the correct word.
6. The player can choose to **play again** or exit.

## Features ✅
- Ensures a valid word is fetched (retries up to 5 times if necessary).
- Scrambles the word in a way that guarantees it's different from the original.
- Allows replaying instead of forcing an exit after one game session.

## How to Run 🚀
Make sure you have Python installed and the `random-word` library:
```bash
pip install random-word
```
Then, simply run the script:
```bash
python word_scramble.py
```

## Future Improvements 🛠️
- Add difficulty levels (short vs. long words).
- Implement a scoring system.
- Enhance error handling for API failures.

## Lessons Learned 📖
Writing this game helped reinforce:
- How to properly structure loops and conditionals.
- The importance of handling edge cases (e.g., API failures).
- Debugging strategies (e.g., printing values for testing and then removing debug prints for production).


