import pygame

pygame.init()
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("sehee game")

#배경 불러오기
background = pygame.image.load("/Users/sehee/pythonWorkspace/pygame_basic/background.png")

#캐릭터 불러오기
character = pygame.image.load("/Users/sehee/pythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0] #가로
character_height = character_size[1] #세로
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#0,0에 배경 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() #화면을 다시 그리기 (반드시 계속 호출)

pygame.quit()