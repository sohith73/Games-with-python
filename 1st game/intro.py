import pygame, sys, time
pygame.init()
width, height = 1280, 720
disp = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
# test = pygame.Surface((400,250))
img = pygame.image.load('E://Programing Code//PROJECTS//games assets//asteroid_shooter_files//asteroid_shooter_files//project_1 - blank window//graphics/ship.png').convert_alpha()
img1 = pygame.image.load('E://Programing Code//PROJECTS//games assets//asteroid_shooter_files//asteroid_shooter_files//project_1 - blank window//graphics/ship.png').convert_alpha()
font = pygame.font.Font('E://Programing Code//PROJECTS//games assets//asteroid_shooter_files//asteroid_shooter_files//project_1 - blank window//graphics/subatomic.ttf', 50)
text  = font.render('Space game', True, 'red')
i = 0
y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    # test.fill((39, 69, 99))
    disp.fill('wheat')
    disp.blit(img, ((100+i), 200))
    disp.blit(img, (100 , (200+y)))
    disp.blit(text,(100, 100))
    # disp.blit(test, ((1180-400), 0))
    pygame.display.update()
    i = i+10
    y = y+10
    # time.sleep(0.0002)
    if i > 1180:
        i = 0
    if y > 720:
        y = 0