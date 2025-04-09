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
isabella_scale = 0.5
isabella_image = pygame.transform.scale(isabella_image, (p_width, p_height))
isabella_x = 200
isabella_y = 0
isabella_vx = 20
isabella_vy = 0
i_width = isabella_image.get_width()
i_height = isabella_image.get_height()

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
    
    isabella_rect = pygame.rect.Rect(isabella_x, isabella_y, i_width, i_height)
    for rect in rect_p[:]:
        if isabella_rect.colliderect(rect):
            rect_p.remove(rect)
            isabella_score += 1
    
    screen.blit(phineas_image, (phineas_x, phineas_y))
    screen.blit(isabella_image, (isabella_x, isabella_y))
    
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
    
    pygame.display.flip()

print(f"Phineas score: {phineas_score}")
print(f"Isabella score: {isabella_score}")

pygame.quit()