import pygame
import os
import time
import random
import sys

pygame.init()
color = (173, 209, 255)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
display_width = 620
display_height = 680
os.environ['SDL_VIDEO_CENTERED'] = '1'
game = pygame.display.set_mode((display_width, display_height))  # pygame.NOFRAME is use for not to move Pygame window
pygame.display.set_caption("RACING | FURY")
clock = pygame.time.Clock()
img = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c0.jpg')
bg = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\s.jpg')
y_strip = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\line.jpg')
strip = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\strip.jpg')
main_bg = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\f.jpg')
int_bg = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\rc.jpg')
car_width = 46
global pause
pause = True


def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        game.blit(main_bg, (0, 0))
        font = pygame.font.SysFont(None, 75)
        text = font.render("RACING FURY", True, white)
        game.blit(text, (135, 36))
        button("START", 60, 560, 100, 36, white, color, "play")
        button("HOW TO PLAY ?", 218, 610, 180, 36, white, color, "intro")
        button("CLOSE", 450, 560, 100, 36, white, color, "quit")
        pygame.display.update()
        clock.tick(50)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "intro":
                instruction()
            elif action == "main":
                intro_loop()
            elif action == "pause":
                paused()
            elif action == "unpause":
                Unpause()

    else:
        pygame.draw.rect(game, ic, (x, y, w, h))
    s_text = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, s_text)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    game.blit(textsurf, textrect)


def instruction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
        game.blit(int_bg, (0, 0))
        s_text = pygame.font.Font("freesansbold.ttf", 18)
        m_text = pygame.font.Font("freesansbold.ttf", 30)
        l_text = pygame.font.Font("freesansbold.ttf", 50)
        font = pygame.font.SysFont(None, 27)
        text = font.render("This is a 2D car game which is developed in Python using Pygame ", True, black)
        game.blit(text, (20, 200))
        TextSurf, TextRect = text_objects("INSTRUCTION", l_text)
        TextRect.center = (300, 100)
        game.blit(TextSurf, TextRect)
        stextSurf, stextRect = text_objects("ARROW LEFT : LEFT TURN", s_text)
        stextRect.center = (150, 450)
        hTextSurf, hTextRect = text_objects("ARROW RIGHT : RIGHT TURN", s_text)
        hTextRect.center = (160, 500)
        atextSurf, atextRect = text_objects("ARROW UP : ACCELERATOR", s_text)
        atextRect.center = (158, 550)
        rtextSurf, rtextRect = text_objects("ARROW DOWN : BRAKE", s_text)
        rtextRect.center = (140, 600)
        ptextSurf, ptextRect = text_objects("P : PAUSE", s_text)
        ptextRect.center = (80, 400)
        sTextSurf, sTextRect = text_objects("CONTROLS", m_text)
        sTextRect.center = (120, 350)
        game.blit(sTextSurf, sTextRect)
        game.blit(stextSurf, stextRect)
        game.blit(hTextSurf, hTextRect)
        game.blit(atextSurf, atextRect)
        game.blit(rtextSurf, rtextRect)
        game.blit(ptextSurf, ptextRect)
        game.blit(sTextSurf, sTextRect)
        button("BACK", 480, 610, 100, 35, white, color, "main")
        pygame.display.update()
        clock.tick(30)


def paused():
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        game.blit(int_bg, (0, 0))
        font = pygame.font.SysFont(None, 100)
        text = font.render("PAUSED", True, black)
        game.blit(text, (180, 100))
        button("CONTINUE", 60, 610, 120, 36, white, color, "unpause")
        button("RESTART", 260, 610, 100, 36, white, color, "play")
        button("MENU", 480, 610, 100, 36, white, color, "main")
        pygame.display.update()
        clock.tick(30)


def Unpause():
    global pause
    pause = False


def countdown_bg():
    font = pygame.font.SysFont(None, 25)
    x = (display_width * 0.45)
    y = (display_height * 0.84)
    game.blit(bg, (0, 0))
    game.blit(bg, (0, 200))
    game.blit(bg, (0, 400))
    game.blit(bg, (500, 0))
    game.blit(bg, (500, 200))
    game.blit(bg, (500, 400))
    game.blit(y_strip, (310, 0))
    game.blit(y_strip, (310, 100))
    game.blit(y_strip, (310, 200))
    game.blit(y_strip, (310, 300))
    game.blit(y_strip, (310, 400))
    game.blit(y_strip, (310, 500))
    game.blit(y_strip, (310, 600))
    game.blit(strip, (120, 0))
    game.blit(strip, (120, 0))
    game.blit(strip, (120, 0))
    game.blit(strip, (500, 0))
    game.blit(strip, (500, 0))
    game.blit(strip, (500, 0))
    game.blit(img, (x, y))
    text = font.render("PASSED: 0", True, black)
    score = font.render("SCORE: 0", True, red)
    game.blit(text, (0, 50))
    game.blit(score, (0, 25))
    button("II", 505, 1, 50, 25, white, red, "pause")


def countdown():
    countdown = True

    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        game.fill(color)
        countdown_bg()
        large = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects("3", large)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        game.fill(color)
        countdown_bg()
        large = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects("2", large)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        game.fill(color)
        countdown_bg()
        large = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects("1", large)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        game.fill(color)
        countdown_bg()
        large = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects("GO!!!", large)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        game_loop()


def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c1.jpg')
    elif obs == 1:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c2.jpg')
    elif obs == 2:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c3.jpg')
    elif obs == 3:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c4.jpg')
    elif obs == 4:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c5.jpg')
    elif obs == 5:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-ProjectL\\Images\\cars\\c6.jpg')
    elif obs == 6:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c7.jpg')
    elif obs == 7:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c8.jpg')
    elif obs == 8:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c9.jpg')
    elif obs == 9:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c16.jpg')
    elif obs == 10:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c17.jpg')
    elif obs == 11:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c3.jpg')
    elif obs == 12:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c13.jpg')
    elif obs == 13:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c17.jpg')
    elif obs == 14:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\b1.jpg')
    elif obs == 15:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c15.jpg')
    elif obs == 16:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\c9.jpg')
    elif obs == 17:
        obs_pic = pygame.image.load('C:\\Users\\Nikith\\PycharmProjects\\Pygame-Project\\Images\\cars\\b0.jpg')
    game.blit(obs_pic, (obs_startx, obs_starty))


def score_system(passed, score):
    font = pygame.font.SysFont(None, 30)
    text = font.render("PASSED: " + str(passed), True, black)
    score = font.render("SCORE: " + str(score), True, red)
    game.blit(text, (0, 50))
    game.blit(score, (0, 25))


def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    large = pygame.font.Font("freesansbold.ttf", 50)
    textsurf, textrect = text_objects(text, large)
    textrect.center = ((display_width / 2), (display_height / 2))
    game.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("CRASHED")


def background():
    game.blit(bg, (0, 0))
    game.blit(bg, (0, 200))
    game.blit(bg, (0, 400))
    game.blit(bg, (500, 0))
    game.blit(bg, (500, 200))
    game.blit(bg, (500, 400))
    game.blit(y_strip, (310, 0))
    game.blit(y_strip, (310, 100))
    game.blit(y_strip, (310, 200))
    game.blit(y_strip, (310, 300))
    game.blit(y_strip, (310, 400))
    game.blit(y_strip, (310, 500))
    game.blit(y_strip, (310, 600))
    game.blit(strip, (120, 0))
    game.blit(strip, (120, 0))
    game.blit(strip, (120, 0))
    game.blit(strip, (500, 0))
    game.blit(strip, (500, 0))
    game.blit(strip, (500, 0))


def car(x, y):
    game.blit(img, (x, y))


def game_loop():
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.84)
    x_change = 0
    obstacle_speed = 8
    obs = 0
    obs_startx = random.randrange(200, (display_width - 200))
    obs_starty = -750
    obs_width = 50
    obs_height = 95
    level = 0
    passed = 0
    score = 0
    x2 = 7
    fps = 120

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_d:
                    x_change = 5
                if event.key == pygame.K_w:
                    obstacle_speed += 2
                if event.key == pygame.K_s:
                    obstacle_speed -= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
        x += x_change
        pause = True
        game.fill(color)
        rel_y = x2 % bg.get_rect().width
        game.blit(bg, (0, rel_y - bg.get_rect().width))
        game.blit(bg, (500, rel_y - bg.get_rect().width))
        if rel_y < 620:
            game.blit(bg, (0, rel_y))
            game.blit(bg, (500, rel_y))
            game.blit(y_strip, (310, rel_y))
            game.blit(y_strip, (310, rel_y + 100))
            game.blit(y_strip, (310, rel_y + 200))
            game.blit(y_strip, (310, rel_y + 300))
            game.blit(y_strip, (310, rel_y + 400))
            game.blit(y_strip, (310, rel_y + 500))
            game.blit(y_strip, (310, rel_y + 600))
            game.blit(y_strip, (310, rel_y - 100))
            game.blit(strip, (120, rel_y - 200))
            game.blit(strip, (120, rel_y + 20))
            game.blit(strip, (120, rel_y + 30))
            game.blit(strip, (500, rel_y - 100))
            game.blit(strip, (500, rel_y + 20))
            game.blit(strip, (500, rel_y + 30))
        x2 += obstacle_speed

        obs_starty -= (obstacle_speed / 4)
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed
        car(x, y)
        score_system(passed, score)
        if x > 500 - car_width or x < 115:
            crash()
        if x > display_width - (car_width + 115) or x < 115:
            crash()
        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(170, (display_width - 170))
            obs = random.randrange(0, 17)
            passed = passed + 1
            score = passed * 10
            if int(passed) % 10 == 0:
                level = level + 1
                obstacle_speed + 2
                large = pygame.font.Font("freesansbold.ttf", 50)
                textsurf, textrect = text_objects("LEVEL " + str(level), large)
                textrect.center = ((display_width / 2), (display_height / 2))
                game.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                crash()
        button("II", 505, 1, 50, 25, white, red, "pause")
        pygame.display.update()
        clock.tick(60)


intro_loop()
game_loop()
pygame.quit()
quit()
