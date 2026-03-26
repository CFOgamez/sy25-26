import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 100]
player_size = 100

# Load player image
player_img = pygame.image.load("son-goku-super-saiyan-4.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (player_size, player_size))

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

# Load enemy image
enemy_img = pygame.image.load("BabyKiBlast.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (enemy_size, enemy_size))

# ✅ Trail list (stores previous positions)
trail = []

score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5

    # Keep player on screen
    player_pos[0] = max(0, min(WIDTH - player_size, player_pos[0]))

    # Update enemy position
    enemy_pos[1] += enemy_speed

    # Reset enemy
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        print(f"Score: {score}")

    # Collision detection
    if (enemy_pos[0] < player_pos[0] + player_size and
        enemy_pos[0] + enemy_size > player_pos[0] and
        enemy_pos[1] < player_pos[1] + player_size and
        enemy_pos[1] + enemy_size > player_pos[1]):
        print("Game Over!")
        game_over = True

    # ✅ Add current player position to trail
    trail.append((player_pos[0] + player_size // 2, player_pos[1] + player_size // 2))

    # Limit trail length
    if len(trail) > 15:
        trail.pop(0)

    # Drawing
    screen.fill((0, 0, 0))

    # ✅ Draw blurred yellow trail
    for i, pos in enumerate(trail):
        # Create fading effect
        alpha = int(255 * (i / len(trail)))
        radius = int(30 * (i / len(trail)) + 5)

        trail_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.circle(trail_surface, (255, 255, 0, alpha), pos, radius)
        screen.blit(trail_surface, (0, 0))

    # Draw enemy
    screen.blit(enemy_img, (enemy_pos[0], enemy_pos[1]))

    # Draw player
    screen.blit(player_img, (player_pos[0], player_pos[1]))

    pygame.display.update()
    clock.tick(30)

pygame.quit()