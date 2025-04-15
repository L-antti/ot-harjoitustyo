import pygame
from game_state import GameState
from sprites.bean import Bean
from settings import SCREEN_WIDTH, LAUNCHER_POSITION, MAX_Y


class GameLogic:
    def __init__(self, game_area):
        self.game_area = game_area
        self.state = GameState.IDLE
        self.current_bean = None
        self.score = 0
        self.failed_shots = 0

    def update_game_state(self):
        if (
            self.state == GameState.GAME_OVER
            or self.check_game_over()
            or self.state == GameState.IDLE
        ):
            return

        if self.state == GameState.LAUNCHING:
            self.launch_next_bean()
        elif self.state == GameState.MOVING:
            self.move_current_bean()
        elif self.state == GameState.EVALUATING:
            self.evaluate_bean()
        elif self.state == GameState.ADDING_ROW:
            self.game_area.add_new_row()
            self.transition_state(GameState.IDLE)

    def transition_state(self, new_state):
        self.state = new_state

    def check_game_over(self):
        for bean in self.game_area.beans:
            if bean.rect.bottom >= MAX_Y:
                self.transition_state(GameState.GAME_OVER)
                return True
        return False

    def launch_next_bean(self, launcher):
        if self.state != GameState.IDLE:
            return

        new_color = self.game_area.get_next_bean()
        self.current_bean = Bean(new_color, LAUNCHER_POSITION)

        self.current_bean.set_velocity(launcher.angle)

        self.transition_state(GameState.MOVING)

    def move_current_bean(self):
        bean = self.current_bean
        bean.rect.x += bean.velocity[0]
        bean.rect.y += bean.velocity[1]

        if bean.rect.left <= 0 or bean.rect.right >= SCREEN_WIDTH:
            bean.velocity[0] *= -1

        overlapping = pygame.sprite.spritecollide(
            bean, self.game_area.beans, False, pygame.sprite.collide_circle)
        if bean.rect.top <= 0 or overlapping:
            bean.attach(self.game_area.beans)
            bean.update_neighbours(self.game_area.beans)
            bean.velocity = [0, 0]
            self.transition_state(GameState.EVALUATING)

    def evaluate_bean(self):
        bean = self.current_bean
        self.game_area.update()

        group = self.get_connected_same_color(bean)

        if len(group) >= 3:
            self.game_area.beans.remove(group)
            self.score += len(group) * 10
            self.failed_shots = 0
        else:
            self.failed_shots += 1

        if self.failed_shots >= 3:
            self.transition_state(GameState.ADDING_ROW)
            self.failed_shots = 0
            if self.check_game_over():
                return
        else:
            self.transition_state(GameState.IDLE)

    def get_connected_same_color(self, start_bean, visited=None):
        if visited is None:
            visited = set()

        visited.add(start_bean)
        group = [start_bean]

        for neighbour in start_bean.neighbours:
            if neighbour.color == start_bean.color and neighbour not in visited:
                group.extend(self.get_connected_same_color(neighbour, visited))

        return group
