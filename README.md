# Rock Paper Scissors Lizard Spock Game (Jogo de Pedra, Papel, Tesoura, Lagarto, Spock)

A command-line implementation of the extended Rock Paper Scissors game, including Lizard and Spock variations, made popular by the TV show "The Big Bang Theory".

## Description

This is a text-based version of Rock Paper Scissors Lizard Spock where players compete against the computer. The game extends the classic Rock Paper Scissors with two additional options: Lizard and Spock, creating more strategic possibilities. The game keeps track of the score and allows multiple rounds of play.

## Requirements

- Python 3.x
- No additional external dependencies required

## How to Run

1. Make sure you have Python installed on your system
2. Download the `main_game.py` file
3. Open a terminal/command prompt
4. Navigate to the directory containing the game file
5. Run the following command:

```python
python main_game.py
```

## How to Play

1. When prompted, select your move by entering a number:
   - 0 for Paper (Papel)
   - 1 for Rock (Pedra)
   - 2 for Scissors (Tesoura)
   - 3 for Lizard (Lagarto)
   - 4 for Spock

2. The computer will randomly select its move

## Game Rules

The game follows these winning conditions:
- Scissors cuts Paper
- Paper covers Rock
- Rock crushes Lizard
- Lizard poisons Spock
- Spock smashes Scissors
- Scissors decapitates Lizard
- Lizard eats Paper
- Paper disproves Spock
- Spock vaporizes Rock
- Rock crushes Scissors

3. After each round:
   - The game will display both moves
   - Show who won the round
   - Update the score
   - Ask if you want to play again

4. To continue playing:
   - Enter 0 for Yes
   - Enter 1 for No

## Features

- Score tracking
- Input validation
- Clear screen between rounds
- Cross-platform compatibility (Windows/Unix)
- Error handling for invalid inputs
- Portuguese interface

## Project Structure

```
.
├── README.md          # Documentation file
└── main_game.py      # Main game script containing game logic and interface
```