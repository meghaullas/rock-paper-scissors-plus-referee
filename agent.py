 # agent.py

from tools import (
    validate_move,
    bot_choose_move,
    resolve_round,
    update_game_state
)

class RPSRefereeAgent:
    def __init__(self, state):
        self.state = state

    def process_user_input(self, user_input: str):
        valid, result = validate_move(user_input, self.state, "user")

        # Invalid input → round wasted
        if not valid:
            wasted_round = self.state.round_number
            self.state.round_number += 1

            if self.state.round_number > 3:
                self.state.game_over = True

            return (
                f"Round {wasted_round}\n"
                "Invalid input. This round is wasted.\n"
                f"Score → You: {self.state.user_score}, Bot: {self.state.bot_score}"
            )

        user_move = result
        bot_move = bot_choose_move(self.state)

        winner = resolve_round(user_move, bot_move)
        update_game_state(self.state, user_move, bot_move, winner)

        response = (
            f"Round {self.state.round_number - 1}\n"
            f"You played: {user_move}\n"
            f"Bot played: {bot_move}\n"
        )

        if winner == "draw":
            response += "Result: Draw"
        elif winner == "user":
            response += "Result: You win this round"
        else:
            response += "Result: Bot wins this round"

        response += (
            f"\nScore → You: {self.state.user_score}, "
            f"Bot: {self.state.bot_score}"
        )

        return response
