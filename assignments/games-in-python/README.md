
# 🎮 Hangman (Jogo da Forca)

## 🎯 Objective

Build the classic Hangman game in Python to practice string manipulation, loops, conditionals and user input.

## 🎯 Objetivo

Construir a versão clássica do jogo da forca em Python, praticando manipulação de strings, loops, condicionais e entrada do usuário.

## ⏳ Duração estimada

60–90 minutos

## 🔧 Recursos fornecidos

- Código inicial: `starter-code.py`
- Lista de palavras exemplo (interna ao `starter-code.py`)

## 📝 Tasks

### 🛠️ 1 — Word selection and game state

#### Description
Choose a random word from a list and maintain the current state (revealed letters and wrong letters).

#### Requirements

- Select a random word from a predefined list.
- Represent player progress in the `_ _ a _ _` format.

### 🛠️ 2 — Player input and attempt logic

#### Description
Accept player guesses, update state and control remaining attempts.

#### Requirements

- Accept a single-letter input per attempt.
- Ignore invalid inputs (more than one character, non-alphabetic) with an error message.
- Update correct letters and wrong-guesses list; decrement attempts for wrong letters.

### 🛠️ 3 — Win/lose conditions and messages

#### Description
Detect end of game (word complete or attempts exhausted) and display appropriate messages.

#### Requirements

- Display a victory message with the completed word when the player guesses all letters.
- Display a defeat message when attempts run out, revealing the correct word.

### 🛠️ 4 — (Optional) Enhancements

#### Suggestions

- Allow guessing the full word.
- Save simple scores (remaining attempts) to a file.
- Improve the textual UI (ASCII hangman drawing).

## Examples / Usage

Run `starter-code.py` in the assignment folder to play the example version:

```bash
python3 starter-code.py
```

## How to test

- Manual tests: play several rounds, check invalid input handling and final messages.
- For automated tests, keep core logic in functions (e.g. `select_word()`, `process_guess(state, guess)`).

## Notes for instructor

- `starter-code.py` should orchestrate execution and call testable functions; avoid mixing core logic and I/O.

