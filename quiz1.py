from random import randint
import pygame
##기본 초기화 반드시 해야 할 것

pygame.init()
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("sehee game")

clock = pygame.time.Clock()
############################

#1. 사용자 게임 초기화 (배경화면, 이미지, 좌표, 속도, 폰트 등 설정)
#배경 불러오기
background = pygame.image.load("/Users/sehee/pythonWorkspace/pygame_basic/background.png")

#캐릭터 불러오기
character = pygame.image.load("/Users/sehee/pythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0] #가로
character_height = character_size[1] #세로
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

#이동할 좌표
to_x = 0

#이동속도

character_speed = 10

#적 캐릭터
enemy = pygame.image.load("/Users/sehee/pythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0] #가로
enemy_height = enemy_size[1] #세로
enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

#폰트정의
# #시간

running = True

while running:

    dt = clock.tick(60) #초 당 프레임 수

##2. 이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: #키를 눌렀을때
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP: #키에서 손을 뗐을때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            

##3. 게임캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    

##4. 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    # character_rect.right = character_x_pos
    character_rect.top = character_y_pos
    # character_rect.bottom = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    # enemy_rect.right = enemy_x_pos
    # enemy_rect.bottom = enemy_y_pos
    enemy_rect.top = enemy_y_pos


#충돌체크
    if enemy_rect.colliderect(character_rect):

        print("충돌!")
        running = False

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = randint(0, screen_width - enemy_width)

##5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, screen_height - character_height))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    
    pygame.display.update() #화면을 다시 그리기 (반드시 계속 호출)

#끝나기 전 대기
#종료
pygame.quit()