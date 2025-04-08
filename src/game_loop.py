import random
import pygame
from sprites.bean import Bean
from settings import BACKGROUND_COLOR, BEAN_COLORS
from game_area import (initialize_predefined_beans,
                       initialize_bean_queue,
                       draw_bean_queue,
                       draw_next_bean,
                       draw_score)


def run_game(display, launcher, clock):
    beans = initialize_predefined_beans()
    bean_queue = initialize_bean_queue()
    next_bean_color = bean_queue.popleft()
    running = True
    previous_bean_attached = True
    current_bean = None
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            launcher.rotate(1)
        if keys[pygame.K_RIGHT]:
            launcher.rotate(-1)
        if keys[pygame.K_UP] and previous_bean_attached:
            new_bean = Bean(next_bean_color, launcher.position)
            new_bean.shoot(launcher.angle)
            beans.add(new_bean)
            current_bean = new_bean
            previous_bean_attached = False

            next_bean_color = bean_queue.popleft()
            bean_queue.append(random.choice(BEAN_COLORS))

        for bean in beans:
            bean.update(beans)
            if current_bean == bean and bean.velocity == [0, 0]:
                previous_bean_attached = True

        popping_beans = Bean.check_color_groups(beans)
        score += len(popping_beans) * 10
        for bean in popping_beans:
            beans.remove(bean)

        display.fill(BACKGROUND_COLOR)
        launcher.draw(display)
        draw_next_bean(display, next_bean_color, launcher.position)
        draw_bean_queue(display, bean_queue)
        draw_score(display, score)
        beans.draw(display)
        pygame.display.flip()
        clock.tick(60)
