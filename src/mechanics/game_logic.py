from game_state import GameState
from sprites.bean import Bean
from settings import LAUNCHER_POSITION, MAX_Y


class GameLogic:
    """Manages the core game mechanics, including bean movement, scoring,
    and game state transitions."""

    def __init__(self, game_area):
        self.game_area = game_area
        self.state = GameState.IDLE
        self.current_bean = None
        self.score = 0
        self.failed_shots = 0

    def update_game_state(self):
        """Updates the game state based on current conditions."""
        if self.state in [GameState.GAME_OVER, GameState.IDLE] or self.check_game_over():
            return

        state_actions = {
            GameState.LAUNCHING: self.launch_next_bean,
            GameState.MOVING: self.move_current_bean,
            GameState.EVALUATING: self.evaluate_bean,
            GameState.ADDING_ROW: lambda: (
                self.game_area.add_new_row(), self.transition_state(GameState.IDLE))
        }

        if self.state in state_actions:
            state_actions[self.state]()

    def transition_state(self, new_state, reset_failed_shots=False):
        """Handles transitions between different game states.

        Args:
            new_state (GameState): The next game state.
            reset_failed_shots (bool, optional): Whether to reset failed shot counter.
        """
        self.state = new_state
        if reset_failed_shots:
            self.failed_shots = 0

    def check_game_over(self):
        """Checks whether the game is over due to bean collisions."""
        if any(bean.rect.bottom >= MAX_Y for bean in self.game_area.beans):
            self.transition_state(GameState.GAME_OVER)
            return True
        return False

    def launch_next_bean(self, launcher):
        """Launches the next bean from the queue.

        Args:
            launcher (Launcher): The launcher object controlling bean shots.
        """
        if self.state != GameState.IDLE:
            return

        new_color = self.game_area.get_next_bean()
        self.current_bean = Bean(new_color, LAUNCHER_POSITION)
        self.current_bean.velocity = launcher.get_launch_velocity()
        self.transition_state(GameState.MOVING)

    def move_current_bean(self):
        """Moves the currently launched bean, handling collisions and physics."""
        if self.current_bean:
            bean = self.current_bean
            bean.move()
            if bean.has_collided(self.game_area.beans):
                self.game_area.attach_bean(bean)
                bean.stop()
                self.transition_state(GameState.EVALUATING)

    def evaluate_bean(self):
        """Evaluates the launched bean and checks for scoring or row additions."""
        bean = self.current_bean
        group = self.get_connected_same_color(bean)

        same_color_neighbour = any(
            neighbour.color == bean.color for neighbour in bean.neighbours)

        if len(group) >= 3:
            self.game_area.beans.remove(group)
            self.score += len(group) * 10
            self.transition_state(GameState.IDLE, reset_failed_shots=True)
        elif same_color_neighbour:
            self.transition_state(GameState.IDLE, reset_failed_shots=True)
        else:
            self.failed_shots += 1
            if self.failed_shots >= 3:
                self.transition_state(
                    GameState.ADDING_ROW, reset_failed_shots=True)
            else:
                self.transition_state(GameState.IDLE)

    def get_connected_same_color(self, start_bean, visited=None):
        """Finds all beans connected to the given bean that share the same color.

        Args:
            start_bean (Bean): The bean from which the search starts.
            visited (set, optional): Set of visited beans to prevent duplicate checks.
        Returns:
            list[Bean]: A list of connected beans with the same color.
        """
        if visited is None:
            visited = set()

        if start_bean in visited:
            return []

        visited.add(start_bean)
        group = [start_bean]

        for neighbour in start_bean.neighbours:
            if neighbour.color == start_bean.color:
                group.extend(self.get_connected_same_color(neighbour, visited))

        return group

    def reset_game(self):
        """Resets game to initial state."""
        self.state = GameState.IDLE
        self.current_bean = None
        self.score = 0
        self.failed_shots = 0
        self.game_area.reset()
