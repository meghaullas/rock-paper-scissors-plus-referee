# tools.py

import random

VALID_MOVES = {"rock", "paper", "scissors", "bomb"}


def validate_move(move: str, state, player: str):
    move = move.lower().strip()

    if move not in VALID_MOVES:
        return False, "Invalid move"

    if move == "bomb":
        if player == "user" and state.user_bomb_used:
            return False, "Bomb already used by user"
        if player == "bot" and state.bot_bomb_used:
            return False, "Bomb already used by bot"

    return True, move


def bot_choose_move(state):
    possible_moves = ["rock", "paper", "scissors"]
    if not state.bot_bomb_used:
        possible_moves.append("bomb")
    return random.choice(possible_moves)


def resolve_round(user_move, bot_move):
    if user_move == bot_move:
        return "draw"

    if user_move == "bomb":
        return "user"

    if bot_move == "bomb":
        return "bot"

    beats = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    return "user" if beats[user_move] == bot_move else "bot"


def update_game_state(state, user_move, bot_move, winner):
    if user_move == "bomb":
        state.user_bomb_used = True
    if bot_move == "bomb":
        state.bot_bomb_used = True

    if winner == "user":
        state.user_score += 1
    elif winner == "bot":
        state.bot_score += 1

    state.history.append({
        "round": state.round_number,
        "user_move": user_move,
        "bot_move": bot_move,
        "winner": winner
    })

    state.round_number += 1

    if state.round_number > 3:
        state.game_over = True
