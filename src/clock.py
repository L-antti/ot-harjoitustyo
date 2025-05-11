import pygame


class Clock:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(self, fps):
        """
        Controls the game's frame rate.

        Args:
            fps (int): Frames per second to cap the game loop.
        """
        self.clock.tick(fps)
