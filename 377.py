import pygame
import math

pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Перемещение круга")

BACKGROUND = (0, 0, 0)
CIRCLE_COLOR = (255, 255, 255)
CIRCLE_RADIUS = 20
circle_pos = (320, 240)
angle = 20
speed = 2

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dx = speed * math.cos(math.radians(angle))
    dy = speed * math.sin(math.radians(angle))
    circle_pos = (circle_pos[0] + dx, circle_pos[1] + dy)

    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, CIRCLE_COLOR, (int(circle_pos[0]), int(circle_pos[1])), CIRCLE_RADIUS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()