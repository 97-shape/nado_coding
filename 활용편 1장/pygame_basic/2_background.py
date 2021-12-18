import pygame

pygame.init()  # 초기화(필수!)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/Sanguook/nado_coding/pythonProject1/pygame_basic/background.png")  # \\ 혹은 /

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")  # 게임 이름

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # (필수) 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 끝남

    # screen.fill((0, 0, 255))  # 배경 채우기
    screen.blit(background, (0, 0))  # 배경 그리기

    pygame.display.update()  # 게임화면을 다시 그리기! (배경을 계속 호출해서 표시)

# pygame 종료
pygame.quit()