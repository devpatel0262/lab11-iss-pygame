import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True

phineas_image = pygame.image.load("assets/images/phineas_flipped.png")
phineas_x = 50
phineas_y = 0
phineas_vx = 20
phineas_vy = 0

p_width = phineas_image.get_width()
p_height = phineas_image.get_height()

isabella_image = pygame.image.load("assets/images/isabella.png")
isabella_image = pygame.transform.scale(isabella_image, (p_width + 10, p_height + 25))
isabella_x = 200
isabella_y = 0
isabella_vx = 20
isabella_vy = 0

i_width = isabella_image.get_width()
i_height = isabella_image.get_height()

perry_image = pygame.image.load("assets/images/perry.png")
perry_scale = 0.4
perry_image = pygame.transform.scale(perry_image, (int(perry_image.get_width() * perry_scale), int(perry_image.get_height() * perry_scale)))

perry_visible = False
perry_timer = 0
perry_message = ""

phineas_last_milestone = 0
isabella_last_milestone = 0

gravity = 2006
clock = pygame.time.Clock()

rect_g = []
rect_p = []

phineas_score = 0
isabella_score = 0

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        phineas_vy = -600
    if keys[pygame.K_RIGHT]:
        phineas_x += phineas_vx
    if keys[pygame.K_LEFT]:
        phineas_x -= phineas_vx

    if keys[pygame.K_w]:
        isabella_vy = -600
    if keys[pygame.K_d]:
        isabella_x += isabella_vx
    if keys[pygame.K_a]:
        isabella_x -= isabella_vx

    screen.fill((0, 0, 0))

    if random.randint(0, 2000) > 1754:
        rect_g.append(pygame.rect.Rect(WIDTH, random.randint(0, HEIGHT), 10, 100))

    if random.randint(0, 2000) > 1754:
        rect_p.append(pygame.rect.Rect(WIDTH, random.randint(0, HEIGHT), 10, 100))

    for rect in rect_g[:]:
        pygame.draw.rect(screen, (0, 255, 0), rect)
        rect.x -= 5
        if rect.x < -10:
            rect_g.remove(rect)

    for rect in rect_p[:]:
        pygame.draw.rect(screen, (255, 150, 200), rect)
        rect.x -= 5
        if rect.x < -10:
            rect_p.remove(rect)

    phineas_rect = pygame.rect.Rect(phineas_x, phineas_y, p_width, p_height)
    for rect in rect_g[:]:
        if phineas_rect.colliderect(rect):
            rect_g.remove(rect)
            phineas_score += 1
            if phineas_score % 100 == 0 and phineas_score != phineas_last_milestone:
                perry_visible = True
                perry_timer = 3
                perry_message = f"Phineas scored {phineas_score} points!!!"
                phineas_last_milestone = phineas_score

    isabella_rect = pygame.rect.Rect(isabella_x, isabella_y, i_width, i_height)
    for rect in rect_p[:]:
        if isabella_rect.colliderect(rect):
            rect_p.remove(rect)
            isabella_score += 1
            if isabella_score % 100 == 0 and isabella_score != isabella_last_milestone:
                perry_visible = True
                perry_timer = 3
                perry_message = f"Isabella scored {isabella_score} points!!!"
                isabella_last_milestone = isabella_score

    screen.blit(phineas_image, (phineas_x, phineas_y))
    screen.blit(isabella_image, (isabella_x, isabella_y))

    if perry_visible:
        perry_timer -= dt*2
        perry_x = WIDTH // 2 - perry_image.get_width() // 2
        perry_y = HEIGHT // 2 - perry_image.get_height() // 2
        screen.blit(perry_image, (perry_x, perry_y))
        font = pygame.font.SysFont(None, 48)
        message_text = font.render(perry_message, True, (0, 255, 255))
        message_x = WIDTH // 2 - message_text.get_width() // 2
        message_y = perry_y + perry_image.get_height() + 10
        screen.blit(message_text, (message_x, message_y))
        if perry_timer <= 0:
            perry_visible = False

    phineas_vy += gravity * dt
    phineas_y += phineas_vy * dt

    isabella_vy += gravity * dt
    isabella_y += isabella_vy * dt

    if phineas_y > HEIGHT - p_height:
        phineas_y = HEIGHT - p_height
        phineas_vy = 0

    if phineas_x < 0:
        phineas_x = 0

    if phineas_x > WIDTH - p_width:
        phineas_x = WIDTH - p_width

    if isabella_y > HEIGHT - i_height:
        isabella_y = HEIGHT - i_height
        isabella_vy = 0

    if isabella_x < 0:
        isabella_x = 0

    if isabella_x > WIDTH - i_width:
        isabella_x = WIDTH - i_width

    font = pygame.font.SysFont(None, 36)
    phineas_score_text = font.render(f"Phineas: {phineas_score}", True, (0, 255, 0))
    isabella_score_text = font.render(f"Isabella: {isabella_score}", True, (255, 150, 200))

    screen.blit(phineas_score_text, (10, 10))
    screen.blit(isabella_score_text, (10, 50))

    pygame.display.flip()

print(f"Phineas score: {phineas_score}")
print(f"Isabella score: {isabella_score}")

pygame.quit()