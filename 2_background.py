import pygame

pygame.init()
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("sehee game")

#배경 불러오기
background = pygame.image.load("/Users/sehee/pythonWorkspace/pygame_basic/background.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#0,0에 배경 그리기
    screen.blit(background, (0,0))
    pygame.display.update() #화면을 다시 그리기 (반드시 계속 호출)

pygame.quit()