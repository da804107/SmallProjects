#old school pong game created using pygame
import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
ball = pygame.Rect(screen.get_width()/2 - 15, screen.get_height()/2 - 15, 30, 30)
p1 = pygame.Rect(20, screen.get_height()/2 - 40, 10, 80)
p2 = pygame.Rect(screen.get_width()- 10 - 20, screen.get_height()/2 - 40, 10, 80)
ball_vel = [1, 1]

def player_bounds():
    if p1.top < 0:
        p1.top = 0
    if p1.bottom > screen.get_height():
        p1.bottom = screen.get_height()
    if p2.top < 0:
        p2.top = 0
    if p2.bottom > screen.get_height():
        p2.bottom = screen.get_height()

def ball_bounds():
    if ball.top < 0:
        ball.top = 0
        ball_vel[1] *= -1
    if ball.bottom > screen.get_height():
        ball.bottom = screen.get_height()
        ball_vel[1] *= -1

def ball_collide():
    if p1.colliderect(ball):
        ball_vel[0] *= -1
        ball_vel[0] += .1
    if p2.colliderect(ball):
        ball_vel[0] += .1
        ball_vel[0] *= -1

def game_end():
    if ball.left < 0 or ball.right > screen.get_width():
        return False
    else:
        return True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.draw.ellipse(screen, "white", ball)
    pygame.draw.rect(screen, "white", p1)
    pygame.draw.rect(screen, "white", p2)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1.top -= 300 * dt
    if keys[pygame.K_s]:
        p1.top += 300 * dt
    if keys[pygame.K_UP]:
        p2.top -= 300 * dt
    if keys[pygame.K_DOWN]:
        p2.top += 300 * dt

    player_bounds()

    ball.x += 300 * dt * ball_vel[0]
    ball.y += 300 * dt * ball_vel[1]

    ball_bounds()
    ball_collide()
    running = game_end()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
