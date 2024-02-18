import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bombaster')

play_img = pygame.image.load('play.png')
play_rect = play_img.get_rect()
play_rect.center = (400, 300)

player_img = pygame.image.load('player.png')
player_rect = player_img.get_rect()
player_rect.center = (400, 300)
player_score = 0
player_speed = 5

bomb_img = pygame.image.load('bomb.png')
pygame.display.set_icon(bomb_img)

bg = pygame.image.load("space.png")

fps = 60
clock = pygame.time.Clock()

pomegranate_img = pygame.image.load('pomegranate.png')
pomegranate_rect = pomegranate_img.get_rect()

def get_random_position():
    return random.randint(0, 800), random.randint(0, 600)

pomegranate_rect.center = get_random_position()

font = pygame.font.Font(None, 48)

spike_img = pygame.image.load('spike_ball.png')
spike_rect = spike_img.get_rect()
spike_rect.topleft = 0, 0
spike_speed = 3
spike_direction_x = 1
spike_direction_y = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            screen.blit(bg, (0, 0))
        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                if player_rect.left > 0:
                    player_rect.x -= player_speed
            if keys[pygame.K_d]:
                if player_rect.right < 800:
                    player_rect.x += player_speed
            if keys[pygame.K_w]:
                if player_rect.top > 0:
                    player_rect.y -= player_speed
            if keys[pygame.K_s]:
                if player_rect.bottom < 600:
                    player_rect.y += player_speed
            
            if player_rect.colliderect(spike_rect):
                text = font.render('Game Over ', True, (200, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (400, 300)
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.delay(5000)
                running = False
            
            if player_rect.colliderect(pomegranate_rect):
                player_score += 1
                pomegranate_rect.center = get_random_position()
                spike_speed += 0.1
            
            if spike_rect.left < 0 or spike_rect.right > 800:
                spike_direction_x = -spike_direction_x
            if spike_rect.top < 0 or spike_rect.bottom > 600:
                spike_direction_y = -spike_direction_y

            spike_rect.x += spike_speed * spike_direction_x
            spike_rect.y += spike_speed * spike_direction_y

            screen.blit(spike_img, spike_rect)
            screen.blit(player_img, player_rect)
            screen.blit(pomegranate_img, pomegranate_rect)

            score_text = font.render(f'Очки: {player_score}', True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
            
            pygame.display.update()
            clock.tick(fps)
pygame.quit()
exit()