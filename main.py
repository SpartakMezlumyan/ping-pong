import pygame
import random
import math

pygame.init()
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PingPong")

player_speed = 2
first_player_x = (width - width) + 7
first_player_y = 150
second_player_x = width - 20
second_player_y = 300
player_width = 13
player_height = 100

circle_radius = 20
circle_x = width // 2
circle_y = height // 2
circle_speed = 3
circle_angle = random.uniform(0, math.pi * 2)
win = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)

score_left = 0
score_right = 0

bacgraund_image = pygame.image.load("Images/TEXT-MODE.png").convert_alpha()
background_image = pygame.transform.scale(bacgraund_image, (width, height))

game_over = False
restart_button = pygame.Rect(width // 2 - 50, height // 2, 100, 50)

running = True
while running:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            mouse_pos = event.pos
            if restart_button.collidepoint(mouse_pos):
                game_over = False
                score_left = 0
                score_right = 0
                first_player_y = 150
                second_player_y = 300
                circle_x = width // 2
                circle_y = height // 2
                circle_angle = random.uniform(0, math.pi * 2)

    if game_over:
        screen.fill(black)
        font = pygame.font.Font(None, 72)
        if score_left == 16:
            gameover_text = font.render("Game Over!", True, white)
            text_surface = font.render("Player on the left wins!", True, white)
        else:
            gameover_text = font.render("Game Over!", True, white)
            text_surface = font.render("Player on the right wins!", True, white)

        text_rect = text_surface.get_rect(center=(width / 2, height / 2 - 35))
        gameover_text_rect = gameover_text.get_rect(center=(width / 2, height / 2 - 95))
        screen.blit(text_surface, text_rect)
        screen.blit(gameover_text, gameover_text_rect)

        font = pygame.font.Font('Fonts/Roboto-Black.ttf', 55)
        restart_text = font.render("Restart", True, white, )
        pygame.draw.rect(screen, black, restart_button)
        restart_rect = restart_text.get_rect(center=restart_button.center)
        screen.blit(restart_text, restart_rect)

    else:
        screen.fill((0, 0, 0))

        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (first_player_x, first_player_y, player_width, player_height))
        pygame.draw.rect(screen, (255, 255, 255), (second_player_x, second_player_y, player_width, player_height))
        pygame.draw.circle(win, "Red", (circle_x, circle_y), circle_radius)

        font = pygame.font.Font(None, 36)
        text_surface_left = font.render(str(score_left), True, white)
        text_surface_right = font.render(str(score_right), True, white)
        screen.blit(text_surface_left, (width / 2 + 100, 50))
        screen.blit(text_surface_right, (width / 2 + (-100), 50))

        for i in range(10000):
            pygame.draw.rect(screen, (255, 255, 255), (width / 2, i * 25, 13, 15))

        if keys[pygame.K_w]:
            first_player_y -= player_speed
        elif keys[pygame.K_s]:
            first_player_y += player_speed

        if keys[pygame.K_UP]:
            second_player_y -= player_speed
        elif keys[pygame.K_DOWN]:
            second_player_y += player_speed

        if circle_x <= circle_radius:
            score_right += 1
        elif circle_x >= width - circle_radius:
            score_left += 1

        if score_right == 10 or score_left == 10:
            game_over = True

        first_player_x = max(0, min(first_player_x, width - player_width))
        first_player_y = max(0, min(first_player_y, height - player_height))

        second_player_x = max(0, min(second_player_x, width - player_width))
        second_player_y = max(0, min(second_player_y, height - player_height))

        circle_x += circle_speed * math.cos(circle_angle)
        circle_y += circle_speed * math.sin(circle_angle)

        if circle_x <= circle_radius or circle_x >= width - circle_radius:
            circle_angle = math.pi - circle_angle
        if circle_y <= circle_radius or circle_y >= height - circle_radius:
            circle_angle = -circle_angle

        circle_x = max(circle_radius, min(circle_x, width - circle_radius))
        circle_y = max(circle_radius, min(circle_y, height - circle_radius))

        player_rect = pygame.Rect(first_player_x, first_player_y, 13, 100)
        second_player_rect = pygame.Rect(second_player_x, second_player_y, 13, 100)
        ball_rect = pygame.Rect(circle_x - circle_radius, circle_y - circle_radius, circle_radius * 2, circle_radius * 2)

        if ball_rect.colliderect(player_rect) or ball_rect.colliderect(second_player_rect):
            circle_angle = math.pi - circle_angle

    pygame.display.flip()

pygame.quit()
