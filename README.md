# Rock–Paper–Scissors–Plus Referee Bot

## Introduction
This project implements a simple conversational referee for a modified version of the
classic Rock–Paper–Scissors game. The bot manages the game flow, validates user inputs,
enforces the rules consistently, and keeps track of the game state across multiple rounds.

The goal of this implementation is not to build a complex interface, but to clearly
demonstrate clean state management, rule enforcement, and agent–tool separation in a
short, interactive game setting.

---

## Game Rules
- The game is played for a maximum of three rounds (best of three).
- Valid moves are: `rock`, `paper`, `scissors`, and `bomb`.
- Each player may use `bomb` only once per game.
- `Bomb` defeats all other moves.
- If both players use `bomb`, the round results in a draw.
- Any invalid input counts as a wasted round.
- The game ends automatically after the third round.

---

## State Management
All game-related information is stored in a dedicated `GameState` object.  
The state tracks:
- Current round number
- User and bot scores
- Whether each player has already used the bomb
- A game-over flag
- A history of played rounds

Keeping the state explicit and separate ensures that the game logic does not rely on
prompt memory and remains deterministic and easy to reason about.

---

## Agent and Tool Design
The implementation is structured to keep responsibilities clearly separated:

- **Agent (`agent.py`)**  
  The agent is responsible for interpreting user input, coordinating tool calls, and
  generating user-facing responses. It does not contain game logic itself.

- **Tools (`tools.py`)**  
  Tools handle move validation, rule enforcement, round resolution, and state updates.
  All changes to the game state are performed through these functions.

- **Game Loop (`main.py`)**  
  The game loop manages user interaction through the command line, prints rules,
  advances rounds, and ends the game once the maximum number of rounds is reached.

This separation keeps the system easy to extend and aligns with good agent design
practices.

---

## Design Decisions and Tradeoffs
- The bot’s move selection is intentionally random to keep the focus on rule enforcement
  rather than strategy.
- No external storage or databases are used, as the game is intended to run as a single,
  self-contained session.
- The interface is command-line based to stay within the assignment constraints and
  keep the implementation lightweight.

---

## Possible Improvements
Given more time, the following enhancements could be explored:
- Configurable number of rounds or rule variations
- Smarter bot strategies based on previous rounds
- A replay or summary view using the stored round history
- A UI layer built separately from the core logic

---

## Running the Game
Install the required dependency and start the game using:

```bash
pip install -r requirements.txt
python main.py
