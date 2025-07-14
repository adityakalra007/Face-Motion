# main.py
import cv2
import pygame
from face_tracker import FaceTracker
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Face-Controlled Paddle Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

# Paddle
bar_width, bar_height = 100, 20
bar_x = WIDTH // 2 - bar_width // 2
bar_y = HEIGHT - 50
bar_color = (0, 102, 255)

# Ball
ball_radius = 12
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = random.choice([-4, 4])
ball_speed_y = -4
ball_color = (255, 0, 0)

# Game state
lives = 3
score = 0
game_over = False

# Webcam
cap = cv2.VideoCapture(0)
tracker = FaceTracker()

running = True
while running:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    if not game_over:
        # Track head angle
        angle = tracker.get_head_turn_angle(frame)
        angle = max(-20, min(20, angle))
        angle_ratio = (angle + 20) / 40
        target_x = int(angle_ratio * (WIDTH - bar_width))
        bar_x += (target_x - bar_x) * 0.3

        # Move ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Bounce off walls
        if ball_x <= ball_radius or ball_x >= WIDTH - ball_radius:
            ball_speed_x *= -1
        if ball_y <= ball_radius:
            ball_speed_y *= -1

        # Paddle collision
        if bar_y <= ball_y + ball_radius <= bar_y + bar_height and \
           bar_x <= ball_x <= bar_x + bar_width:
            ball_speed_y *= -1
            score += 1

        # Missed the ball
        if ball_y > HEIGHT:
            lives -= 1
            if lives == 0:
                game_over = True
            else:
                ball_x = WIDTH // 2
                ball_y = HEIGHT // 2
                ball_speed_x = random.choice(-6, 6)
                ball_speed_y = 6
            


    # Draw everything
    screen.fill((255, 255, 255))  # White background

    if not game_over:
        pygame.draw.rect(screen, bar_color, (int(bar_x), bar_y, bar_width, bar_height))
        pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
        screen.blit(score_text, (20, 20))
        screen.blit(lives_text, (WIDTH - 120, 20))
    else:
        over_text = font.render("🎮 Game Over!", True, (200, 0, 0))
        final_score = font.render(f"Final Score: {score}", True, (0, 0, 0))
        restart = font.render("Press ESC to exit", True, (100, 100, 100))
        screen.blit(over_text, (WIDTH//2 - 100, HEIGHT//2 - 60))
        screen.blit(final_score, (WIDTH//2 - 100, HEIGHT//2))
        screen.blit(restart, (WIDTH//2 - 100, HEIGHT//2 + 40))

    pygame.display.flip()
    clock.tick(60)

# Cleanup
cap.release()
cv2.destroyAllWindows()
pygame.quit()
