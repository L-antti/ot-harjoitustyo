import pygame
from game_state import GameState
from settings import FPS


class GameLoop:
    """Runs the main loop of the game."""

    def __init__(self, logic, events, renderer, gameover, clock):
        """
        Initializes the game loop with logic, event handler, renderer,
        game over controller, and clock.
        """
        self.logic = logic
        self.events = events
        self.renderer = renderer
        self.gameover_controller = gameover
        self.clock = clock

    def run(self):
        """
        Main loop that updates game state, handles input, draws the game,
        and controls the frame rate.
        """
        while self.events.running:
            exit_menu = self.events.process_events()

            if self.events.in_menu:
                self.renderer.draw_menu()
                if exit_menu:
                    pygame.event.clear()
            else:
                if self.logic.state != GameState.IDLE:
                    self.logic.update_game_state()

                self.gameover_controller.handle_game_over()

                self.renderer.render_game_view()

            self.clock.tick(FPS)
