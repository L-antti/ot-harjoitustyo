import pygame
from game_area import GameArea
from game_ui import GameUI
from game_logic import GameLogic
from game_state import GameState
from menu import GameMenu
from sprites.launcher import Launcher
from clock import Clock
from settings import LAUNCHER_POSITION, FPS


class GameController:
    def __init__(self, screen):
        self.menu = GameMenu(screen)
        self.ui = GameUI(screen)
        self.area = GameArea()
        self.logic = GameLogic(self.area)
        self.launcher = Launcher(LAUNCHER_POSITION)
        self.clock = Clock()
        self.running = True
        self.in_menu = True

    def run(self):
        while self.running:
            if self.in_menu:
                self.menu.draw_menu()
                pygame.display.flip()
                user_input = self.menu.handle_input()
                if user_input:
                    pygame.event.clear()
                    self.in_menu = False
            else:
                self.handle_events()
                if self.logic.state != GameState.IDLE:
                    self.logic.update_game_state()
                self.render()
                self.clock.tick(FPS)

    def handle_events(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.launcher.rotate(1)
        if keys[pygame.K_RIGHT]:
            self.launcher.rotate(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.logic.state == GameState.IDLE:
                    self.logic.launch_next_bean(self.launcher)

    def render(self):
        self.ui.draw_game_area()
        self.ui.draw_score(self.logic.score)
        self.ui.draw_beans(self.area.beans)

        if self.logic.state == GameState.MOVING:
            self.ui.draw_single_bean(self.logic.current_bean)

        if self.logic.state != GameState.ADDING_ROW:
            self.ui.draw_launcher(self.launcher)

        if self.logic.state == GameState.GAME_OVER:
            self.ui.draw_game_over()

        self.ui.draw_next_bean(self.area.bean_queue)
        self.ui.draw_bean_queue(self.area.bean_queue)

        pygame.display.flip()
