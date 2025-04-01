import pygame
import math
from sprites.launcher import Launcher
from sprites.bean import Bean
from clock import Clock


def main():
    window_width = 400
    window_height = 800
    display= pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("BEANSHOOTER")

    pygame.init()

    clock = Clock()

    running = True
    launcher = Launcher((window_width//2, window_height-50))

    beans = pygame.sprite.Group()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            launcher.rotate(2)
        if keys[pygame.K_RIGHT]:
            launcher.rotate(-2)
        if keys[pygame.K_UP]:
            angle_rad = math.radians(launcher.angle)
            new_bean = Bean((255, 255, 0), launcher.position)
            new_bean.velocity = [5 * math.cos(angle_rad), -5 * math.sin(angle_rad)]
            beans.add(new_bean)

        beans.update()

        display.fill((0, 0, 0)) 
        launcher.draw(display)



        beans.draw(display) 
        pygame.display.flip()

        clock.tick(60)





if __name__ == "__main__":
    main()