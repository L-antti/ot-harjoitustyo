from enum import Enum


class GameState(Enum):
    IDLE = "idle"
    LAUNCHING = "launching"
    MOVING = "moving"
    EVALUATING = "evaluating"
    ADDING_ROW = "adding_row"
    GAME_OVER = "game_over"
