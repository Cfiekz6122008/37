import pygame
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man следует за курсором")

BACKGROUND = (0, 0, 0)

try:
    pacman_images = {
        "up": pygame.image.load("resours/pacman_up.png"),
        "down": pygame.image.load("resours/pacman_down.png"),
        "left": pygame.image.load("resours/pacman_left.png"),
        "right": pygame.image.load("resours/pacman_right.png"),
        "up_left": pygame.image.load("resours/pacman_up_left.png"),
        "up_right": pygame.image.load("resours/pacman_up_right.png"),
        "down_left": pygame.image.load("resours/pacman_down_left.png"),
        "down_right": pygame.image.load("resours/pacman_down_right.png")
    }

    for key in pacman_images:
        pacman_images[key] = pygame.transform.scale(pacman_images[key], (40, 40))
except:
    # Создаем заглушки для всех направлений
    pacman_images = {
        "up": pygame.Surface((40, 40), pygame.SRCALPHA),
        "down": pygame.Surface((40, 40), pygame.SRCALPHA),
        "left": pygame.Surface((40, 40), pygame.SRCALPHA),
        "right": pygame.Surface((40, 40), pygame.SRCALPHA),
        "up_left": pygame.Surface((40, 40), pygame.SRCALPHA),
        "up_right": pygame.Surface((40, 40), pygame.SRCALPHA),
        "down_left": pygame.Surface((40, 40), pygame.SRCALPHA),
        "down_right": pygame.Surface((40, 40), pygame.SRCALPHA)
    }

    # Рисуем желтые круги для всех направлений
    for key in pacman_images:
        pygame.draw.circle(pacman_images[key], (255, 255, 0), (20, 20), 20)

        # Добавляем "рот" для каждого направления
        if key == "up":
            pygame.draw.polygon(pacman_images[key], (0, 0, 0), [(20, 20), (40, 0), (0, 0)])
        elif key == "down":
            pygame.draw.polygon(pacman_images[key], (0, 0, 0), [(20, 20), (40, 40), (0, 40)])
        elif key == "left":
            pygame.draw.polygon(pacman_images[key], (0, 0, 0), [(20, 20), (0, 40), (0, 0)])
        elif key == "right":
            pygame.draw.polygon(pacman_images[key], (0, 0, 0), [(20, 20), (40, 0), (40, 40)])
        elif key == "up_left":
            pygame.draw.polygon(pacman_images[key], (0, 0, 0), [(20, 20), (0, 0), (10, 0), (0, 10)])
        elif key == "up_right":
            pygame.draw.polygon(pacman_images[key], (0, 0, 0), [(20, 20), (40, 0), (30, 0), (40, 10)])
        elif key == "down_left":
            pygame.draw.polygon(pacman_images[key], (0, 0, 0), [(20, 20), (0, 40), (10, 40), (0, 30)])
        elif key == "down_right":
            pygame.draw.polygon(pacman_images[key], (0, 0, 0), [(20, 20), (40, 40), (30, 40), (40, 30)])

pacman_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
speed = 4


def get_direction(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]

    if abs(dx) < 2 and abs(dy) < 2:
        return "right"

    angle = math.degrees(math.atan2(-dy, dx)) % 360

    if 22.5 <= angle < 67.5:
        return "up_right"
    elif 67.5 <= angle < 112.5:
        return "up"
    elif 112.5 <= angle < 157.5:
        return "up_left"
    elif 157.5 <= angle < 202.5:
        return "left"
    elif 202.5 <= angle < 247.5:
        return "down_left"
    elif 247.5 <= angle < 292.5:
        return "down"
    elif 292.5 <= angle < 337.5:
        return "down_right"
    else:
        return "right"


def move_towards(pos1, pos2, speed):
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x2 - x1
    dy = y2 - y1
    distance = max(1, math.sqrt(dx * dx + dy * dy))

    if distance > speed:
        x1 += dx * speed / distance
        y1 += dy * speed / distance
    else:
        x1, y1 = x2, y2

    return (x1, y1)


clock = pygame.time.Clock()
FPS = 60
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    direction = get_direction(pacman_pos, mouse_pos)
    pacman_pos = move_towards(pacman_pos, mouse_pos, speed)

    screen.fill(BACKGROUND)

    # Проверяем, существует ли направление в словаре
    if direction in pacman_images:
        pacman_rect = pacman_images[direction].get_rect(center=pacman_pos)
        screen.blit(pacman_images[direction], pacman_rect)
    else:
        # Если направление не найдено, используем направление по умолчанию
        pacman_rect = pacman_images["right"].get_rect(center=pacman_pos)
        screen.blit(pacman_images["right"], pacman_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()