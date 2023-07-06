import pygame

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Meu jogo em Python")

bg = pygame.image.load('images/Flat_Game_Background_1.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x,y))

alien = pygame.image.load('images/nave-espacial-ovni.png').convert_alpha()
alien = pygame.transform.scale(alien, (80, 80))


playerImg = pygame.image.load('images/Nave.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerImg = pygame.transform.rotate(playerImg, 45)

pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            
    screen.blit(bg, (0,0))
    
    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0)) #criando o fundo
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))
        
    #comandos
    
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 2
    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 2
    if tecla[pygame.K_LEFT] and pos_player_x > 1:
        pos_player_x -= 2
    if tecla[pygame.K_RIGHT] and pos_player_x < 1000:
        pos_player_x += 2
    #movimento velocidade
    x-=1
    
    screen.blit(alien, (pos_alien_y, pos_alien_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))
    
    
    
    pygame.display.update()