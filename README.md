# Hangman

A classic word guessing game in Python. Available in English and Russian.

## Features

- Two languages: English and Russian
- Choose your own number of lives (3–10)
- Add your own words before the game
- Hints for the price of one life
- Letter validation (only one letter, only letters)

## How to run

1. Install Python
2. Run `hangman.py`
3. Choose a language: `en` or `ru`
4. Choose number of lives (3–10)
5. Add your own words (or type `no` / `нет`)
6. Guess the word letter by letter

## Commands

- Type a letter to guess it
- Type `hint` or `help` to get a hint (costs 1 life)
- Type `подсказка` or `помощь` (Russian version)

## Example

```
Choose a language/выбери язык (ru, en/рус, англ): en
How many lives do you want? (min. 3, max. 10.) 5
If you want, you can add your own words, if you don`t want, print «no»: no
Ok, so we start!

Game «Hangman»!
5-letter word. lives: 5

Rules:

Guess the word letter by letter

If the letter is in the word, it opens

If not, you lose a life
...

guess a letter: h
There is!
h _ _ _ _
guess a letter: o
There is!
h o _ _ _
...
You won! Word was: house
```

## Author

Restont
