import pygame
import math

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man следует за курсором")

# Цвета
BACKGROUND = (0, 0, 0)

# Загрузка изображений Pac-Man для разных направлений
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
    # Масштабирование изображений (если нужно)
    for key in pacman_images:
        pacman_images[key] = pygame.transform.scale(pacman_images[key], (40, 40))
except:
    # Заглушки, если изображения не найдены
    pacman_images = {
        "up": pygame.Surface((40, 40), pygame.SRCALPHA),
        # ... остальные направления аналогично
    }
    # Рисуем желтые круги в качестве заглушек
    for key in pacman_images:
        pygame.draw.circle(pacman_images[key], (255, 255, 0), (20, 20), 20)

# Начальная позиция Pac-Man
pacman_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
speed = 4


# Функция определения направления
def get_direction(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]

    # Если расстояние очень маленькое, не меняем направление
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


# Функция движения к цели
def move_towards(pos1, pos2, speed):
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x2 - x1
    dy = y2 - y1
    distance = max(1, math.sqrt(dx * dx + dy * dy))

    # Плавное движение
    if distance > speed:
        x1 += dx * speed / distance
        y1 += dy * speed / distance
    else:
        x1, y1 = x2, y2

    return (x1, y1)


# Игровой цикл
clock = pygame.time.Clock()
FPS = 60
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем позицию курсора
    mouse_pos = pygame.mouse.get_pos()

    # Определяем направление и двигаем Pac-Man
    direction = get_direction(pacman_pos, mouse_pos)
    pacman_pos = move_towards(pacman_pos, mouse_pos, speed)

    # Отрисовка
    screen.fill(BACKGROUND)

    # Рисуем Pac-Man с учетом направления
    pacman_rect = pacman_images[direction].get_rect(center=pacman_pos)
    screen.blit(pacman_images[direction], pacman_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()