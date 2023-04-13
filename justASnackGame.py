import pygame
import random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

segment_width = 10
segment_height = 10

x = WINDOW_WIDTH / 2
y = WINDOW_HEIGHT / 2
dx = segment_width
dy = 0

food_x = round(random.randrange(0, WINDOW_WIDTH - segment_width) / 10.0) * 10.0
food_y = round(random.randrange(0, WINDOW_HEIGHT - segment_height) / 10.0) * 10.0

length = 1
score = 0

score_font = pygame.font.SysFont("arial", 20)
pygame.display.set_caption("justA Snake Game")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
snake_segments = [[x, y]]
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx = -segment_width
        dy = 0
    elif keys[pygame.K_RIGHT]:
        dx = segment_width
        dy = 0
    elif keys[pygame.K_UP]:
        dx = 0
        dy = -segment_height
    elif keys[pygame.K_DOWN]:
        dx = 0
        dy = segment_height
    x += dx
    y += dy
    if x < 0 or x >= WINDOW_WIDTH or y < 0 or y >= WINDOW_HEIGHT:
        score = 0
        length = 1
        x = WINDOW_WIDTH / 2
        y = WINDOW_HEIGHT / 2
        dx = segment_width
        dy = 0
        snake_segments.clear()
    if x == food_x and y == food_y:
        food_x = round(random.randrange(0, WINDOW_WIDTH - segment_width) / 10.0) * 10.0
        food_y = round(random.randrange(0, WINDOW_HEIGHT - segment_height) / 10.0) * 10.0
        score += 1
        length += 1
    head = [x, y]
    if head in snake_segments[1:]:
        score = 0
        length = 1  
        x = WINDOW_WIDTH / 2
        y = WINDOW_HEIGHT / 2
        dx = segment_width
        dy = 0  
        snake_segments.clear()
    snake_segments.insert(0, [x, y])
    if len(snake_segments) > length:
        snake_segments.pop()
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(food_x, food_y, segment_width, segment_height))
    for segment in snake_segments:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(segment[0], segment[1], segment_width, segment_height))
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))  
    pygame.display.update()
    clock.tick(20)
pygame.quit()
