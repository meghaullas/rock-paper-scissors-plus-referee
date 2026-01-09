# main.py

from state import GameState
from agent import RPSRefereeAgent


def print_rules():
    print("Welcome to Rock–Paper–Scissors–Plus")
    print("Rules:")
    print("- Best of 3 rounds")
    print("- Moves: rock, paper, scissors, bomb (once per game)")
    print("- Bomb beats all other moves")
    print("- Invalid input wastes the round\n")


def main():
    state = GameState()
    agent = RPSRefereeAgent(state)

    print_rules()

    while not state.game_over:
        user_input = input(f"Round {state.round_number} — Enter your move: ")
        response = agent.process_user_input(user_input)
        print(response)
        print()

    print("Game Over")
    print(f"Final Score → You: {state.user_score}, Bot: {state.bot_score}")

    if state.user_score > state.bot_score:
        print("Final Result: You win the game 🎉")
    elif state.bot_score > state.user_score:
        print("Final Result: Bot wins the game")
    else:
        print("Final Result: Draw")


if __name__ == "__main__":
    main()
