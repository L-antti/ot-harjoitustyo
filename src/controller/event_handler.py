import pygame
from game_state import GameState


class EventHandler:
    """Handles user input and game events."""

    def __init__(self, launcher, logic):
        """
        Sets up the event handler with launcher and game logic.

        Args:
            launcher (Launcher): The launcher object used to shoot beans.
            logic (GameLogic): The game logic managing game states and actions.
        """
        self.launcher = launcher
        self.logic = logic
        self.running = True
        self.in_menu = True

    def process_events(self):
        """
        Handles key inputs and game events.

        Returns:
            bool: True if game started from menu, otherwise False.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.launcher.rotate(1)
        if keys[pygame.K_RIGHT]:
            self.launcher.rotate(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.in_menu:
                    self.in_menu = False
                    return True
                if event.key == pygame.K_UP and self.logic.state == GameState.IDLE:
                    self.logic.launch_next_bean(self.launcher)

        return False
