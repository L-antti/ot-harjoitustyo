from enum import Enum


class GameState(Enum):
    """
    Enum class that defines the different game states.

    The game states are:
        - IDLE: The game is in an idle or paused state, no gameplay is happening.
        - LAUNCHING: When the player is launching a bean.
        - MOVING: When the bean is in motion.
        - EVALUATING: When the game is evaluating the bean's collision or grouping.
        - ADDING_ROW: When a new row of beans is added to the game area.
        - GAME_OVER: When the game is over.
    """
    IDLE = "idle"
    LAUNCHING = "launching"
    MOVING = "moving"
    EVALUATING = "evaluating"
    ADDING_ROW = "adding_row"
    GAME_OVER = "game_over"
