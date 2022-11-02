import pygame, random
pygame.init()
clock = pygame.time.Clock()  # frame per second

screen_width = 900
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PongGame")


# Hàm rect --> tạo đối tượng
ball = pygame.Rect(screen_width / 2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 10,  screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(0,  screen_height/2 - 70, 10, 140)

"""màu:
    (0,0,0 ) --> màu đen
    (255,255,255) --> màu trắng
    pygame.Color("red")
"""
light_grey = (200, 200, 200)
bg_color = pygame.Color("grey12")

player_point = 0
opponent_point = 0
score_font = pygame.font.Font('freesansbold.ttf', 24)


# Tốc độ
ball_speed_x = 7
ball_speed_y = 7

player_speed = 0
opponent_speed = 7


def ball_start():
    global ball_speed_y,ball_speed_x
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN: # ấn nút
            if event.key == pygame.K_DOWN: #nút mũi tên xuông
                player_speed += 7
            if event.key == pygame.K_UP: #nút mũi tên lên
                player_speed -= 7
        if event.type == pygame.KEYUP: # thả nút
            if event.key == pygame.K_DOWN: #nút mũi tên xuông
                player_speed -= 7
            if event.key == pygame.K_UP: #nút mũi tên lên
                player_speed += 7

    player.y += player_speed


    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #  Nếu bóng chạm vào khung sẽ bật lại

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    elif ball.left <= 0 or ball.right >= screen_width:
        ball_start()


    #  Kiểm tra bóng chạm người chới / đối thủ
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.top -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


    if ball.colliderect(player):
        player_point += 1
    elif ball.colliderect(opponent):
        opponent_point += 1
    # Màu nền

    screen.fill(bg_color)

    #  Vẽ 2 thanh ngang
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)

    #  Vẽ quả cầu
    pygame.draw.ellipse(screen, light_grey, ball)

    #  Vẽ thanh lưới
    pygame.draw.aaline(screen, light_grey, (screen_width/2,
                       0), (screen_width/2, screen_height))

    #  Điểm
    player_score = score_font.render(f"{player_point}", False, light_grey)
    screen.blit(player_score,(800,500))

    opponent_score = score_font.render(f"{opponent_point}", False, light_grey)
    screen.blit(opponent_score,(100,500))
    pygame.display.flip()
    clock.tick(60)

