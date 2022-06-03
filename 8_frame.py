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
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

#이동할 좌표

to_x = 0
to_y = 0

#이동속도

character_speed = 0.6

#적 캐릭터
enemy = pygame.image.load("/Users/sehee/pythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0] #가로
enemy_height = enemy_size[1] #세로
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

#폰트정의
game_font = pygame.font.Font(None, 40) #폰트, 크기
#시간
total_time = 10
#시간계산
start_ticks = pygame.time.get_ticks()


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
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: #키에서 손을 뗐을때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

##3. 게임캐릭터 위치 정의
    character_x_pos += to_x *dt
    character_y_pos += to_y *dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


##4. 충돌처리

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

#충돌체크

    if character_rect.colliderect(enemy_rect):
        print("충돌!")
        running = False

##5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    #경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) /1000 #초 단위로
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))

    #시간이 0 이하이면 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃!")
        running = False

    pygame.display.update() #화면을 다시 그리기 (반드시 계속 호출)

#끝나기 전 대기
pygame.time.delay(2000)
#종료
pygame.quit()