import random
import sys

# Inicializace Pygame
pygame.init()

# Nastavení obrazovky
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokročilá FPS Střílečka")

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Hráč
player_img = pygame.Surface((50, 50))
player_img.fill(WHITE)
player_rect = player_img.get_rect(center=(screen_width//2, screen_height//2))
player_speed = 5

# Nepřátelé
enemy_img = pygame.Surface((30, 30))
enemy_img.fill((255, 0, 0))
enemy_rect = enemy_img.get_rect(center=(screen_width//4, screen_height//2))
enemy_speed = 3

# Hlavní smyčka hry
running = True
while running:
    screen.fill(BLACK)

    # Události
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pohyb hráče
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= player_speed
    if keys[pygame.K_s]:
        player_rect.y += player_speed
    if keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_d]:
        player_rect.x += player_speed

    # Pohyb nepřátel
    if enemy_rect.x < player_rect.x:
        enemy_rect.x += enemy_speed
    elif enemy_rect.x > player_rect.x:
        enemy_rect.x -= enemy_speed
    if enemy_rect.y < player_rect.y:
        enemy_rect.y += enemy_speed
    elif enemy_rect.y > player_rect.y:
        enemy_rect.y -= enemy_speed

    # Kreslení hráče a nepřátel
    screen.blit(player_img, player_rect)
    screen.blit(enemy_img, enemy_rect)

    # Obnovení obrazovky
    pygame.display.flip()

    # FPS
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
