# state.py

from dataclasses import dataclass, field

@dataclass
class GameState:
    round_number: int = 1
    user_score: int = 0
    bot_score: int = 0

    user_bomb_used: bool = False
    bot_bomb_used: bool = False

    game_over: bool = False

    history: list = field(default_factory=list)
